"""Unit tests for YouTube provider file cache."""

from __future__ import annotations

import json
import time
from pathlib import Path

import pytest

from file_cache import FileCache


@pytest.fixture
def cache_dir(tmp_path: Path) -> Path:
    """Temporary cache root."""
    return tmp_path / "cache"


@pytest.fixture
def file_cache(cache_dir: Path) -> FileCache:
    """FileCache with a 1 KiB size limit for eviction tests."""
    cache = FileCache(cache_dir, max_size_bytes=1024)
    cache.ensure_ready()
    return cache


def test_sanitize_video_id_valid() -> None:
    """Accept standard 11-character YouTube IDs."""
    assert FileCache.sanitize_video_id("dQw4w9WgXcQ") == "dQw4w9WgXcQ"


def test_sanitize_video_id_invalid() -> None:
    """Reject invalid cache keys."""
    with pytest.raises(ValueError):
        FileCache.sanitize_video_id("../etc/passwd")


def test_get_hit_miss(file_cache: FileCache) -> None:
    """Return None when nothing is cached."""
    assert file_cache.get_hit("dQw4w9WgXcQ") is None


def test_commit_and_get_hit(file_cache: FileCache, cache_dir: Path) -> None:
    """Store a file and read it back as a cache hit."""
    video_id = "dQw4w9WgXcQ"
    entry_dir = cache_dir / video_id
    entry_dir.mkdir(parents=True)
    temp_path = entry_dir / "dl-temp.webm"
    temp_path.write_bytes(b"x" * 128)
    metadata = {"audio_ext": "webm", "format_id": "251"}
    file_cache.commit(video_id, temp_path, metadata)
    hit = file_cache.get_hit(video_id)
    assert hit is not None
    assert hit.audio_path.is_file()
    assert hit.audio_path.stat().st_size == 128
    sidecar = json.loads((entry_dir / "metadata.json").read_text(encoding="utf-8"))
    assert sidecar["audio_file"] == "audio.webm"
    assert hit.audio_path.name == "audio.webm"
    assert sidecar["video_id"] == video_id


def test_get_hit_rejects_incomplete_file(file_cache: FileCache, cache_dir: Path) -> None:
    """Reject and remove cache entries that are too small for their duration."""
    video_id = "dQw4w9WgXcQ"
    entry_dir = cache_dir / video_id
    entry_dir.mkdir(parents=True)
    (entry_dir / "audio.webm").write_bytes(b"x" * 100)
    (entry_dir / "metadata.json").write_text(
        json.dumps({"audio_file": "audio.webm", "duration": 300}),
        encoding="utf-8",
    )
    assert file_cache.get_hit(video_id) is None
    assert not entry_dir.exists()


def test_get_hit_rejects_empty_file(file_cache: FileCache, cache_dir: Path) -> None:
    """Do not return hits for zero-byte files."""
    video_id = "dQw4w9WgXcQ"
    entry_dir = cache_dir / video_id
    entry_dir.mkdir(parents=True)
    (entry_dir / "audio.webm").write_bytes(b"")
    (entry_dir / "metadata.json").write_text(
        json.dumps({"audio_file": "audio.webm"}),
        encoding="utf-8",
    )
    assert file_cache.get_hit(video_id) is None


def test_get_hit_skips_while_downloading(file_cache: FileCache, cache_dir: Path) -> None:
    """Do not serve partial cache entries while a download is in progress."""
    video_id = "dQw4w9WgXcQ"
    assert file_cache.try_acquire_download_lock(video_id)
    entry_dir = cache_dir / video_id
    (entry_dir / "audio.webm").write_bytes(b"partial")
    (entry_dir / "metadata.json").write_text(
        json.dumps({"audio_file": "audio.webm", "duration": 10}),
        encoding="utf-8",
    )
    assert file_cache.get_hit(video_id) is None
    file_cache.release_download_lock(video_id)


def test_clear_all(file_cache: FileCache, cache_dir: Path) -> None:
    """Remove all cached entries."""
    for vid in ("aaaaaaaaaaa", "bbbbbbbbbbb"):
        entry = cache_dir / vid
        entry.mkdir()
        (entry / "audio.webm").write_bytes(b"data")
        (entry / "metadata.json").write_text(
            json.dumps({"audio_file": "audio.webm"}),
            encoding="utf-8",
        )
    removed = file_cache.clear_all()
    assert removed == 2
    assert not any(cache_dir.iterdir())


def test_lru_eviction(file_cache: FileCache, cache_dir: Path) -> None:
    """Evict least-recently-used entries when over size limit."""
    old_id = "aaaaaaaaaaa"
    new_id = "bbbbbbbbbbb"
    for video_id, accessed in ((old_id, 1.0), (new_id, 1000.0)):
        entry = cache_dir / video_id
        entry.mkdir()
        (entry / "audio.webm").write_bytes(b"x" * 600)
        (entry / "metadata.json").write_text(
            json.dumps(
                {
                    "audio_file": "audio.webm",
                    "last_accessed": accessed,
                    "cached_at": accessed,
                }
            ),
            encoding="utf-8",
        )
    file_cache.enforce_size_limit()
    assert file_cache.get_hit(old_id) is None
    assert file_cache.get_hit(new_id) is not None


def test_commit_updates_last_accessed(file_cache: FileCache, cache_dir: Path) -> None:
    """get_hit updates last_accessed in the sidecar."""
    video_id = "dQw4w9WgXcQ"
    entry_dir = cache_dir / video_id
    entry_dir.mkdir(parents=True)
    temp_path = entry_dir / "dl-temp.m4a"
    temp_path.write_bytes(b"cached-audio")
    before = time.time()
    file_cache.commit(video_id, temp_path, {"audio_ext": "m4a"})
    time.sleep(0.01)
    file_cache.get_hit(video_id)
    sidecar = json.loads((entry_dir / "metadata.json").read_text(encoding="utf-8"))
    assert sidecar["last_accessed"] >= before
