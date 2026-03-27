## 2.8.1
- Upstream Music Assistant server update to 2.8.1

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.0](https://github.com/music-assistant/server/releases/tag/2.8.0)_

### 🐛 Bugfixes

- Fix race condition when calling stop/pause on an already stopped Universal Player (by @MarvinSchenkel in #3481)
- Emby Music Provider: fix artist endpoint, image remote accessibility and album artwork (by @hatharry in #3482)
- Fix plex SSL warning polluting the log (by @MarvinSchenkel in #3486)
- Fix filesystem playlists not showing up in the library (by @MarvinSchenkel in #3487)
- Fix not being able to edit Apple Music playlist tracks (by @MarvinSchenkel in #3488)
- Fix tracks from Sonos not being reported as played (by @MarvinSchenkel in #3489)
- Fix dlna not playing on some devices (by @MarvinSchenkel in #3490)

### 🎨 Frontend Changes

- Fix widget rows reloading when toggling the player bar (by @MarvinSchenkel in [#1646](https://github.com/music-assistant/frontend/pull/1646))

### 🧰 Maintenance and dependency bumps

- ⬆️ Update music-assistant-frontend to 2.17.134 (by @music-assistant-machine in #3491)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @hatharry

## 2.8.0-patch.ecf1b23
- Fix workflow for upstream updates, add changelog

## 2.8.0
- Upstream Music Assistant server update to 2.8.0
