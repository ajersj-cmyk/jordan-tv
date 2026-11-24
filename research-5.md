# Jordan TV: Research Round 5 (more Archive sets + PenguPlay and other sites)

Checked Monday, Nov 23, 2026, America/New_York. **Research only:** the import JSON, APK, and repo were not changed. Nothing here has been added.

Current lineup used as the baseline: `jordan-tv-import-full.json` (34 stations, 13,046 videos, 332 unique archive.org identifiers). Almost every video in the app is an Internet Archive file URL, plus 60 YouTube clips.

## Method

- Internet Archive `advancedsearch` (complete-series and title queries, plus a second pass for missed shows and uploaders) and the metadata API. Candidates were checked against the 332 identifiers already in the lineup and against titles already on a channel.
- One original playable file per recommended item (MKV/MP4/AVI/M4V, not IA 480p `.ia.mp4` / `_512kb.mp4` derivatives, and not ISO/VOB/ZIP/RAR) was opened with a Range request. Every recommended file below returned HTTP 206 and was ffprobe'd. Audio is listed as tagged. `untagged` means the rip did not set a language; those are English-language US/UK releases by title, but tracks were not listened to. Dual-audio items are flagged.
- Official episode / theatrical runtimes are the commonly published counts, used only to say whether a set looks complete or a movie looks short.
- Research 2–4 items that were already verified, and that Jordan has not added yet, are not re-pitched as new finds. A short reminder is at the end.

**Copyright note:** Almost all of the movies and series below are still under copyright. These are listings already on archive.org, in the same style as rounds 1–4. Official or clearer-rights options are in the sites section. The only item in this round I would call clearly public domain in the US is the 1941–43 Fleischer Superman shorts. Nothing is added until you pick.

---

## 1) PenguPlay — what it is, and whether Jordan TV can use it

