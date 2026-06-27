"""YouTube provider for Music Assistant using yt-dlp.

Allows searching and playing YouTube videos as audio without requiring
a YouTube Music account or subscription. Uses yt-dlp for both search
and stream extraction.

Optional YouTube Data API v3 support improves search and metadata quality.
Optional cookie support allows access to age-restricted or member-only content.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from music_assistant_models.config_entries import ConfigEntry, ConfigValueType
from music_assistant_models.enums import ConfigEntryType

from .constants import (
    CONF_ACTION_CLEAR_CACHE,
    CONF_API_KEY,
    CONF_CACHE_DIR,
    CONF_CACHE_ENABLED,
    CONF_CACHE_MAX_SIZE_MB,
    CONF_COOKIES,
    CONF_PLAYLIST_LIMIT,
    DEFAULT_CACHE_DIR,
    DEFAULT_CACHE_ENABLED,
    DEFAULT_CACHE_MAX_SIZE_MB,
    DEFAULT_PLAYLIST_LIMIT,
    SUPPORTED_FEATURES,
)
from .file_cache import FileCache
from .provider import YouTubeProvider

if TYPE_CHECKING:
    from music_assistant_models.config_entries import ProviderConfig
    from music_assistant_models.provider import ProviderManifest

    from music_assistant.mass import MusicAssistant
    from music_assistant.models import ProviderInstanceType


async def setup(
    mass: MusicAssistant, manifest: ProviderManifest, config: ProviderConfig
) -> ProviderInstanceType:
    """Initialize provider(instance) with given configuration."""
    return YouTubeProvider(mass, manifest, config, SUPPORTED_FEATURES)


def _cache_dir_from_values(values: dict[str, ConfigValueType] | None) -> Path:
    """Resolve cache directory from config values."""
    raw = (values or {}).get(CONF_CACHE_DIR, DEFAULT_CACHE_DIR)
    return Path(str(raw) if raw else DEFAULT_CACHE_DIR)


async def get_config_entries(
    mass: MusicAssistant,  # noqa: ARG001
    instance_id: str | None = None,  # noqa: ARG001
    action: str | None = None,
    values: dict[str, ConfigValueType] | None = None,
) -> tuple[ConfigEntry, ...]:
    """Return Config entries to setup this provider."""
    cache_cleared_msg = ""
    if action == CONF_ACTION_CLEAR_CACHE:
        cache = FileCache(_cache_dir_from_values(values), max_size_bytes=None)
        removed = cache.clear_all()
        cache_cleared_msg = f"Cleared {removed} cached video(s). "

    cache_enabled = bool((values or {}).get(CONF_CACHE_ENABLED, DEFAULT_CACHE_ENABLED))
    return (
        ConfigEntry(
            key=CONF_API_KEY,
            type=ConfigEntryType.SECURE_STRING,
            label="YouTube Data API Key (optional)",
            description=(
                "Optional. Enter a YouTube Data API v3 key to use the official API "
                "for search and metadata. This improves reliability and avoids "
                "scraping limits. Create a key at "
                "https://console.cloud.google.com/apis/credentials"
            ),
            required=False,
        ),
        ConfigEntry(
            key=CONF_PLAYLIST_LIMIT,
            type=ConfigEntryType.INTEGER,
            label="Artist playlist limit",
            description=("Maximum number of channel playlists to return as albums per artist."),
            required=False,
            default_value=DEFAULT_PLAYLIST_LIMIT,
            value=DEFAULT_PLAYLIST_LIMIT,
            range=(1, 100),
        ),
        ConfigEntry(
            key=CONF_COOKIES,
            type=ConfigEntryType.SECURE_STRING,
            label="YouTube cookie (for restricted videos)",
            description=(
                "Optional. Paste your YouTube cookies to enable playback of "
                "age-restricted or member-only content.\n\n"
                "How to obtain cookies:\n"
                "1. Install a browser extension such as 'Get cookies.txt LOCALLY' "
                "(Chrome/Edge) or 'cookies.txt' (Firefox).\n"
                "2. Log in to youtube.com with your Google account.\n"
                "3. Use the extension to export cookies for youtube.com "
                "in Netscape/cookies.txt format.\n"
                "4. Paste the full exported text here.\n\n"
                "Alternatively, open browser DevTools (F12) → Network tab → "
                "reload youtube.com → click any request → copy the 'Cookie' "
                "request header value (e.g. 'name1=val1; name2=val2').\n\n"
                "Note: cookies may expire over time and need to be refreshed. "
                "Leave empty for public content only."
            ),
            required=False,
        ),
        ConfigEntry(
            key=CONF_CACHE_ENABLED,
            type=ConfigEntryType.BOOLEAN,
            label="Enable file cache",
            description=(
                "Download and cache YouTube audio on disk for faster replay and seeking. "
                "Live streams are never cached."
            ),
            required=False,
            default_value=DEFAULT_CACHE_ENABLED,
            value=values.get(CONF_CACHE_ENABLED, DEFAULT_CACHE_ENABLED) if values else DEFAULT_CACHE_ENABLED,
        ),
        ConfigEntry(
            key=CONF_CACHE_DIR,
            type=ConfigEntryType.STRING,
            label="Cache directory",
            description=(
                "Directory for cached audio files. Use a persistent mapped path such as "
                "/media/music-assistant-youtube-cache — the add-on container filesystem is "
                "ephemeral (tmpfs) unless you store cache on a volume."
            ),
            required=False,
            default_value=DEFAULT_CACHE_DIR,
            value=values.get(CONF_CACHE_DIR, DEFAULT_CACHE_DIR) if values else DEFAULT_CACHE_DIR,
            depends_on=CONF_CACHE_ENABLED,
            depends_on_value=True,
        ),
        ConfigEntry(
            key=CONF_CACHE_MAX_SIZE_MB,
            type=ConfigEntryType.INTEGER,
            label="Maximum cache size (MB)",
            description=(
                "Maximum total cache size in megabytes. Set to 0 for unlimited. "
                "When exceeded, least-recently-used entries are removed."
            ),
            required=False,
            default_value=DEFAULT_CACHE_MAX_SIZE_MB,
            value=values.get(CONF_CACHE_MAX_SIZE_MB, DEFAULT_CACHE_MAX_SIZE_MB)
            if values
            else DEFAULT_CACHE_MAX_SIZE_MB,
            range=(0, 1_000_000),
            depends_on=CONF_CACHE_ENABLED,
            depends_on_value=True,
        ),
        ConfigEntry(
            key="cache_label",
            type=ConfigEntryType.LABEL,
            label=f"{cache_cleared_msg}Use the button below to delete all cached audio files.",
            depends_on=CONF_CACHE_ENABLED,
            depends_on_value=True,
        ),
        ConfigEntry(
            key=CONF_ACTION_CLEAR_CACHE,
            type=ConfigEntryType.ACTION,
            label="Clear file cache",
            description="Delete all cached audio files for this provider.",
            action=CONF_ACTION_CLEAR_CACHE,
            action_label="Clear cache",
            required=False,
            depends_on=CONF_CACHE_ENABLED,
            depends_on_value=True,
        ),
    )
