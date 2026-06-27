"""Synchronous yt-dlp wrapper functions for the YouTube provider.

All functions in this module are blocking and intended to be called via
asyncio.to_thread() from the async provider layer.
"""

from __future__ import annotations

import logging
import time
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

from music_assistant_models.errors import UnplayableMediaError

from .constants import LIVE_STATUSES, YT_DOMAIN

_LOGGER = logging.getLogger(__name__)

# Preferred audio format IDs in priority order (highest quality first).
# Opus formats (WebM), then AAC (M4A).
PREFERRED_AUDIO_FORMAT_IDS = [
    251,  # Opus 160 kbps
    250,  # Opus 70 kbps
    249,  # Opus 50 kbps
    141,  # AAC 256 kbps
    140,  # AAC 128 kbps
    139,  # AAC 48 kbps
    171,  # Vorbis 128 kbps
]

# Number of retries for stream extraction.
EXTRACT_RETRIES = 3
EXTRACT_RETRY_DELAY = 1.0  # seconds


def is_live_entry(entry: dict[str, Any]) -> bool:
    """Return True if the yt-dlp entry represents an active live stream.

    :param entry: Raw yt-dlp info dict.
    """
    if entry.get("is_live"):
        return True
    return entry.get("live_status", "") in LIVE_STATUSES


def search_yt(
    yt_dlp: Any, ydl_opts: dict[str, Any], query: str, limit: int
) -> list[dict[str, Any]]:
    """Run a YouTube search and return flat video entries (no stream extraction).

    :param yt_dlp: The imported yt_dlp module.
    :param ydl_opts: Base yt-dlp options dict.
    :param query: Search query string.
    :param limit: Maximum number of results to return.
    """
    opts = {**ydl_opts, "extract_flat": True, "skip_download": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"ytsearch{limit}:{query}", download=False)
    return info.get("entries", []) if info else []


def extract_video_info(
    yt_dlp: Any, ydl_opts: dict[str, Any], video_id: str
) -> dict[str, Any] | None:
    """Extract full video metadata for a given video id.

    :param yt_dlp: The imported yt_dlp module.
    :param ydl_opts: Base yt-dlp options dict.
    :param video_id: YouTube video ID.
    """
    # Use permissive format to avoid "Requested format is not available" errors —
    # we only need metadata here, not a specific stream format.
    opts = {**ydl_opts, "skip_download": True, "format": "bestaudio/best"}
    with yt_dlp.YoutubeDL(opts) as ydl:
        result: dict[str, Any] | None = ydl.extract_info(
            f"{YT_DOMAIN}/watch?v={video_id}", download=False
        )
    return result


def search_channels(
    yt_dlp: Any, ydl_opts: dict[str, Any], query: str, limit: int
) -> list[dict[str, Any]]:
    """Run a YouTube search filtered to channels and return flat entries.

    :param yt_dlp: The imported yt_dlp module.
    :param ydl_opts: Base yt-dlp options dict.
    :param query: Search query string.
    :param limit: Maximum number of results to return.
    """
    opts = {**ydl_opts, "extract_flat": True, "skip_download": True, "playlistend": limit}
    url = f"{YT_DOMAIN}/results?search_query={quote_plus(query)}&sp=EgIQAg%3D%3D"
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
    if not info:
        return []
    return [e for e in info.get("entries", []) if e][:limit]


def search_playlists(
    yt_dlp: Any, ydl_opts: dict[str, Any], query: str, limit: int
) -> list[dict[str, Any]]:
    """Run a YouTube search filtered to playlists and return flat entries.

    :param yt_dlp: The imported yt_dlp module.
    :param ydl_opts: Base yt-dlp options dict.
    :param query: Search query string.
    :param limit: Maximum number of results to return.
    """
    opts = {**ydl_opts, "extract_flat": True, "skip_download": True, "playlistend": limit}
    url = f"{YT_DOMAIN}/results?search_query={quote_plus(query)}&sp=EgIQAw%3D%3D"
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
    if not info:
        return []
    return [e for e in info.get("entries", []) if e][:limit]