PenguPlay is **not** a streaming site with its own licensed movies, like Tubi or Pluto. It is a free **Stremio / Nuvio addon** at [https://pengu.uk/](https://pengu.uk/). You sign in (Google or an access token), pick “providers,” and the addon hands the player a direct HTTP link.

Its default providers, from public install guides, include sites such as **4KHDHub, MovieBox, MoviesDrives, VAPlayer, 2Peckle, and HDHub4u**, plus optional anime/drama scrapers (Miruro, Anikoto, KissKH, VegaMovies, ToonWorld4All, and others). Those are third-party file hosts / pirate streaming sites, not studio or FAST apps. PenguPlay’s own homepage is mostly a DMCA notice that says it does not host the files and that users are responsible for copyright compliance.

**This is a pirated-content aggregator.** I would not add it to Jordan TV, and I am not going to wire it up. Even aside from the legal issue:

- It needs a personal login and a private addon URL. Links are not stable MP4s you can save in the import JSON.
- Streams break, get rate-limited, or go offline.
- The sources can see the TV’s IP address.
- It does not fit the app’s current model (a saved list of archive.org / YouTube URLs).

If you want a big on-demand catalog on the same TV, the legal path is to install an official free app next to Jordan TV (see below), not to scrape PenguPlay.

---

## 2) Other sites besides Internet Archive

The app already plays **archive.org file URLs** and **YouTube**. There is also an unused Torbox/Trakt path in older notes. Here is an honest look at the services you named, plus the usual legal free options.

### Can be used in Jordan TV today, with caveats

| Source | What it is | Direct playable URL? | Ads / login | Legality | How hard to use in this app |
|---|---|---|---|---|---|
| **Internet Archive** | User-uploaded movies and complete series, plus a real public-domain collection | Yes. Direct `archive.org/download/...` MP4/MKV/AVI links, same as the current lineup | No ads on the file URL | Mix. Public-domain items are the clean ones. Most “complete series” rips are still under copyright, same as the channels you already have | Already works |
| **Official YouTube channels** | Nickelodeon, Cartoon Network, PBS / PBS KIDS, and studio “Movies” channels sometimes post full episodes or movies | Yes, as the app’s existing `youtube` kind — not a raw MP4 | YouTube ads; official videos can be region-locked or unlisted later | Legal when it is the official channel | Easy for a few titles, weak as a channel. Links disappear, get cropped, or switch to a trailer. Check each link at add time |
| **Public-domain features on Archive** | The [feature_films](https://archive.org/details/feature_films) collection, plus official PD YouTube channels | Yes, same Archive file URLs | No | The only movies I would call clearly free to keep. You already have several Christmas PD titles | Easy, but the catalog is old Hollywood / early cartoons, not 90s Nick movies |
| **PeerTube, some Vimeo** | Independent hosts. PeerTube often has a real MP4. Vimeo has a direct-file option only when the uploader turns it on | Sometimes | Varies | Legal only for what the uploader actually has the right to post. There is no large licensed 80s/90s kids catalog here | Possible one-off, not a channel source |

### Legal free apps — good on the TV, poor inside Jordan TV

These are the real “other sites” for full movies. They are licensed and ad-supported. They do **not** expose a stable, login-free MP4 the import JSON can point at. Their terms forbid ripping, bypassing the player, or retransmitting the stream. Playback is usually DRM-protected HLS/DASH with a short-lived token.

| Source | What you actually get | Integrate into Jordan TV? | Better use |
|---|---|---|---|
| **Tubi** | Broadest free on-demand library in the US right now (movies, classic TV, kids, horror). Fox-owned, licensed | No. ToS bars copying, framing, or indexing the catalog, and forbids bypassing the player / DRM | Install the official Android TV app next to Jordan TV |
| **Pluto TV** | Live FAST channels plus a smaller on-demand shelf. Paramount | No. Same player/DRM/ToS pattern. Unofficial playlist scrapers exist; that is against the terms and the URLs expire | Official app, especially for lean-back “channels” |
| **The Roku Channel** | Free movies, shows, live channels, and Roku Originals. Works without Roku hardware on many TVs | No, same reason | Official app |
| **Plex (free Fast/AVOD side)** | Free movies, shows, and live channels. This is separate from Plex Media Server | No official public API for the free *catalog* that would let us drop files into the import. The documented API is for a user’s own server | Official app, or a future project only if you run your own Plex server of files you already have |
| **Prime Video “Free with ads” (old Freevee)** | Amazon’s free-with-ads shelf, mixed in with Prime / rentals | No. Account, DRM, and paid titles sit next to free ones | Watch in the Prime Video app; do not try to pull URLs out |
| **Shout! TV** (Shout! Factory) | Cult, horror, MST3K, ALF, Farscape, retro TV. Official apps and FAST channels on Pluto/Tubi/Roku | No direct files. Legal catalog is a good *watch next door* option for grown-up retro | Official app or those FAST channels |
| **RetroCrush** | Licensed 70s–90s anime, often sub and dub, US and Canada, free with ads (paid tier exists) | No direct files | Official app. Useful if you want legal retro anime the Archive sets don’t cover cleanly |
| **FilmRise** | Licensed free movies and classic TV; also syndicates onto Tubi / Pluto / Roku | No direct files | Official app, or find the same title on Tubi/Pluto |
| **Popcornflix** | Legal free ad-supported movies/TV; it went dark after the Redbox mess and is back at popcornflix.com | No direct files | Official site/app if it still has a TV app when you try it |
| **Kanopy / Hoopla** | Library movies, docs, some kids. Need a participating library card. Stream (Hoopla also has time-limited downloads) | No. Account, DRM, and terms bar copying / screen-recording / bypass | Official apps, only if your library includes them |
| **Xumo Play** | Live FAST channels, similar to Pluto | No | Official app |

**Crackle is gone.** Sony ended the service after the 2024 shutdown. There is nothing to integrate.

### Weak or messy as a Jordan TV source

| Source | Why I would not build a channel on it |
|---|---|
| **Odysee / Rumble** | Some direct files, but the catalogs are user-uploaded. Full current movies there are often unofficial rips. Unstable, and a legality risk |
| **Dailymotion** | A few official partners; ToS restricts downloading other people’s videos. Not a kids-catalog source |
| **Bilibili** | Huge anime/kids library in practice, but geo, login, and a player we cannot legally scrape into ExoPlayer |

**Bottom line:** for this app, Archive (and occasional official YouTube) is still the only source that drops neatly into the import JSON. The legal full-movie services are real, and they are the clean way to watch titles Archive does not have, but they belong as **separate apps on the same Android TV**, not as new Jordan TV stations.

---

## 3) New Internet Archive finds (verified this round)

Counts below are **original playable videos** on the item (not IA derivatives). “Complete” means the file count matches the published episode total, or is off by only a couple.

### A. 80s Saturday-morning cartoons (strongest new series block)

| Title | IA | Files / known total | Typical picture · runtime | Probe (mid or feature) | Notes |
|---|---|---|---|---|---|
| Beetlejuice: The Complete Animated Series (1989–1991) | https://archive.org/details/beetlejuice-1989-complete-animated-series | 94 / 94 | 632×480 · ~22m | HTTP 206, h264 / aac untagged, 22m | Clean SxxExx MP4 names. Best copy of the two I compared |
| Heathcliff and the Catillac Cats (1984–1987) | https://archive.org/details/heathcliff-and-the-catillac-cats-1984-complete-series | 86 / 86 | 631×480 · ~11m | HTTP 206, h264 710×480 / aac(eng), 11m | Complete. 11-minute episodes |
| Inspector Gadget, seasons 1–2 (1983–86) | https://archive.org/details/inspector-gadget-go-go-gadget-series | 86 / 86 | 720×540 · ~22m | HTTP 206, h264 / aac untagged, 22m | This is the complete original series (65 + 21). The uploader tagged it CC0; that is not a real public-domain release — the show is still under copyright |
| The Real Ghostbusters | https://archive.org/details/the-real-ghostbusters | 135 / 140 | 704×480 · ~22m | HTTP 206, h264 / aac untagged, 22m | Nearly complete, five episodes short of the published 140 |
| Filmation’s Ghostbusters (1986) | https://archive.org/details/filmations-ghostbusters-19860 | 65 / 65 | Cinepack AVI · (length not in metadata for the mid file) | Mid file is a Cinepack AVI; ExoPlayer already plays AVI on your box | Complete. Different show from *The Real Ghostbusters* |
| Extreme Ghostbusters (1997) | https://archive.org/details/extreme-ghostbusters-1997-web-dl | 40 / 40 | 640×480 · ~22m | HTTP 206, h264 / aac untagged, 22m | Complete. Prefer this over the 38-episode 360p set at `extreme-ghostbusters-complete-series-1997` |
| Sonic Underground, complete | https://archive.org/details/sonic-underground-the-complete-series_202106 | 40 / 40 | 720×480 · ~22m | HTTP 206, mpeg2 / ac3(eng), 22m | Complete. You already have *Adventures of Sonic the Hedgehog* on Retro Saturday Morning. **Sonic SatAM** only turned up as DVD ISOs (`Sonic-SatAM-Complete-Series`), which the app cannot point at |
| The Transformers (G1, 1984–1987) | https://archive.org/details/s-01-ep-01-more-than-meets-the-eye-part-1 | 98 / 98 | 720×480 · ~23m | HTTP 206, mpeg2 / ac3 untagged, 23m | Complete original series, despite the awkward identifier. A 1080p Season 1-only set also exists (`transformers-season-1`, 16 files) if you ever want a sharper first season |
| The Care Bears, classic 1980s run | https://archive.org/details/TCBClassic19851988 | 71 files | 640×480 · ~23m | HTTP 206, h264 / aac untagged, 23m | Looks complete or very close to the usual 70-episode 1985–88 count |
| Rainbow Brite, complete VHS set | https://archive.org/details/rainbow-brite-complete-vhs-set | 15 files (series is 13 episodes, plus extras) | 320-wide VHS · ~19m | Metadata only for the mid file (MPEG4 320-wide). The 15 original files are `.m4v` | Complete-ish, but soft VHS. The other “complete series” listing (`rainbow-brite-disc-1`) is ISO-only |

**Chip ’n Dale Rescue Rangers:** I did **not** find a playable complete series. Laserdisc volumes and VHS compilations exist, plus a 1280×720 file titled *Rescue Rangers to the Rescue* (https://archive.org/details/chipndale-rescuerangers-themovie, HTTP 206, h264 / aac(eng), **109 minutes**). That runtime does not cleanly match the 1990 compilation (~72m) or the 2022 Disney+ movie (~97m), so I am not treating it as a confirmed title.

### B. Nick / Cartoon Network fills (not already on a channel as a full show)

| Title | IA | Files / known total | Typical picture · runtime | Probe | Notes |
|---|---|---|---|---|---|
| Danny Phantom | https://archive.org/details/danny-phantom-complete-series-480p | 49 / 53 | 640×480 · ~24m | HTTP 206, h264 / aac untagged, 24m | Near-complete. You only have holiday scraps in the lineup today |
| The Angry Beavers | https://archive.org/details/angry-beavers-complete | 126 files / 62 eps (124 segments + extras) | 716×476 · ~12m | HTTP 206, hevc / aac untagged, 12m | Looks complete, including the pilot and a couple of extras. 11–12 minute segments |
| Codename: Kids Next Door, full series | https://archive.org/details/codename-kids-next-door-full-series_202611 | 144 files | 1440×1080 · ~11m | HTTP 206, hevc / eac3(eng), 11m | Strong 1080p set of 11-minute segments + specials. The official run is 78 half-hours plus specials. You only have holiday KND in the lineup now |
| The Grim Adventures of Billy & Mandy, complete | https://archive.org/details/s-01-e-01-meet-the-reaper-evil-con-carne-skeletons-in-the-water-closet | 127 files | 640×480 · ~23m | HTTP 206, h264 / aac(eng), 23m | Awkward identifier; the files are normal `SxxExx` names and include early Evil Con Carne pairings. A 79-file 720p Tubi set is at `s-01-e-01-toadblatts-school-of-sorcery-educating-grim-its-hokey-mon` if you prefer looks over extras |
| Teen Titans (2003), complete | https://archive.org/details/teen-titans-complete | 65 / 65 | 1920×1080 · ~23m | HTTP 206, **hevc** / aac(eng), 23m | Complete, 1080p HEVC (your onn box already handles HEVC). The lineup only has a couple of Titans odds and ends, not this series |
| The Zeta Project, complete, 1080p AI upscale | https://archive.org/details/the-zeta-project-1080p-ai-upscale | 26 / 26 | 1420×1076 · ~21m | HTTP 206, **hevc** / aac untagged, 21m | Complete. It is an AI upscale, so it can look a little painted. Fits the superhero channel next to Batman / Batman Beyond / Static Shock |
| Justice League (2001) | https://archive.org/details/justice-league-complete-season | 46 / 52 | 480×360 · ~22m | Metadata: MPEG4 480×360, 22m. Not ffprobe’d | Partial and soft. Only worth it if you want *some* JL and can live with 360p |

*Johnny Bravo* already has a complete-series identifier in the import, but only 8 episodes are actually in the lineup. A cleaner 185-file set exists at `johnny-bravo-complete` if you ever want to finish that show. I am not counting it as a brand-new find.

### C. Magic School Bus / Bill Nye (PBS-adjacent, not already in the lineup)

| Title | IA | Files / known total | Typical picture · runtime | Probe | Notes |
|---|---|---|---|---|---|
| The Magic School Bus (1994), full series DVD rip | https://archive.org/details/the-magic-school-bus-full-series-dvd-rip | 53 / 52 | 704×480 · ~26m | HTTP 206, **hevc** 704×480 / **two untagged ac3 tracks**, 26m | File count matches the 52-episode series plus one extra. **Do not assume English is first** — there are two untagged audio tracks |
| Bill Nye the Science Guy, complete | https://archive.org/details/billnyethescienceguythecompleteseries-07-28-2021 | 100 / 100 | 416×304 · ~23m | HTTP 206, mpeg4 / mp3 untagged, 23m | Complete, but soft early-2000s AVI. ExoPlayer already plays this kind of file |

### D. Sitcoms (new complete or near-complete sets)

| Title | IA | Files / known total | Typical picture · runtime | Probe | Notes |
|---|---|---|---|---|---|
| Malcolm in the Middle, complete (2000–2006) | https://archive.org/details/malcolm-in-the-middle-complete-series-2000-2006 | 151 / 151 | 1920×1080 · ~22m | HTTP 206, h264 1920×1080 / aac(eng), 22m | Complete, and sharp. The best new sitcom find this round |
| Everybody Loves Raymond | https://archive.org/details/everybody-loves-raymond-tv-series | 208 / 210 | 960×720 · ~22m | HTTP 206, h264 / aac untagged, 22m | Two episodes short of the published 210 |
| The Nanny, complete series | https://archive.org/details/the-nanny-complete-series_20260128 | 144 / 146 | 720×480 · ~23m | HTTP 206, mpeg2 / ac3(eng), 23m | Nearly complete. MPEG-2 inside an MKV; ExoPlayer already plays MPEG-2 |
| That ’70s Show | `that-70s-show-season-1` and `that-70s-show-season-2` | 25 + 26 files | (not probed) | Metadata only | Seasons 1–2 only. I did not find a complete series |

Still not found as a playable complete set: *The Fresh Prince of Bel-Air*, *Full House*. *Home Improvement*, *Saved by the Bell*, and *Sabrina the Teenage Witch* were already verified in earlier rounds and are still unused (see leftovers).

### E. Anime

| Title | IA | Files / known total | Typical picture · runtime | Probe | Notes |
|---|---|---|---|---|---|
| Naruto, complete original series, English dub | https://archive.org/details/naruto-complete-original-series-english-dub | 220 / 220 | 640×480 · ~21m | HTTP 206, h264 / aac(eng), 21m | Complete **original** Naruto, not Shippuden |
| Cowboy Bebop, complete + the movie, 1080p dual audio | https://archive.org/details/cowboy-bebop-yakubo | 27 files (26 eps + the film) | 1448×1080 10-bit HEVC · ~25m | HTTP 206, hevc / **two untagged opus 5.1 tracks**, 25m | Beautiful copy, but **do not assume English is first**. Same class of risk as the old dual-audio movie items |
| Digimon Fusion, complete English series | https://archive.org/details/digimon-fusion-complete-english-series | 54 / 54 | 704×396 · ~20m | HTTP 206, h264 / aac untagged, 20m | Complete English Fusion (the first three Japanese *Xros Wars* seasons). You already have *Digimon Adventure* / *Digital Monsters* on Toonami |
| Sailor Moon, DIC dub, season 1 only | https://archive.org/details/sailor-moon-complete-s01-dic-dub | 40 files | 640×480 · ~22m | Metadata: MPEG4 640×480, 22m | Complete for DIC season 1 only, not the whole series. A listing that claimed the “complete English” series had no playable files |

*Digimon Tamers* still has no playable files (same as research-3). A “DBZ Westwood remaster” exists (`dbz-westwood-remaster`, 170 files) but the filenames start at episode 108 — it is not a start-to-finish English set. *Yu-Gi-Oh! Season 0* is Japanese. I did not find a complete English *Yu-Gi-Oh! Duel Monsters* series. *Avatar: The Last Airbender* is still DVD ISOs only.

### F. Preschool / early-kids (new or large partials)

| Title | IA | Files / known total | Typical picture · runtime | Probe | Notes |
|---|---|---|---|---|---|
| Little Einsteins, “original cut,” large set | https://archive.org/details/little-einsteins-full-series-original-cut | 59 / 67 | 640×480 · 24m | HTTP 206, h264 / aac untagged, 24m | Big, but eight episodes short of the published 67 |
| Thomas & Friends, US, large set | https://archive.org/details/thomas-and-friends-the-complete-series-us | 198 files, through at least Season 16 | 1920×1080 · ~11m | HTTP 206, h264 1920×1080 / aac(eng), 11m | The mid file is S16E17. A very large US-narration set, not a claim that every Thomas episode ever made is here |
| A Bunch of Munsch (1991), complete | https://archive.org/details/A_Bunch_Of_Munsch_Complete_Series | 13 / 13 | 710×480 · ~12m | HTTP 206, h264 / aac untagged, 12m | Complete. Short, sweet preschool |
| The Shoe People (1987), complete | https://archive.org/details/the-shoe-people-the-complete-collection-1987 | 26 / 26 | 720×576 · ~5m | HTTP 206, mpeg2 / ac3(eng), 5m | Complete. The item is marked Attribution-NoDerivs 4.0 on Archive |
| Bingo and Molly (1997), complete | https://archive.org/details/bingo-and-molly-1997--complete-series | 26 files | 854×640 · ~26m | HTTP 206, h264 / aac(eng), 26m | Complete-looking 26-episode preschool set |
| Care Bears: Adventures in Care-a-Lot (2007) + 3 movies | https://archive.org/details/care-bears-adventures-in-care-a-lot | 30 files | 1280-wide · ~22m | Metadata: 1280-wide Matroska, 22m | The later Care Bears series, not the 80s one above |
| Barney & Friends, Season 1 master copy | https://archive.org/details/barney-friends-season-1-master-copy | 24 / 30 | 1440-wide · ~28m | Metadata only | Season 1 only, and short of the usual 30 |
| Handy Manny “full series” | https://archive.org/details/handy-manny-full-series | 26 files / ~100+ eps | 640×480 · 24m | Metadata: MPEG4 640×480, 24m | **Not** a full series. Too thin to build a channel on |
| Fleischer Superman theatrical shorts (1941–1943) | https://archive.org/details/superman-fleischer-brothers-animated-series-1941-1943 | 17 / 17 | 640×480 · ~8m | HTTP 206, h264 / aac untagged, 8m | Complete, and the rare **public-domain** set in this list. Nice extra for the superhero channel |

*Sesame Street Season 25* from the American Archive of Public Broadcasting (`sesame-street-season-25`) has 130 original files, and a mid file that is a 61-minute episode. I did not uniquely count episode numbers, so I am not calling it a clean complete season.

### G. Sports and family movies (new or newly playable)

Runtimes below are the probed file, then the usual theatrical time in parentheses.

| Title | IA | File runtime (theatrical) | Picture | Probe | Notes |
|---|---|---|---|---|---|
| The Mighty Ducks (1992) | https://archive.org/details/the-mighty-ducks-1992-vhs-rip | 108m (104m) | 720×480 VHS | HTTP 206, h264 / aac untagged | Full movie, a few minutes of VHS previews/padding. You already have the *Mighty Ducks* cartoon, not this film. D2 / D3 still not found as playable features |
| Cool Runnings (1993) | https://archive.org/details/cool-runnings_202601 | 98m (98m) | 1904×1024 | HTTP 206, h264 / aac untagged | Clean length, sharp |
| Angels in the Outfield (1994), 1995 VHS | https://archive.org/details/disneys-angels-in-the-outfield-1995-vhs | 109m (102m) | 640×480 | HTTP 206, h264 / aac untagged | Two VHS versions on the item; Version 1 was the one probed. Extra minutes are almost certainly previews |
| Remember the Titans (2000) | https://archive.org/details/remember-the-titans-2000 | 113m (113m) | 1280×544 | HTTP 206, h264 / aac untagged | Clean length |
| Field of Dreams (1989) | https://archive.org/details/field-of-dreams_1989 | 106m (107m) | 1920×1080 | HTTP 206, h264 / aac untagged | Essentially full, 1080p |
| Hoosiers (1986) | https://archive.org/details/hoosiers_202611 | 115m (114m) | 720×544 Cinepack AVI | HTTP 206, mpeg4 / mp3 untagged | Full movie. AVI, which the app already plays |
| The Princess Bride (1987) | https://archive.org/details/the-princess-bride_202306 | 98m (98m) | 1280×720 | HTTP 206, h264 / eac3 6ch untagged | Clean length. A heavier 480p VHS copy is at `1987-the-princess-bride-1998-mgm-vhs-480p-h-264` (101m) |
| The NeverEnding Story (1984) | https://archive.org/details/the.neverending.story.1984.hd | 94m (94m) | 1920×800 HEVC | HTTP 206, hevc / eac3(eng) 6ch | Clean length, 1080p-wide HEVC. There is also a 101-minute “extended German cut” (`the-neverending-story-1984-ext`); I did not trust the English audio on that one without a listen |
| Honey, I Shrunk the Kids (1989) | https://archive.org/details/honey-i-shrunk-the-kids.-disney.-buena-vista.-1990 | 103m (93m) | 640×480 VHS | HTTP 206, h264 / aac untagged | **New.** Research-4 did not find a playable feature. This is a VHS rip with about 10 extra minutes of previews/padding |
| Honey, I Blew Up the Kid (1992) | https://archive.org/details/honey_i_blew_up_the_kid_1992 | 89m (89m) | 676×360 | HTTP 206, h264 / aac untagged | **New.** Research-4 only found RAR/ISO listings. Soft picture, but it is the full movie and it plays |
| George of the Jungle (1997) | https://archive.org/details/george-of-the-jungle-1997 | 92m (92m) | 1920×1024 | HTTP 206, h264 / aac untagged | Clean length. A longer 99-minute 1080p-upscaled VHS is at `disneys-george-of-the-jungle-vhs-1997` if you want the tape feel |
| Thumbelina (1994) | https://archive.org/details/thumbelinafullmovie1994 | 87m (86m) | 640×348 | HTTP 206, h264 / aac untagged | Research-4 left this unverified. It is a complete feature, just a soft picture |
| The Parent Trap (1961) | https://archive.org/details/the-parent-trap-1961_202205 | 129m (129m) | 1280×720 | Metadata: MPEG4 1280×720, 129m. Not ffprobe’d | This is the **Hayley Mills original**, not the 1998 Lindsay Lohan remake (still not found) |

**The Goonies (1985)** at https://archive.org/details/the-goonies-1985_202510 is playable (HTTP 206, h264 1092×800 / aac untagged) but the file is **97 minutes** against a 114-minute theatrical cut. That is too short to recommend without you knowing it may be edited, PAL-cut, or missing a chunk.

*Air Bud* is already in the lineup. *The Sandlot* is already on VHS Kids Movies.

---

## 4) Archive pages / collections worth browsing

These are starting points, not auto-add lists. I verified the URLs exist.

- [feature_films](https://archive.org/details/feature_films) — Internet Archive’s public-domain / freely available feature collection. This is the cleanest “more Archive pages” list for whole movies with clearer rights.
- [classic_tv / classic television search space](https://archive.org/search?query=collection%3Aclassic_tv) — lots of old US TV, much of it also still under copyright, and a lot of it is not kids’ stuff.
- Complete cartoon-series uploaders I kept running into (the uploader *name* did not always search cleanly, but the items are real): the Beetlejuice and Heathcliff complete sets, *A Bunch of Munsch*, *Bingo and Molly*, and *The Shoe People* / Inspector Gadget-style complete cartoon rips. Those pages often “see also” similar complete series.
- American Archive of Public Broadcasting Sesame Street season items, for example [Sesame Street Season 25](https://archive.org/details/sesame-street-season-25). Unique-episode quality would need a careful count before adding.

---

## 5) Recommended next channels (only if you want them)

I would not build all of these. If you pick one or two, a new import can be assembled the same way as Halloween / Muppets / 90s Classics.

1. **80s Saturday Morning** — Inspector Gadget, Beetlejuice TAS, Heathcliff, Real Ghostbusters, Filmation Ghostbusters, Extreme Ghostbusters, Transformers G1, Sonic Underground, classic Care Bears. This is the strongest new-series idea this round. It sits beside your existing Retro Saturday Morning (Sonic *Adventures*, Super Mario Bros Super Show, Captain Planet).
2. **Sports Movie Night** — Mighty Ducks, Cool Runnings, Angels in the Outfield, Remember the Titans, Field of Dreams, Hoosiers, plus *Air Bud* and *The Sandlot* you already have, and *Little Giants* from the research-4 leftover pile if you want the tape-quality one. Still missing a clean *Space Jam*, D2/D3, *The Big Green*, *Like Mike*, and *Little Big League*.
3. **80s/90s Family Movie Night** — Honey, I Shrunk the Kids; Honey, I Blew Up the Kid; George of the Jungle; The Princess Bride; The NeverEnding Story; Thumbelina; optional Parent Trap 1961. This is the research-4 “family comedy” idea, now with several titles that were missing last time.
4. **Classic Sitcoms** — Malcolm in the Middle (the prize), Everybody Loves Raymond, The Nanny, plus the still-unused *Home Improvement*, *Saved by the Bell*, and *Sabrina* from earlier research. Fresh Prince and Full House are still missing.
5. **Nick 2000s / Nicktoons fill** — Danny Phantom, Angry Beavers, and Kids Next Door, either as a new channel or mixed into Nickelodeon 90s. *Pete & Pete* already has 15 episodes in the lineup from the complete-series item; it is a partial, not a new find.
6. **Anime night** — Naruto original (complete English), Digimon Fusion, optional Cowboy Bebop if you are willing to test which audio track is English, plus *Hamtaro* from the research-4 leftover list. Toonami already has Digimon Adventure and Cardcaptors.
7. **Preschool extras** — Little Einsteins (large but not complete), Thomas (US, large), Bunch of Munsch, Shoe People, Bingo and Molly, later Care Bears. Magic School Bus and Bill Nye could live here or on a “PBS extras” block next to PBS KIDS 2000s.
8. **Superhero add-ons** (not necessarily a new channel) — Teen Titans 2003, The Zeta Project, Fleischer Superman (public domain), maybe Filmation Ghostbusters. *Samurai Jack* and *Avatar* are still ISO-only.

---

## 6) Leftovers from research 2–4 (still unused, not new)

Still good, still not re-pitched as new:

- **Nick game shows:** Figure It Out, Double Dare 1986/1988, Super Sloppy Double Dare, Nickelodeon GUTS, Nick Arcade.
- **Sitcoms:** Home Improvement (complete DVD rip, 205 files), Saved by the Bell (the `savedbythebell_202507` set includes *Good Morning, Miss Bliss*), Sabrina the Teenage Witch (163 episodes).
- **Don Bluth / theatrical animation:** FernGully (the English MP4 from research-4 now looks ISO-only on that item; I did not re-verify a playable file this round), Once Upon a Forest, A Troll in Central Park. Thumbelina *is* newly verified above. *The Secret of NIMH*, *Balto*, and one *All Dogs Go to Heaven* listing are still ISO-only; you already have All Dogs VHS tapes on VHS Kids Movies.
- **Anime leftover:** Hamtaro English, 104–105 dubbed episodes (`hamtaro_complete` / `hamtaro-enhanced-720p-episodes-1-104`).
- **Sports leftover:** Little Giants VHS recording; Space Jam theatrical audience VHS (short, rough).
- **Research-3 cartoon leftovers still unused:** Regular Show, She-Ra, Voltron, Over the Garden Wall, Infinity Train, Star vs. the Forces of Evil, Ninjago, Wander Over Yonder, Amphibia (partial), We Bare Bears (partial), and the unused preschool leftovers (Odd Squad, Peg + Cat, Hey Duggee, Nature Cat, Ben & Holly, PJ Masks).

---

## 7) Looked for, but not usable (or not found) this round

- **ISO / VIDEO_TS only (poor fit for the app):** Avatar: The Last Airbender Book 1 collection, Samurai Jack complete series, Sonic SatAM Shout! Factory DVD, Secret of NIMH widescreen, Balto (from earlier rounds), All Dogs Go to Heaven DVD-R, Rainbow Brite disc ISOs, Magic School Bus Korean DVD ISOs.
- **Access-restricted:** a WTTG broadcast of *Mrs. Doubtfire* (`WTTG_20010916_233000_Mrs._Doubtfire`, `access-restricted-item: true`). Do not use it.
- **No playable complete series found:** Chip ’n Dale Rescue Rangers, Rugrats (the main series), CatDog, Rocko’s Modern Life as a *complete* set (you already have some Rocko), Ren & Stimpy (the “S01–S04” item had no original video files), Kenan & Kel, Clarissa (only scraps), He-Man, ThunderCats as a playable complete set, Yu-Gi-Oh! Duel Monsters English, Dragon Ball Z from episode 1 in English, Digimon Tamers, The Fresh Prince of Bel-Air, Full House, Boy Meets World as a complete series (you already have TGIF blocks).
- **Movies still missing a clean playable English feature:** Home Alone, Good Burger, Snow Day, Casper (1995), Who Framed Roger Rabbit, Honey I Shrunk / Blew Up were the *old* gaps — Shrunk and Blew Up are now found. D2 / D3 Mighty Ducks, Like Mike, Little Big League, The Big Green, The Parent Trap (1998), Mrs. Doubtfire (usable copy). *The Goonies* exists but looks short (97m vs 114m).

---

Nothing in this file has been added to the lineup. Say which channels or titles you want, if any, and a new import can be built from the verified items only.
