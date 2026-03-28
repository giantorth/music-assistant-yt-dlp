# Music Assistant Server with YouTube Provider

A Home Assistant add-on that packages the [Music Assistant](https://music-assistant.io/) server with a YouTube provider powered by yt-dlp.

## Installation

[![Add to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fgiantorth%2Fmusic-assistant-yt-dlp)

Or manually:

1. In Home Assistant, go to **Settings > Add-ons > Add-on Store**
2. Click the three-dot menu (top right) and select **Repositories**
3. Add this repository URL:
   ```
   https://github.com/giantorth/music-assistant-yt-dlp
   ```
4. Find **Music Assistant Server (YouTube)** in the add-on store and install it

> **Note:** This add-on replaces the official Music Assistant add-on. Do not run both simultaneously — they use the same port (8094).

## How It Works

- The official `ghcr.io/music-assistant/server` image is used as a base
- The YouTube provider is copied into the container's providers directory at build time
- A GitHub Actions workflow checks for new upstream MA releases every 6 hours and rebuilds automatically

## Configuration

Once installed, add the YouTube provider in Music Assistant under **Settings > Providers**. All configuration options are optional — the provider works out of the box with yt-dlp alone.

### YouTube Data API Key

Providing a [YouTube Data API v3](https://console.cloud.google.com/apis/credentials) key improves search reliability and metadata quality by using the official API instead of scraping. When configured, the provider uses the API for search and metadata lookups, falling back to yt-dlp automatically if the API is unavailable or quota is exceeded.

### Artist Playlist Limit

Controls the maximum number of channel playlists returned as albums per artist. Defaults to 25. Can be set between 1 and 100.

### YouTube Cookies

Paste your YouTube cookies to enable playback of age-restricted or member-only content. Two formats are accepted:

- **Netscape/cookies.txt format** — exported via a browser extension such as "Get cookies.txt LOCALLY" (Chrome/Edge) or "cookies.txt" (Firefox)
- **Raw cookie header** — copied from browser DevTools (F12 > Network tab), e.g. `name1=val1; name2=val2`

Cookies may expire over time and need to be refreshed. Leave empty for public content only.

## Updating the YouTube Provider

Edit the files in `music_assistant_youtube/youtube_provider/` and push to `main`. The build workflow will automatically rebuild and publish new container images.

## Architecture Support

- `amd64`
- `aarch64`
