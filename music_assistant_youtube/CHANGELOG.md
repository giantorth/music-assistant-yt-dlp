## 2.9.4
- Upstream Music Assistant server update to 2.9.4

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.9.3](https://github.com/music-assistant/server/releases/tag/2.9.3)_

### 🐛 Bugfixes

- Validate return_url before appending JWT token (by @s0yd4RK in #4272)
- Fix Spotify playback failing on broken Spotify CDN URLs (by @marcelveldt in #4398)
- Fix unjoining a syncgroup member that joined the leader externally (by @marcelveldt in #4405)
- Recover flow stream restart on Cast groups (players that don't report idle) (by @OzGav in #4406)
- Keep universal player when its protocol links can't migrate to the native player (by @maximmaxim345 in #4413)
- Fix Home Assistant control of universal players running an external source (by @maximmaxim345 in #4415)
- Keep radio/live streams restartable after a mid-stream disconnect (by @marcelveldt in #4421)
- Reconnect ICY radio streams on disconnect (by @marcelveldt in #4422)
- Fix WiiM UPnP event-callback binding on multi-homed / containerized hosts (by @rwlove in #4434)
- fix(snapcast): fix ~65s stop delay caused by spurious inactivity timer (by @vintvinst in #4436)
- Make live audio analysis a passive observer so it can never stall playback (by @chrisuthe in #4442)

### 🧰 Maintenance and dependency bumps

- Bump ytmusicapi from 1.11.5 to 1.12.1 (by @dependabot[bot] in #4235)
- Bump zeroconf from 0.149.12 to 0.149.16 (by @dependabot[bot] in #4408)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@OzGav, @chrisuthe, @marcelveldt, @maximmaxim345, @rwlove, @s0yd4RK, @vintvinst

## 2.9.3
- Upstream Music Assistant server update to 2.9.3

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.9.2](https://github.com/music-assistant/server/releases/tag/2.9.2)_

### 🐛 Bugfixes

- Fix Tidal DASH playback stuttering by serving manifests as HTTP routes (by @libre-7 in #4062)
- Pace audio analysis and cap it to half the CPU cores (by @marcelveldt in #4311)
- Fix protocol player settings not reverting to their default value (by @marcelveldt in #4314)
- Fix WebDAV sync failing on folder names with special characters (by @marcelveldt in #4315)
- Fix podcast episode lookup and a queue preload crash on a drained queue (by @marcelveldt in #4318)
- Preserve percent-encoding when fetching radio/HTTP stream URLs (by @OzGav in #4319)
- Fix podcast episode lookup in gpodder (by @fmunkes in #4323)
- Fix playback of multipart files with apostrophes in path (by @OzGav in #4329)
- Raise open-file soft limit at startup (by @OzGav in #4332)
- Fix Party URL when webserver URL has trailing / (by @OzGav in #4375)
- Fix white noise bug in Jellyfin (by @OzGav in #4378)
- Fix elapsed time drift for live sources played to a sync group (by @marcelveldt in #4385)
- Plex: fix track sync re-scanning the whole library on every page (by @marcelveldt in #4386)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@OzGav, @fmunkes, @libre-7, @marcelveldt

## 2.9.2
- Upstream Music Assistant server update to 2.9.2

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.9.1](https://github.com/music-assistant/server/releases/tag/2.9.1)_

### 🚀 Features and enhancements

- Relax resource requirements for audio analysis providers (by @marcelveldt in #4249)
- Relax 'Maximum' buffer tier to 7GB RAM (by @marcelveldt in #4268)

### 🐛 Bugfixes

- Alexa: Fix restore saved session after aiohttp update (by @Joshi425 in #4181)
- Add correct playlog information when retrieving audiobooks in audiobooks controller (by @fmunkes in #4199)
- Fix Cast Group mDNS for Nest Mini stereo pairs (cast_port/leader rename) (by @goodlucknow in #4224)
- Skip multichannel files in AcoustID scan instead of crashing (by @OzGav in #4230)
- Fix progress report when transitioning from idle or paused (by @fmunkes in #4236)
- Fix image download from CDNs that reject our User-Agent (by @OzGav in #4243)
- Backfill missing album on provider album tracks (by @OzGav in #4244)
- Fix standard crossfade falling back to a hard cut on some tracks (by @marcelveldt in #4253)
- Bound audio-analysis CPU usage and silence NNPACK spam on ARM (by @marcelveldt in #4257)
- Record explicit album/artist/track plays as user-initiated (by @chrisuthe in #4260)
- Release drained audio buffers in the inactivity monitor (by @marcelveldt in #4294)

### 🧰 Maintenance and dependency bumps

<details>
<summary>5 changes</summary>

- Vectorize weighted distance in the sonic similarity provider (by @marcelveldt in #4203)
- Bump aiohttp from 3.14.0 to 3.14.1 (by @dependabot[bot] in #4241)
- Type ytmusic search filter as a Literal (unblock ytmusicapi 1.12.1 mypy) (by @OzGav in #4245)
- Accept Python 3.14 syntax in backports without reformatting stable (by @marcelveldt in #4256)
- Make SQLite page-cache and mmap RAM-aware (by @marcelveldt in #4293)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@Joshi425, @OzGav, @chrisuthe, @fmunkes, @goodlucknow, @marcelveldt

## 2.9.1
- Upstream Music Assistant server update to 2.9.1

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.9.0](https://github.com/music-assistant/server/releases/tag/2.9.0)_

### 🚀 Features and enhancements

- Improve smart crossfade audio quality: true frequency sweep and equal-power curves (by @MarvinSchenkel in #4158)
- Automatically check if CPU is supported for Audio Analysis (by @chrisuthe in #4166)

### 🐛 Bugfixes

- Fix Universal Group Player producing no audio on some members (by @OzGav in #4116)
- fix(alexa): include track metadata in the initial play_media push (by @croll83 in #4168)
- Fix Sendspin grouping with Cast devices (by @maximmaxim345 in #4170)
- Restore 'ignore volume reports' setting for AirPlay players (by @MarvinSchenkel in #4172)
- Fix track duration shrinking when seeking near the end with smart crossfade (by @MarvinSchenkel in #4176)
- Fix invalid scope error when adding a custom Spotify client ID (by @marcelveldt in #4182)
- Remove local providers without wiping the entire library (by @marcelveldt in #4183)
- Fix ISRC lookups failing for Last.fm track MBIDs (by @OzGav in #4185)
- Fix Last.fm Discover rows showing owned tracks under a different version name (by @OzGav in #4186)
- Derive Last.fm genre rows from listening history, not manual tags (by @OzGav in #4187)
- Fix now-playing artwork showing a solid background for transparent logos (by @OzGav in #4188)
- Fix sync group member playing out of sync after concurrent group changes (by @marcelveldt in #4189)
- Drop per-track MusicBrainz ISRC lookups from Last.fm recommendations (by @OzGav in #4190)
- Skip stale artist paths during filesystem track parsing (by @chrisuthe in #4191)
- Fix high idle memory usage (by @marcelveldt in #4198)

### 🧰 Maintenance and dependency bumps

- Reduce idle memory usage by tuning jemalloc (by @marcelveldt in #4213)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @chrisuthe, @croll83, @marcelveldt, @maximmaxim345

## 2.9.0
- Upstream Music Assistant server update to 2.9.0

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.9](https://github.com/music-assistant/server/releases/tag/2.8.9)_

### 🚀 Features and enhancements

- Separate library artist views from per-provider artist listings (by @marcelveldt in #4039)
- Add Settings to allow Control of default similar_track action (by @chrisuthe in #4053)
- Add album_type filter to smart playlist rules (by @dmoo500 in #4059)
- Cache recommendations() for sonic_similarity and audiobookshelf (by @MarvinSchenkel in #4099)
- Speed up YouTube Music recommendations loading (by @MarvinSchenkel in #4120)
- Spread metadata maintenance schedule across the day (by @MarvinSchenkel in #4126)
- Add get_artist_toptracks to lastfm recommendations provider (by @OzGav in #4141)
- Enable WiiM and Last.fm Recommendations by default (by @MarvinSchenkel in #4142)
- Smart playlists: optional AI-generated descriptions (by @MarvinSchenkel in #4144)
- Lastfm improvements (by @OzGav in #4148)
- Improve playlog for artists and albums (by @chrisuthe in #4149)
- ACoustID Switch to shared API key by default (by @OzGav in #4154)
- Default artist fix (by @chrisuthe in #4163)
- Add unofficial-integration disclaimer to streaming provider settings (by @marcelveldt in #4164)

### 🐛 Bugfixes

- Plex Connect: refactor and fixes plugin (by @anatosun in #3510)
- Make universal player merge deterministic when link counts tie (by @sdhomecode in #4017)
- Fix AcoustID scan coverage stalling (by @OzGav in #4070)
- Fix smart playlist dedup for streaming (non-library) tracks (by @MarvinSchenkel in #4082)
- Fix genre icons disappearing after install path changes (by @MarvinSchenkel in #4083)
- Fix YouTube Music search() signature (by @OzGav in #4085)
- Fix WiiM volume_set by using HTTP command instead of UPnP (by @MarvinSchenkel in #4086)
- Reconcile smart playlist library entries on load to recover after DB reset (by @dmoo500 in #4088)
- Apple Music: stream library tracks and harden transient-error handling (by @teancom in #4089)
- Fix YTMusic provider not retrying when PO Token server is slow to start (by @CodeCommander in #4093)
- Fix radio station logos rendering as black or failing to load (by @OzGav in #4094)
- Phishin Change fallback album image URL (by @OzGav in #4097)
- AirPlay: fix mDNS cross-match when device name is substring of another device name (by @MarvinSchenkel in #4098)
- Fix None handling in music controller track/resume lookups (by @OzGav in #4102)
- Avoid event loop block in YouTube Music recommendations and skip SoundCloud default avatar (by @MarvinSchenkel in #4104)
- Only advertise extended ICY headers on flow stream when ICY metadata is requested (by @mcaulifn in #4105)
- Fix Apple Music library-only album artwork by caching blobstore URLs (by @dmoo500 in #4106)
- Added None guard (by @anatosun in #4107)
- Fix library-only tracks/albums showing as unavailable in shared playlists (by @dmoo500 in #4108)
- Fix transfer_queue losing position when source queue is paused/idle (by @OzGav in #4115)
- AirPlay: Ignore mDNS address updates that replace a routable IP with a Docker bridge address (by @MarvinSchenkel in #4117)
- Re-add configurable output buffer for AirPlay 1 (RAOP) players (by @MarvinSchenkel in #4118)
- Fix version parsing for titles with nested parentheses (by @OzGav in #4119)
- Audio analysis: re-scan stale-version tracks in background scan (by @chrisuthe in #4123)
- Don't enqueue next track onto a stopped queue (by @MarvinSchenkel in #4127)
- Bump `aiosendspin` to 6.0.2 to fix spec conformance issues (by @maximmaxim345 in #4128)
- Fix volume jump when crossfade intro and body normalize differently (by @MarvinSchenkel in #4129)
- Send Sendspin album artwork for radio and Spotify Connect streams (by @maximmaxim345 in #4130)
- Adjust Chromecast playback defaults (HTTP Profile 3 + flow mode) (by @MarvinSchenkel in #4133)
- Fix misleading smart-crossfade FFmpeg failure log message (by @MarvinSchenkel in #4139)
- Separate Phish.in artist tracks from top tracks (by @OzGav in #4140)
- Fix disappearing Sendspin Visualizer clients (by @maximmaxim345 in #4143)
- Align MusicBrainz throttler with mirror rate limit (by @MarvinSchenkel in #4146)
- Fix Sendspin not playing when grouping ESPHome devices (by @maximmaxim345 in #4147)
- end of queue results in track being reported as played twice (by @chrisuthe in #4150)
- Fix sendspin unmute (by @OzGav in #4151)
- Cap concurrent MusicBrainz ISRC lookups in Last.fm recommendations (by @OzGav in #4155)
- Fix cache cleanup missing most records and skip needless startup vacuum (by @MarvinSchenkel in #4156)
- Last.fm provider search bug fixes (by @OzGav in #4159)
- Fix 30s delay when grouping some Sendspin devices (by @maximmaxim345 in #4160)
- Prevent out-of-memory crash when compacting the library database (by @MarvinSchenkel in #4161)

### 🎨 Frontend Changes

- Show Smart Playlist provider in playlists provider filter (by @dmoo500 in [#1848](https://github.com/music-assistant/frontend/pull/1848))
- Fanart for top picks (by @stvncode in [#1854](https://github.com/music-assistant/frontend/pull/1854))
- Fix play button centering + banner behind tile (by @stvncode in [#1852](https://github.com/music-assistant/frontend/pull/1852))
- Prune stale provider ids from stored listing filters (by @OzGav in [#1727](https://github.com/music-assistant/frontend/pull/1727))
- Derive library membership from in_library flag (by @OzGav in [#1810](https://github.com/music-assistant/frontend/pull/1810))
- fix(theme): fix dark-mode rendering (by @teancom in [#1811](https://github.com/music-assistant/frontend/pull/1811))
- Show catalog providers in library provider filter (by @OzGav in [#1851](https://github.com/music-assistant/frontend/pull/1851))
- Fix album/playlist track order when played directly from a list (by @OzGav in [#1850](https://github.com/music-assistant/frontend/pull/1850))
- Lower smart playlist dedup_hours max to 2160h (90 days) (by @MarvinSchenkel in [#1861](https://github.com/music-assistant/frontend/pull/1861))
- Always show lights and visualisers in the group list (by @OzGav in [#1860](https://github.com/music-assistant/frontend/pull/1860))
- Add link to background analysis Concurrency Setting (by @chrisuthe in [#1830](https://github.com/music-assistant/frontend/pull/1830))
- Add back provider icon in discover pge + fix fanart (by @stvncode in [#1859](https://github.com/music-assistant/frontend/pull/1859))
- Add back provider icon in discover pge + fix fanart (by @stvncode in [#1859](https://github.com/music-assistant/frontend/pull/1859))
- Fix genre display in smart playlist rule picker (by @dmoo500 in [#1864](https://github.com/music-assistant/frontend/pull/1864))
- Put play button to the right for consistency (by @stvncode in [#1868](https://github.com/music-assistant/frontend/pull/1868))
- Hide/Show top picks and replace v-btn by shadcn one (by @stvncode in [#1867](https://github.com/music-assistant/frontend/pull/1867))
- Add album type filter to smart playlist rules (by @dmoo500 in [#1847](https://github.com/music-assistant/frontend/pull/1847))
- Fix server spam for fresh recommandation with debounce (by @stvncode in [#1869](https://github.com/music-assistant/frontend/pull/1869))
- Fix erroneous underline on Audio Analysis concurrency link (by @chrisuthe in [#1872](https://github.com/music-assistant/frontend/pull/1872))
- Only refetch recommendations on track end, not periodic progress (by @stvncode in [#1870](https://github.com/music-assistant/frontend/pull/1870))
- Lokalise: Translations update (by @marcelveldt in [#1875](https://github.com/music-assistant/frontend/pull/1875))
- Fix queue items disappearing in fullscreen player (by @MarvinSchenkel in [#1874](https://github.com/music-assistant/frontend/pull/1874))
- Single artist detail view with provider filter (by @marcelveldt in [#1829](https://github.com/music-assistant/frontend/pull/1829))
- Fix: Update overflow menu on shortcuts change and album tracks on navigation (by @dmoo500 in [#1892](https://github.com/music-assistant/frontend/pull/1892))
- Add refresh top picks + Fix two shorcut bugs (by @stvncode in [#1901](https://github.com/music-assistant/frontend/pull/1901))
- Store some settings per user (by @OzGav in [#1335](https://github.com/music-assistant/frontend/pull/1335))
- Lokalise: Translations update (by @marcelveldt in [#1904](https://github.com/music-assistant/frontend/pull/1904))

### 🧰 Maintenance and dependency bumps

<details>
<summary>37 changes</summary>

- Bump stages on 2.9 release (by @OzGav in #3942)
- Treat Retry-After as a floor for rate limits, not an exact target (by @rnewman in #4067)
- Some Typing fixes for Apple Music (by @OzGav in #4073)
- Final Typing fixes for Bluesound provider (by @OzGav in #4074)
- Add PGH003 mypy rule (by @OzGav in #4075)
- ⬆️ Update music-assistant-models to 1.1.129 (by @music-assistant-machine in #4076)
- ⬆️ Update music-assistant-frontend to 2.17.175 (by @music-assistant-machine in #4077)
- Further typing fixes for Apple Music (by @OzGav in #4078)
- Bump aiohttp from 3.13.5 to 3.14.0 (by @dependabot[bot] in #4079)
- Remove ignore from Bluesound player.py (by @OzGav in #4080)
- Type throttle_with_retries via Protocol instead of Provider bound (by @OzGav in #4081)
- Final typing fixes for Apple Music (by @OzGav in #4084)
- Some typing fixes for the YouTube Music provider (by @OzGav in #4087)
- Final typing fixes for YouTube Music (by @OzGav in #4090)
- Type-check plex and plex_connect providers, treat plexapi as untyped (by @OzGav in #4091)
- Typing fixes for the music controller - stage 1 (by @OzGav in #4092)
- ⬆️ Update music-assistant-frontend to 2.17.176 (by @music-assistant-machine in #4096)
- ⬆️ Update music-assistant-frontend to 2.17.177 (by @music-assistant-machine in #4100)
- Typing fixes for the music controller stage 2 (by @OzGav in #4101)
- Enable ruff UP043 and drop unnecessary default type arguments (by @OzGav in #4103)
- ⬆️ Update music-assistant-frontend to 2.17.178 (by @music-assistant-machine in #4111)
- ⬆️ Update music-assistant-frontend to 2.17.179 (by @music-assistant-machine in #4113)
- Final typing fixes for the Music controller (by @OzGav in #4114)
- Add translation_key to builtin playlists (by @OzGav in #4122)
- ⬆️ Update music-assistant-frontend to 2.17.180 (by @music-assistant-machine in #4125)
- Pin Sendspin Cast app id to the frozen `ma-2.9` channel (by @maximmaxim345 in #4131)
- ⬆️ Update music-assistant-frontend to 2.17.181 (by @music-assistant-machine in #4132)
- Bump pyblu from 2.0.7 to 2.0.8 (by @dependabot[bot] in #4134)
- Bump lyricsgenius from 3.11.0 to 3.12.2 (by @dependabot[bot] in #4136)
- ⬆️ Update music-assistant-frontend to 2.17.182 (by @music-assistant-machine in #4137)
- Add more translation keys (by @OzGav in #4138)
- ⬆️ Update music-assistant-frontend to 2.17.183 (by @music-assistant-machine in #4145)
- Use the standalone hue-entertainment library in the Hue Lights Sync plugin (by @marcelveldt in #4152)
- Fix guard_single_request type-var bound so media controllers don't need ignores (by @OzGav in #4153)
- ⬆️ Update music-assistant-frontend to 2.17.184 (by @music-assistant-machine in #4157)
- ⬆️ Update music-assistant-frontend to 2.17.185 (by @music-assistant-machine in #4162)
- ⬆️ Update music-assistant-frontend to 2.17.186 (by @music-assistant-machine in #4165)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@CodeCommander, @MarvinSchenkel, @OzGav, @anatosun, @chrisuthe, @dmoo500, @marcelveldt, @maximmaxim345, @mcaulifn, @rnewman, @sdhomecode, @stvncode, @teancom

## 2.8.9
- Upstream Music Assistant server update to 2.8.9

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.8](https://github.com/music-assistant/server/releases/tag/2.8.8)_

### 🐛 Bugfixes

- Resolve universal_player wrappers in UGP stream handler (by @OzGav in #3952)
- Skip DSP-triggered playback restart when DSP was and remains disabled (by @MarvinSchenkel in #3988)
- Fix Deezer playback stalling on tracks with insufficient rights (error 2002) (by @MarvinSchenkel in #4048)
- Phishin fixes and optimisations (by @OzGav in #4066)
- Fix Bluesound ungroup crashing on non-existent pyblu client attributes (by @OzGav in #4072)

### 🧰 Maintenance and dependency bumps

- Revert "Resolve universal_player wrappers in UGP stream handler" (by @OzGav in #3956)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav

## 2.8.8
- Upstream Music Assistant server update to 2.8.8

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.7](https://github.com/music-assistant/server/releases/tag/2.8.7)_

### 🚀 Features and enhancements

- Support German radio station metadata (by @OzGav in #3881)

### 🐛 Bugfixes

- Fix protocol recovery with missing cached parent (by @prydie in #3829)
- Fix output bit depth ignoring supported sample-rate/bit-depth pairs in player settings (by @OzGav in #3842)
- Fix imageproxy URL encoding for paths containing only spaces (by @OzGav in #3863)
- Tolerate non-UTF-8 metadata in DLNA SOAP/NOTIFY responses (by @OzGav in #3864)
- Disable zone handling for a disabled player in MusicCast (by @fmunkes in #3872)
- Fix media progress retrieval for open sessions in Audiobookshelf (by @fmunkes in #3879)
- Fix Airplay not stopping stream on some devices. (by @MarvinSchenkel in #3903)
- Squeezelite: Honor per-player output_codec in multi-client sync URL (by @MarvinSchenkel in #3924)
- Sonos S1: Implement select_source for line-in support (by @MarvinSchenkel in #3925)
- Streams: Handle empty supported_sample_rates in get_output_format (by @MarvinSchenkel in #3926)
- Fix HEOS showing incorrect Now Playing (by @Tommatheussen in #3928)
- Close coroutines when submitted in rapid succession (by @MarvinSchenkel in #3929)
- Fix HEOS queue cleanup slowing down other commands (by @Tommatheussen in #3932)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @Tommatheussen, @fmunkes, @prydie

## 2.8.7
- Upstream Music Assistant server update to 2.8.7

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.6](https://github.com/music-assistant/server/releases/tag/2.8.6)_

### 🚀 Features and enhancements

- Emby Music Provider: add audio format to stream details (by @hatharry in #3796)

### 🐛 Bugfixes

- Workaround for "Youtube Music playlist stalls on uploaded music" music-assistant/support#4469 (by @whitty in #3156)
- Fix volume of Sendspin bridge players defaulting to 100% (by @maximmaxim345 in #3782)
- Suppress `StreamStoppedError` when skipping tracks with Sendspin (by @maximmaxim345 in #3783)
- Fix YTMusic stream format selection (by @greenmansuperhero in #3784)
- Update MASS_LOGO_ONLINE URL to raw GitHub link (by @h4de5 in #3797)
- Fix library sync deletion for non-streaming providers (by @OzGav in #3806)
- bbc_sounds: use LiveStation.id for station identifier (by @MacTheFork in #3807)
- YTMusic: Add auto mixes to recommendations. (by @MarvinSchenkel in #3816)
- Airplay: Add debounce to prevent-playback=1 commands (by @MarvinSchenkel in #3817)
- Fix Spotify playlists failing when track count is a multiple of 50 (by @gitviola in #3818)
- Snapcast: Adopt orphaned snapserver streams on name collision instead of misreporting as no-free-port (by @PeterPalenik in #3830)
- Fix output bit depth ignoring supported sample-rate/bit-depth pairs in player settings (by @OzGav in #3842)

### 🧰 Maintenance and dependency bumps

- Use /playlists/{id}/items endpoint (Spotify Feb 2026 API change) (by @Yipsh in #3436)
- Spotify: Update get_artist_albums limit, log error messages, guard methods (by @delatt in #3762)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MacTheFork, @MarvinSchenkel, @OzGav, @PeterPalenik, @Yipsh, @delatt, @gitviola, @greenmansuperhero, @h4de5, @hatharry, @maximmaxim345, @whitty

## 2.8.6
- Upstream Music Assistant server update to 2.8.6

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.5](https://github.com/music-assistant/server/releases/tag/2.8.5)_

### 🐛 Bugfixes

- Fix ffmpeg process leak in smart fades mixer on aborted playback (by @marcelveldt in #3725)
- Harden AirPlay STOP command delivery and add teardown logging (by @marcelveldt in #3729)
- Prevent concurrent flow-stream producers from corrupting the playlog (by @marcelveldt in #3731)
- Guard Sonos volume attribute update against uninitialized state (by @marcelveldt in #3732)
- Fix ORF Radiothek browse reverting to top level (by @OzGav in #3733)
- Preserve multi-value album type across all tag parsers (by @OzGav in #3743)
- [Soundcloud]: improving search (by @fionn-r in #3745)
- Fix enqueue action 'replace' stopping the music (by @MarvinSchenkel in #3753)
- Qobuz: fix credential leak on 401 and populate date_added (by @OzGav in #3754)
- Implement power control function for squeezelite (by @MarvinSchenkel in #3755)
- Fix manual genres disappearing after a cleanup run (by @MarvinSchenkel in #3757)
- Force imageproxy over streamserver for Airplay artwork (by @MarvinSchenkel in #3763)
- Fix tidal recommendations (by @jozefKruszynski in #3767)
- Change heartbeat of websocket and sendspin proxy socket to 25s (by @MarvinSchenkel in #3769)
- Fix 30s delay after switching tracks on Sendspin (by @maximmaxim345 in #3777)

### 🧰 Maintenance and dependency bumps

- Bump auntie-sounds to 1.1.8 (by @kieranhogg in #3723)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@MarvinSchenkel, @OzGav, @fionn-r, @jozefKruszynski, @kieranhogg, @marcelveldt, @maximmaxim345

## 2.8.5
- Upstream Music Assistant server update to 2.8.5

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.4](https://github.com/music-assistant/server/releases/tag/2.8.4)_

### 🚀 Features and enhancements

- Apple Music: Add Unicode NFC normalization for artist/album/track names (by @jasonhollis in #2631)
- Apple Music: Add content rating check for explicit tracks (by @LosCV29 in #3514)
- Apple Music: Add content rating check for explicit tracks (by @LosCV29 in #3669)

### 🐛 Bugfixes

- Fix AirPlay DACP volume control for Sonos speakers (by @marcelveldt in #3654)
- Fix queue items showing zero/unknown duration (by @marcelveldt in #3668)
- Tweak imageproxy (by @MarvinSchenkel in #3671)
- Several fixes for synced playback stability (by @marcelveldt in #3672)
- Filter stale podcast episodes (by @OzGav in #3673)
- Sendspin: guard against negative track_progress in metadata (by @marcelveldt in #3681)
- Fix sync group session lifecycle and AirPlay late joiner sync (by @marcelveldt in #3682)
- Automatically clean up loudness measurements on media item deletion (by @MarvinSchenkel in #3687)
- Fix multiple (virtual) devices on the same host being merged. (by @MarvinSchenkel in #3688)
- Fix sync group dissolve+reform race with async providers (by @marcelveldt in #3691)
- Fix Jellyfin multidisc albums with same named tracks (by @MarvinSchenkel in #3692)
- Fix Volume control for Bluesound native devices (by @MarvinSchenkel in #3693)
- Fix race condition in AirPlay stream session client removal (by @marcelveldt in #3698)
- Improve loudness measurement robustness (by @marcelveldt in #3703)
- Fix smart fades mixer sometimes choking up the flow stream + Smart Fades provider not starting on ARM (by @MarvinSchenkel in #3706)
- Bump aiohttp to 3.13.5 and ibroadcastaio to 0.6.0 (by @staticdev in #3707)
- Fix syncgroup state derivation and tighten lifecycle handling (by @marcelveldt in #3709)
- Fix duration parsing for M3U playlist items (by @marcelveldt in #3714)
- Fix AirPlay cleanup idling re-added clients (by @marcelveldt in #3716)
- Fix sync leader child state forwarding (by @marcelveldt in #3717)
- Forward syncgroup join/unjoin to the syncgroup player (by @marcelveldt in #3718)
- Fix audiobook controller not using userid in library_items call (by @fmunkes in #3719)

### 🧰 Maintenance and dependency bumps

<details>
<summary>4 changes</summary>

- [Backport to stable] 2.8.2 (by @marcelveldt in #3564)
- Add diagnostics for AirPlay stream stalls and increase flow buffer (by @marcelveldt in #3696)
- Remove temporary airplay diagnostics (by @marcelveldt in #3720)
- Fix power control for squeezelite (by @marcelveldt in #3721)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@LosCV29, @MarvinSchenkel, @OzGav, @fmunkes, @jasonhollis, @marcelveldt, @staticdev

## 2.8.4
- Upstream Music Assistant server update to 2.8.4

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.3](https://github.com/music-assistant/server/releases/tag/2.8.3)_

### Other Changes

- [Backport to stable] 2.8.4 (by @github-actions[bot] in #3634)


## 2.8.3
- Upstream Music Assistant server update to 2.8.3

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.2](https://github.com/music-assistant/server/releases/tag/2.8.2)_

### 🐛 Bugfixes

- Rewrite tidal stream behaviour to avoid premature cutoff (by @jozefKruszynski in #3369)
- YT Music: Fix syncing 'Episodes for later' in podcast library sync (by @teancom in #3582)
- Fix flow stream playlog pre-count and use 50/50 crossfade split (by @marcelveldt in #3587)
- Fix sync group player desynchronization and add dynamic leader switching (by @marcelveldt in #3591)
- Revert "Rewrite tidal stream behaviour to avoid premature cutoff (#3369)" (by @jozefKruszynski in #3593)
- Fix sync group regressions: proper locking and dynamic leader switch (by @marcelveldt in #3594)
- Include missing description in automatic artist metadata scan (by @OzGav in #3595)
- Add protocol awareness and transition guards to sync group player (by @marcelveldt in #3600)
- Fix party duplicate prevention race (by @marcelveldt in #3601)
- Subsonic: Fix structured lyrics yet again (by @khers in #3604)
- Fix player/queue deadlock on multiple simultane (play) actions (by @marcelveldt in #3624)
- Fix AirPlay late joiner out-of-sync when joining a sync group (by @marcelveldt in #3625)
- Fix flow mode queue tracking drift on AirPlay dynamic leader switch (by @marcelveldt in #3628)

### 🧰 Maintenance and dependency bumps

- Consolidate smart fades analyzer thread calls to fix asyncio slow-task warning (by @marcelveldt in #3588)

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@OzGav, @jozefKruszynski, @khers, @marcelveldt, @teancom

## 2.8.2
- Upstream Music Assistant server update to 2.8.2

### Upstream Release Notes
## 📦 Stable Release

_Changes since [2.8.1](https://github.com/music-assistant/server/releases/tag/2.8.1)_

### 🚀 New Providers

- Add Coverart Archive metadata provider (by @OzGav in #3523)

### 🚀 Features and enhancements

- Allow use of a personal client id for Spotify (by @marcelveldt in #1536)
- Try parsing track number from the filename (by @marcelveldt in #1663)
- A few small bugfixes and enhancements to playback and enqueuing  (by @marcelveldt in #1670)
- Fix IPv6 support across core and providers (by @fmurodov in #3235)
- Support playback of radio station PLS playlist URLs with query parameters (by @OzGav in #3419)
- Open Subsonic Lyric support (by @khers in #3424)
- Add optional timestamp to get_resume_position (by @fmunkes in #3505)
- Add Socks proxy option for Pandora (by @TermeHansen in #3513)
- Dynamic playlist queue support for is_dynamic playlists (by @dmoo500 in #3527)
- Fix group volume balance drift with interpolation-based scaling (by @marcelveldt in #3548)
- Add config for show progress bar in party mode (by @Awashcard0 in #3549)
- Add Canada in UI for Alexa provider (by @EricLabranche in #3568)
- Add duplicate track prevention and empty default for party name/QR text (by @apophisnow in #3576)

### 🐛 Bugfixes

- Apple Music: Various fixes (by @MarvinSchenkel in #1652)
- Fix cast/dlna player stops playing after 1 or 2 tracks of a playlist (by @marcelveldt in #1658)
- Bluesound: fixed deprecated enqueue next issue, announcements removed (by @Cyanogenbot in #1659)
- Create new session so Pandora fetches fresh tracks (by @OzGav in #3493)
- Fix podcasts from filesystem source not appearing in library (by @teancom in #3494)
- Fix Bandcamp provider not having pagination (by @teancom in #3496)
- Fix output format reporting for protocol and sendspin players (by @marcelveldt in #3498)
- Fix player controls configuration (by @marcelveldt in #3503)
- Improve audio buffering in streams controller (by @marcelveldt in #3507)
- Improve Qobuz API rate limiting, backoff, and sync efficiency (by @teancom in #3515)
- Fix jellyfin get_artist_albums always returning empty list (by @TastyPi in #3521)
- Several small bugfixes and stability enhancements related to streaming (by @marcelveldt in #3522)
- Fix Sonos not unmuting when playing via Airplay (by @MarvinSchenkel in #3529)
- Bump aioslimproto to 3.1.8. (by @MarvinSchenkel in #3530)
- Subsonic: Include bookmark creation date if available (by @khers in #3531)
- Fix player controls for non-native players (by @marcelveldt in #3532)
- Fix: select_source should ungroup a player if its grouped/synced (by @marcelveldt in #3534)
- Guard against non-UTF-8 filenames in file system providers (by @OzGav in #3539)
- Fix syncgroup ungroup command silently ignored due to stale state (by @marcelveldt in #3540)
- Fix AirPlay mDNS discovery race between RAOP and AirPlay services (by @marcelveldt in #3546)
- Fix AirPlay Sendspin bridge audio sync and re-enable AirPlay2 (by @marcelveldt in #3547)
- Fix filesystem provider sync config checkboxes not being respected (by @teancom in #3550)
- Fix plugin source volume feedback loop with group players (by @marcelveldt in #3556)
- Fix player queue stuck on play_action_in_progress (by @marcelveldt in #3557)
- Subsonic: Bump py-opensonic for lyrics fix (by @khers in #3559)
- A few fixes for audio streaming (by @marcelveldt in #3560)
- Plex: fix streaming of newly added Plex tracks (by @anatosun in #3561)
- Fix Universal Group Player playback issues (by @marcelveldt in #3562)
- Fix high CPU usage during audio streaming on low-power devices (by @marcelveldt in #3567)
- Fix external source reporting on Universal Players (by @marcelveldt in #3571)
- Fix sync group player features not available when idle (by @marcelveldt in #3572)
- Fix scheduled sync task settings not persisting across restarts (by @marcelveldt in #3574)
- Fix plugin source players stuck in PLAYING state after disconnect (by @marcelveldt in #3579)
- Fix AirPlay late-join timing and remove oversized pipe buffers (by @marcelveldt in #3581)
- Fix AirPlay late-join sync: start_at must match first byte stream position (by @marcelveldt in #3583)
- Restore flow stream buffering for smart fades headroom (by @marcelveldt in #3584)
- Fix flow stream UI showing next track too early during crossfade (by @marcelveldt in #3586)

### 🎨 Frontend Changes

- Accept frameless query param without requiring a value (by @apophisnow in [#1650](https://github.com/music-assistant/frontend/pull/1650))
- Fix Party dashboard QR color and track sizing (by @apophisnow in [#1649](https://github.com/music-assistant/frontend/pull/1649))
- Add import playlist feature (by @chrisuthe in [#1662](https://github.com/music-assistant/frontend/pull/1662))
- Add progress bar for current track in party mode (by @Awashcard0 in [#1664](https://github.com/music-assistant/frontend/pull/1664))
- Disable shuffle and repeat buttons for dynamic playlists (by @dmoo500 in [#1667](https://github.com/music-assistant/frontend/pull/1667))
- Add favorite button to player bar (by @dmoo500 in [#1666](https://github.com/music-assistant/frontend/pull/1666))
- Player menu enhancements (by @radiohe4d in [#1536](https://github.com/music-assistant/frontend/pull/1536))
- Add translation strings for player options (by @fmunkes in [#1663](https://github.com/music-assistant/frontend/pull/1663))
- Add track action menu to player bar (by @dmoo500 in [#1669](https://github.com/music-assistant/frontend/pull/1669))
- Party duplicate prevention (by @apophisnow in [#1670](https://github.com/music-assistant/frontend/pull/1670))
- Party duplicate prevention (by @apophisnow in [#1670](https://github.com/music-assistant/frontend/pull/1670))

### Other Changes

- Fix: Handle radio stations providing non utf-8 in streamtitle (by @marcelveldt in #1664)
- Adding missing icon for the Soundcloud music provider (by @robsonke in #1665)
- Fix loading state from cache when connecting to slimproto players (by @kepstin in #1666)

### 🧰 Maintenance and dependency bumps

<details>
<summary>34 changes</summary>

- Split up build workflow to use intermediate base image (by @marcelveldt in #1647)
- Bump zeroconf from 0.133.0 to 0.134.0 (by @dependabot[bot] in #1656)
- Bump ruff from 0.6.4 to 0.6.5 (by @dependabot[bot] in #1667)
- Bump pyblu from 0.4.0 to 1.0.2 (by @dependabot[bot] in #1669)
- Bump lyricsgenius from 3.7.5 to 3.11.0 (by @dependabot[bot] in #3405)
- Bump ruff from 0.14.13 to 0.15.6 (by @dependabot[bot] in #3406)
- Add support for dynamic playlists to the Queue controller (by @dmoo500 in #3432)
- AirPlay improvements for pre-4K devices and interface resolution in Docker (by @dmoo500 in #3434)
- Rename music provider to source (by @OzGav in #3480)
- Add pkce to spotify_connect (by @SuperSandro2000 in #3485)
- ⬆️ Update music-assistant-frontend to 2.17.135 (by @music-assistant-machine in #3500)
- Bump cryptography from 46.0.5 to 46.0.6 (by @dependabot[bot] in #3501)
- ⬆️ Update music-assistant-models to 1.1.109 (by @music-assistant-machine in #3502)
- ⬆️ Update music-assistant-frontend to 2.17.136 (by @music-assistant-machine in #3504)
- ⬆️ Update music-assistant-frontend to 2.17.137 (by @music-assistant-machine in #3517)
- ⬆️ Update music-assistant-models to 1.1.110 (by @music-assistant-machine in #3519)
- Add PTH119 and PTH116 mypy rules (by @OzGav in #3526)
- Remaintain jellyfin (by @staticdev in #3528)
- Bump aiohttp from 3.13.3 to 3.13.4 (by @dependabot[bot] in #3533)
- fix(alexa): Fix issue with language on alexa skills for french and english canada (by @EricLabranche in #3535)
- ⬆️ Update music-assistant-frontend to 2.17.139 (by @music-assistant-machine in #3536)
- Standardise icons for remote filesystem providers (by @OzGav in #3537)
- Replace blind asyncio.sleep calls with event-based state waiting (by @marcelveldt in #3541)
- Fix cache controller to enforce consistent JSON serialization (by @marcelveldt in #3542)
- Stream smart fades FFmpeg output instead of buffering (by @marcelveldt in #3543)
- Bump hass client to 1.2.3. (by @MarvinSchenkel in #3544)
- Bump docker/login-action from 4.0.0 to 4.1.0 (by @dependabot[bot] in #3545)
- Copy queue items list before mutation in delete_item for consistency (by @teancom in #3551)
- Bandcamp: fix Liskov substitution violation in get_artist signature (by @teancom in #3552)
- ⬆️ Update music-assistant-frontend to 2.17.140 (by @music-assistant-machine in #3553)
- Clean up leaked throttlers, command locks, and protocol evaluations on player unregister (by @teancom in #3554)
- Add MusicCast player options translation keys (by @fmunkes in #3558)
- ⬆️ Update music-assistant-frontend to 2.17.141 (by @music-assistant-machine in #3565)
- ⬆️ Update music-assistant-frontend to 2.17.142 (by @music-assistant-machine in #3578)

</details>

## :bow: Thanks to our contributors

Special thanks to the following contributors who helped with this release:

@Awashcard0, @Cyanogenbot, @EricLabranche, @MarvinSchenkel, @OzGav, @SuperSandro2000, @TastyPi, @TermeHansen, @anatosun, @apophisnow, @chrisuthe, @dmoo500, @fmunkes, @fmurodov, @kepstin, @khers, @marcelveldt, @radiohe4d, @robsonke, @staticdev, @teancom

## 2.8.1-patch.f02c3bf
- Better playback, format selection, retry logic

## 2.8.1-patch.47be7c5
- Upstream pipeline fix

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