def extract_channel_videos(
    yt_dlp: Any, ydl_opts: dict[str, Any], channel_id: str, limit: int
) -> list[dict[str, Any]]:
    """Extract flat video entries from a channel's videos tab.

    :param yt_dlp: The imported yt_dlp module.
    :param ydl_opts: Base yt-dlp options dict.
    :param channel_id: YouTube channel ID.
    :param limit: Maximum number of video entries to return.
    """
    opts = {
        **ydl_opts,
        "extract_flat": True,
        "skip_download": True,
        "playlistend": limit,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"{YT_DOMAIN}/channel/{channel_id}/videos", download=False)
    if not info:
        return []
    return [e for e in info.get("entries", []) if e][:limit]


def extract_channel_info(
    yt_dlp: Any, ydl_opts: dict[str, Any], channel_id: str
) -> dict[str, Any] | None:
    """Extract channel metadata for a given channel id.

    :param yt_dlp: The imported yt_dlp module.
    :param ydl_opts: Base yt-dlp options dict.
    :param channel_id: YouTube channel ID.
    """
    opts = {
        **ydl_opts,
        "extract_flat": True,
        # playlistend=0 fetches channel metadata only, skipping all video entries
        "playlistend": 0,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        result: dict[str, Any] | None = ydl.extract_info(
            f"{YT_DOMAIN}/channel/{channel_id}", download=False
        )
    return result


def extract_channel_playlists(
    yt_dlp: Any, ydl_opts: dict[str, Any], channel_id: str, limit: int
) -> list[dict[str, Any]]:
    """Extract flat playlist entries from a channel's playlists tab.

    :param yt_dlp: The imported yt_dlp module.
    :param ydl_opts: Base yt-dlp options dict.
    :param channel_id: YouTube channel ID.
    :param limit: Maximum number of playlist entries to return.
    """
    opts = {
        **ydl_opts,
        "extract_flat": True,
        "skip_download": True,
        "playlistend": limit,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"{YT_DOMAIN}/channel/{channel_id}/playlists", download=False)
    if not info:
        return []
    return [e for e in info.get("entries", []) if e][:limit]


def extract_playlist_info(
    yt_dlp: Any, ydl_opts: dict[str, Any], playlist_id: str
) -> dict[str, Any] | None:
    """Extract playlist metadata (without video entries).

    :param yt_dlp: The imported yt_dlp module.
    :param ydl_opts: Base yt-dlp options dict.
    :param playlist_id: YouTube playlist ID.
    """
    opts = {
        **ydl_opts,
        "extract_flat": True,
        "playlistend": 0,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        result: dict[str, Any] | None = ydl.extract_info(
            f"{YT_DOMAIN}/playlist?list={playlist_id}", download=False
        )
    return result


def extract_playlist_videos(
    yt_dlp: Any, ydl_opts: dict[str, Any], playlist_id: str, limit: int
) -> list[dict[str, Any]]:
    """Extract flat video entries from a YouTube playlist.

    :param yt_dlp: The imported yt_dlp module.
    :param ydl_opts: Base yt-dlp options dict.
    :param playlist_id: YouTube playlist ID.
    :param limit: Maximum number of video entries to return.
    """
    opts = {
        **ydl_opts,
        "extract_flat": True,
        "skip_download": True,
        "playlistend": limit,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"{YT_DOMAIN}/playlist?list={playlist_id}", download=False)
    if not info:
        return []
    return [e for e in info.get("entries", []) if e][:limit]


def extract_stream_or_live(yt_dlp: Any, ydl_opts: dict[str, Any], video_id: str) -> dict[str, Any]:
    """Extract stream info with retries and multi-format fallback.

    Returns a dict with ``is_live`` set to True or False.
    For VOD, the dict also contains the selected audio stream format fields.
    For live streams, the dict contains ``manifest_url``, ``title``, and ``uploader``.

    :param yt_dlp: The imported yt_dlp module.
    :param ydl_opts: Base yt-dlp options dict.
    :param video_id: YouTube video ID.
    """
    last_err: Exception | None = None
    for attempt in range(EXTRACT_RETRIES):
        try:
            return _extract_stream_or_live_once(yt_dlp, ydl_opts, video_id)
        except (UnplayableMediaError, Exception) as err:
            last_err = err
            if attempt < EXTRACT_RETRIES - 1:
                _LOGGER.warning(
                    "Stream extraction attempt %d/%d failed for %s: %s — retrying",
                    attempt + 1,
                    EXTRACT_RETRIES,
                    video_id,
                    err,
                )
                time.sleep(EXTRACT_RETRY_DELAY * (attempt + 1))
            else:
                _LOGGER.error(
                    "All %d stream extraction attempts failed for %s",
                    EXTRACT_RETRIES,
                    video_id,
                )
    raise UnplayableMediaError(str(last_err)) from last_err


def _extract_stream_or_live_once(
    yt_dlp: Any, ydl_opts: dict[str, Any], video_id: str
) -> dict[str, Any]:
    """Single attempt at stream extraction with multi-format fallback."""
    opts = {**ydl_opts}
    with yt_dlp.YoutubeDL(opts) as ydl:
        try:
            info = ydl.extract_info(f"{YT_DOMAIN}/watch?v={video_id}", download=False)
        except yt_dlp.utils.DownloadError as err:
            raise UnplayableMediaError(str(err)) from err
        if not info:
            raise UnplayableMediaError(f"No stream info found for {video_id}")

        if is_live_entry(info):
            return _extract_hls_manifest(info, video_id)

        formats = info.get("formats") or []

        # 1. Try preferred format IDs in priority order (proven reliable list).
        formats_by_id: dict[int, dict[str, Any]] = {}
        for fmt in formats:
            fmt_id = fmt.get("format_id", "")
            # format_id can be "251" or "251-drc"; extract the numeric part
            numeric_id = fmt_id.split("-")[0] if isinstance(fmt_id, str) else fmt_id
            try:
                formats_by_id[int(numeric_id)] = fmt
            except (ValueError, TypeError):
                continue

        for preferred_id in PREFERRED_AUDIO_FORMAT_IDS:
            if preferred_id in formats_by_id:
                fmt = formats_by_id[preferred_id]
                if fmt.get("url"):
                    _LOGGER.debug("Selected preferred format %d for %s", preferred_id, video_id)
                    return {**fmt, "is_live": False}

        # 2. Fall back to yt-dlp's format selector (handles edge cases).
        format_selector = ydl.build_format_selector("m4a/bestaudio/best")
        stream_format = next(format_selector({"formats": formats}), None)
        if stream_format and stream_format.get("url"):
            _LOGGER.debug(
                "Selected fallback format %s for %s",
                stream_format.get("format_id"),
                video_id,
            )
            return {**stream_format, "is_live": False}

        raise UnplayableMediaError(f"No audio stream found for {video_id}")


def _format_selector_for_stream(stream_format: dict[str, Any]) -> str:
    """Build a yt-dlp format selector for a previously selected stream format."""
    format_id = stream_format.get("format_id")
    if format_id:
        return str(format_id)
    return "m4a/bestaudio/best"


def _resolve_downloaded_path(
    info: dict[str, Any],
    stream_format: dict[str, Any],
    inprogress_dir: Path,
) -> Path:
    """Return the path yt-dlp wrote for a completed download."""
    requested = info.get("requested_downloads") or []
    if requested and requested[0].get("filepath"):
        return Path(requested[0]["filepath"])
    if info.get("filepath"):
        return Path(info["filepath"])
    ext = info.get("ext") or stream_format.get("ext") or "bin"
    candidate = inprogress_dir / f"download.{ext}"
    if candidate.is_file():
        return candidate
    matches = sorted(inprogress_dir.glob("download.*"), key=lambda p: p.stat().st_mtime, reverse=True)
    if matches:
        return matches[0]
    msg = "Download produced no file"
    raise UnplayableMediaError(msg)


def download_audio_to_path(
    yt_dlp: Any,
    ydl_opts: dict[str, Any],
    video_id: str,
    dest_stem: Path,
    stream_format: dict[str, Any],
) -> tuple[Path, dict[str, Any]]:
    """Download VOD audio to disk, preserving the original container.

    Downloads into an isolated in-progress folder, then the caller commits the
    finished file into the cache. Prefer the already-extracted stream URL so the
    cached bytes match the HTTP playback stream.

    :param yt_dlp: The imported yt_dlp module.
    :param ydl_opts: Base yt-dlp options dict.
    :param video_id: YouTube video ID.
    :param dest_stem: Unused path anchor; kept for API compatibility.
    :param stream_format: Selected format dict from extract_stream_or_live.
    :returns: Tuple of (downloaded file path, metadata dict for cache sidecar).
    """
    inprogress_dir = dest_stem.parent / "inprogress"
    inprogress_dir.mkdir(parents=True, exist_ok=True)
    outtmpl = str(inprogress_dir / "download.%(ext)s")
    opts = {
        **ydl_opts,
        "outtmpl": outtmpl,
        "skip_download": False,
        "nopart": True,  # --no-part: write directly in the in-progress folder
        "quiet": ydl_opts.get("quiet", True),
    }
    stream_url = stream_format.get("url")
    watch_url = f"{YT_DOMAIN}/watch?v={video_id}"
    try:
        if stream_url:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(stream_url, download=True)
        else:
            opts_with_format = {**opts, "format": _format_selector_for_stream(stream_format)}
            with yt_dlp.YoutubeDL(opts_with_format) as ydl:
                info = ydl.extract_info(watch_url, download=True)
    except yt_dlp.utils.DownloadError as err:
        raise UnplayableMediaError(str(err)) from err
    if not info:
        raise UnplayableMediaError(f"Download failed for {video_id}")
    downloaded = _resolve_downloaded_path(info, stream_format, inprogress_dir)
    if not downloaded.is_file() or downloaded.stat().st_size == 0:
        raise UnplayableMediaError(f"Download produced no file for {video_id}")
    metadata = {
        "format_id": info.get("format_id") or stream_format.get("format_id"),
        "audio_ext": info.get("ext") or stream_format.get("ext"),
        "audio_channels": info.get("audio_channels") or stream_format.get("audio_channels"),
        "asr": info.get("asr") or stream_format.get("asr"),
        "duration": info.get("duration") or stream_format.get("duration"),
    }
    return downloaded, metadata


def _extract_hls_manifest(info: dict[str, Any], video_id: str) -> dict[str, Any]:
    """Extract HLS manifest URL from a live stream info dict.

    :param info: Raw yt-dlp info dict for a live stream.
    :param video_id: YouTube video ID (for error messages).
    """
    manifest_url = info.get("manifest_url")
    if not manifest_url:
        for fmt in info.get("formats") or []:
            if fmt.get("protocol") in ("m3u8", "m3u8_native") and fmt.get("manifest_url"):
                manifest_url = fmt["manifest_url"]
                break
    if not manifest_url:
        for fmt in info.get("formats") or []:
            if fmt.get("protocol") in ("m3u8", "m3u8_native") and fmt.get("url"):
                manifest_url = fmt["url"]
                break
    if not manifest_url:
        raise UnplayableMediaError(f"No HLS manifest found for live stream {video_id}")
    return {
        "is_live": True,
        "manifest_url": manifest_url,
        "title": info.get("title"),
        "uploader": info.get("uploader") or info.get("channel"),
    }
