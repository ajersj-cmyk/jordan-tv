# Jordan TV: Research Round 2 (more kids' and 90s shows)

Checked 2026-11-13 20:12 ET. Research only: no JSON, app or repo changes.

## Method
- I collected candidates from about 250 IA advancedsearch queries (r2/search.json). Each candidate was checked against `jordan-tv-import-full.json`, both by identifier and by show-name keyword in episode titles, and against `research.md`.
- **Episode counts:** distinct episode groups of 4 minutes or more, using original files (r2/final.json).
- **Resolution and format:** the most common original-file height and format.
- **ffprobe:** run on one mid-list file per item, which is the file the builder would choose.
- **URL check:** every sample URL returned HTTP 206 to a byte-range GET. None of the picks is access-restricted.
- **Audio:** every pick is an original English-language US, Canadian or UK production with no dub markers. Where an item had a language tag it was `eng`. Many rips leave the audio untagged (`und`/blank), and those are the original English track. Space Cases has English as track 1 and Russian as track 2.
- **Codecs:** HEVC MKV, AVI XviD, MPEG-2 and MOV all play in the app's ExoPlayer path, and the onn box decodes HEVC in hardware.

## Ranked picks (50)

| # | Channel idea | Show | Eps / known total | Format · typical res · GB | ffprobe sample (video / audio) | IA item(s) | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Nick Game Shows | Nickelodeon GUTS (S1-3 + Global GUTS) | 159 / ~150 | MP4 · 1080p · 101.3 | h264 1440x1080 / aac(eng) | https://archive.org/details/nickelodeon-guts-season-1<br>https://archive.org/details/nickelodeon-guts-season-2<br>https://archive.org/details/nickelodeon-guts-season-3<br>https://archive.org/details/nickelodeon-global-guts-season-4 | 1080p upscales, MP4 straight to the player |
| 2 | Nick Live-Action | Clarissa Explains It All | 65 / 65 | MKV/MP4 · 480p · 12.7 | h264 640x480 / aac(untagged) | https://archive.org/details/clarissa-explains-it-all_202611 | Hulu WEB rips, complete |
| 3 | Nick Live-Action | The Secret World of Alex Mack | 78 / 78 | M4V · 480p · 16.2 | h264 640x480 / aac(und) | https://archive.org/details/secret-world-of-alex-mack |  |
| 4 | Nick Game Shows | Legends of the Hidden Temple | 120 / 120 | AVI · 384p · 29.3 | mpeg4 512x384 / mp3(untagged) | https://archive.org/details/legends.-of.-the.-hidden.-temple.-s | AVI XviD 384p; the player handles AVI |
| 5 | Nick Game Shows | Double Dare (1986) + Double Dare (1988) | 187 / 195 | MP4 · 480p · 26.1 | h264 640x480 / aac(und) | https://archive.org/details/doubledare-1986_202010<br>https://archive.org/details/double-dare-1988_202011 |  |
| 6 | Nick Live-Action | The Amanda Show | 40 / 40 | MP4 · 540p · 9.1 | h264 720x540 / aac(und) | https://archive.org/details/the-amanda-show |  |
| 7 | Nick Live-Action | Hey Dude | 66 / 65 | MKV · 480p · 19.7 | h264 708x480 / aac(untagged) | https://archive.org/details/hey-dude_202211 |  |
| 8 | Nick Live-Action | Salute Your Shorts | 26 / 26 | MP4 · 480p · 4.0 | h264 640x480 / aac(und) | https://archive.org/details/salute-your-shorts-complete |  |
| 9 | Nick Live-Action | Animorphs | 26 / 26 | MP4 · 480p · 4.6 | h264 640x480 / aac(und) | https://archive.org/details/animorphs-season-1-and-2-the-complete-series |  |
| 10 | Nick Live-Action | Space Cases | 26 / 27 | MKV · 540p · 7.2 | hevc 720x540 / aac(eng), aac(rus) | https://archive.org/details/space-cases-1996-complete-series-vhs | VHS source; English is the 1st audio track, Russian 2nd |
| 11 | Nick Live-Action | Unfabulous | 40 / 41 | MKV/MP4 · 480p · 13.4 | h264 632x472 / aac(eng) | https://archive.org/details/Unfabulous2004 | mixed MKV/MP4/AVI |
| 12 | Nickelodeon 90s | KaBlam! | 48 / 48 | MOV · 375p · 16.3 | h264 640x480 / aac(und) | https://archive.org/details/KaBlam_201709 | MOV originals, about 375p |
| 13 | TGIF / TNBC | Saved by the Bell (+ Good Morning Miss Bliss + College Years) | 119 / 118 (13+86+19) | AVI · 544p · 24.1 | mpeg4 720x544 / mp3(untagged) | https://archive.org/details/savedbythebell_202507 | AVI XviD up to 544p |
| 14 | TGIF / TNBC | Saved by the Bell: The New Class | 142 / 143 | MP4 · 384p · 19.5 | h264 512x384 / aac(eng) | https://archive.org/details/saved-by-the-bell-the-new-class-s-01-e-02_202508 |  |
| 15 | TGIF / TNBC | Home Improvement | 205 / 204 | MKV · 476p · 43.6 | h264 700x476 / aac(eng) | https://archive.org/details/home-improvement-complete-dvd-rip | DVD rip |
| 16 | TGIF / TNBC | The Wonder Years | 115 / 115 | MP4 · 472p · 20.6 | h264 704x472 / aac(eng) | https://archive.org/details/the-wonder-years-complete-series |  |
| 17 | TGIF / TNBC | Brotherly Love | 40 / 40 | MP4 · 480p · 21.4 | h264 640x480 / ac3(eng) | https://archive.org/details/brotherly-love-Lando18 |  |
| 18 | TGIF / TNBC | Sweet Valley High S1-3 | 66 / 88 (S4 missing) | MP4 · 720p · 15.2 | h264 1280x720 / aac(und) | https://archive.org/details/sweet-valley-high-1994-tv-series-season-one<br>https://archive.org/details/sweet-valley-high-1994-tv-series-season-two<br>https://archive.org/details/sweet-valley-high-1994-tv-series-third-season | 720p |
| 19 | Fox Kids / Power Rangers | Power Rangers Zeo | 50 / 50 | MKV · 480p · 7.5 | hevc 640x480 / eac3(eng) | https://archive.org/details/power-rangers-zeo | HEVC MKV |
| 20 | Fox Kids / Power Rangers | Power Rangers in Space | 43 / 43 | MKV · 480p · 12.6 | hevc 720x480 / ac3(eng) | https://archive.org/details/power-rangers-in-space_202209 | HEVC MKV |
| 21 | Fox Kids / Power Rangers | Power Rangers Lost Galaxy | 45 / 45 | MKV · 480p · 20.7 | hevc 720x480 / ac3(eng) | https://archive.org/details/power-rangers-lost-galaxy | HEVC MKV |
| 22 | Fox Kids / Power Rangers | Power Rangers Lightspeed Rescue | 40 / 40 | MKV · 480p · 15.1 | hevc 720x480 / ac3(eng) | https://archive.org/details/power-rangers-lightspeed-rescue | HEVC MKV |
| 23 | Fox Kids / Power Rangers | Power Rangers Time Force | 40 / 40 | MKV · 480p · 8.6 | hevc 720x480 / ac3(eng) | https://archive.org/details/power-rangers-time-force_20220928 | HEVC MKV |
| 24 | Saturday Morning | Sonic the Hedgehog (SatAM) | 26 / 26 | MP4 · 480p · 10.1 | h264 960x720 / aac(und) | https://archive.org/details/Sonic-the-Hedgehog-SatAM-The-Complete-Series-Restored | restored, half 720p |
| 25 | Saturday Morning | Garfield and Friends | 362 / 121 eps (362 segments) | MKV · 480p · 103.4 | hevc 720x480 / ac3(en) | https://archive.org/details/garfield-and-friends-complete-series | HEVC MKV, split into segments |
| 26 | Saturday Morning | Captain Planet and the Planeteers | 113 / 113 | MKV · 480p · 35.6 | h264 640x480 / aac(eng) | https://archive.org/details/captain-planet-and-the-planeteers-480p |  |
| 27 | Saturday Morning | Biker Mice from Mars (1993) | 65 / 65 | MKV · 480p · 10.9 | hevc 704x480 / aac(eng) | https://archive.org/details/biker-mice-from-mars_202507 | HEVC MKV |
| 28 | Saturday Morning | Exosquad | 52 / 52 | MP4 · 480p · 8.7 | h264 640x480 / aac(und) | https://archive.org/details/exosquad-s-02-e-06-mind-set |  |
| 29 | Saturday Morning | Sonic Underground | 40 / 40 | MKV · 480p · 37.1 | mpeg2video 720x480 / ac3(eng) | https://archive.org/details/sonic-underground-the-complete-series_202106 | MPEG-2 DVD remux (big files) |
| 30 | Cartoon Network 90s | SWAT Kats | 26 / 25 | AVI/MP4 · 480p · 4.3 | mpeg4 640x480 / mp3(untagged) | https://archive.org/details/swat-kats-moonsong | AVI XviD |
| 31 | Cartoon Network 90s | Camp Lazlo | 115 / 61 + shorts | MKV/MP4 · 1080p · 34.9 | hevc 1920x1080 / eac3(eng) | https://archive.org/details/camp-lazlo-s-03-e-01-hello-summer-goodbye-camp-301 | 1080p HEVC/MP4 |
| 32 | Cartoon Network 90s | Megas XLR | 26 / 26 | MP4 · 480p · 7.5 | h264 640x480 / aac(eng) | https://archive.org/details/megas-xlr-complete-series |  |
| 33 | PBS KIDS Classic | Bill Nye the Science Guy | 100 / 100 | AVI · 384p · 24.0 | mpeg4 416x304 / mp3(untagged) | https://archive.org/details/billnyethescienceguythecompleteseries-07-28-2021 | AVI XviD, 300-384p |
| 34 | PBS KIDS Classic | Reading Rainbow | 155 / 155 | MKV · 480p · 35.1 | h264 640x480 / eac3(eng) | https://archive.org/details/ReadingRainbowTVSeries | MKV H.264 480p |
| 35 | PBS KIDS Classic | Ghostwriter | 74 / 73 | AVI · 480p · 13.5 | mpeg4 640x480 / mp3(untagged) | https://archive.org/details/ghostwriter_1992 | AVI |
| 36 | PBS KIDS Classic | Where in the World Is Carmen Sandiego? S1-5 | 284 / 295 | MP4 · 360p · 26.4 | h264 480x360 / aac(eng) | https://archive.org/details/65_20231114<br>https://archive.org/details/39_20231114_202311<br>https://archive.org/details/59_20231114<br>https://archive.org/details/17_20231114_202311<br>https://archive.org/details/07_20231114_202311 | mostly 360p |
| 37 | PBS KIDS Classic | Mathnet | 30 / 30 | MP4 · 480p · 9.3 | h264 640x480 / aac(und) | https://archive.org/details/Mathnet-TV-series-complete |  |
| 38 | PBS KIDS Classic | Kratts' Creatures | 50 / 50 | MP4 · 480p · 8.4 | h264 640x480 / aac(und) | https://archive.org/details/kratts-creatures-complete-series | not Wild Kratts, which he already has |
| 39 | Preschool (Nick Jr / Playhouse / PBS) | Teletubbies | 365 / 365 | MKV · 480p · 60.4 | hevc 640x480 / aac(eng) | https://archive.org/details/teletubbies_202012 | HEVC MKV |
| 40 | Preschool (Nick Jr / Playhouse / PBS) | Jay Jay the Jet Plane | 63 / 62 | MP4 · 1080p · 14.7 | h264 1920x1080 / aac(und) | https://archive.org/details/JJTJPJJMTVSeries | 1080p |
| 41 | Preschool (Nick Jr / Playhouse / PBS) | Kipper | 78 / 78 | MP4 · 576p · 13.2 | h264 1024x576 / aac(und) | https://archive.org/details/kipper-the-dog-complete-series | 576p |
| 42 | Preschool (Nick Jr / Playhouse / PBS) | Little Bear | 65 / 65 | MP4 · 480p · 18.7 | h264 640x480 / aac(und) | https://archive.org/details/maurice-sendaks-little-bear |  |
| 43 | Preschool (Nick Jr / Playhouse / PBS) | Rolie Polie Olie | 78 / 78 | MP4 · 480p · 10.3 | h264 640x480 / aac(eng) | https://archive.org/details/RPOTVSeries |  |
| 44 | Preschool (Nick Jr / Playhouse / PBS) | Gullah Gullah Island | 70 / 70 | MP4 · 480p · 22.7 | h264 710x480 / aac(und) | https://archive.org/details/gullah-gullah-island-seasons1-4 |  |
| 45 | Preschool (Nick Jr / Playhouse / PBS) | Oswald | 26 / 26 | MP4 · 720p · 2.6 | h264 960x720 / aac(und) | https://archive.org/details/s-01-e-11_20250626 | 720p |
| 46 | Preschool (Nick Jr / Playhouse / PBS) | Maisy | 26 / 26 | MP4 · 1074p · 8.4 | h264 1434x1072 / aac(eng) | https://archive.org/details/maisy-full-series_202403 | 1080p |
| 47 | Preschool (Nick Jr / Playhouse / PBS) | Caillou | 116 / ~120 | MP4 · 576p · 33.2 | h264 720x480 / eac3(eng) | https://archive.org/details/CTVSeriesAMZN19972010 |  |
| 48 | Preschool (Nick Jr / Playhouse / PBS) | Wonder Pets! | 63 / 62 | MP4/MOV · 480p · 21.0 | h264 640x480 / eac3(eng) | https://archive.org/details/wonder-pets-original |  |
| 49 | Preschool (Nick Jr / Playhouse / PBS) | Sid the Science Kid | 68 / 66 | MKV/MP4 · 720p · 122.4 | h264 1280x720 / eac3(eng) | https://archive.org/details/STSKTVSeries | 720p |
| 50 | Preschool (Nick Jr / Playhouse / PBS) | WordWorld | 45 / 44 | MKV · 1080p · 50.3 | h264 1920x1080 / eac3(eng) | https://archive.org/details/WWTVSeries20072011 | 1080p |

## Bench (10, usable but weaker: low resolution, partial, or awkward file layout)

| # | Channel idea | Show | Eps / known total | Format · res · GB | ffprobe | IA item(s) | Notes |
|---|---|---|---|---|---|---|---|
| 51 | TGIF / TNBC | Growing Pains | 164 / 166 | MP4 · 360p · 9.1 | h264 480x360 / aac(eng) | https://archive.org/details/growing-pains-complete-series | only 360p |
| 52 | TGIF / TNBC | Smart Guy | 52 / 51 | MP4 · 360p · 3.7 | h264 480x360 / aac(und) | https://archive.org/details/SmartGuySeason3Episode18Crushed | only 360p |
| 53 | TGIF / TNBC | Hang Time S1, S3, S4 | 63 / 104 (S2, S5, S6 missing) | MKV · 480p · 11.4 | h264 640x480 / aac(untagged) | https://archive.org/details/hang-time-1995-season-one<br>https://archive.org/details/hang-time-1995-season-three<br>https://archive.org/details/hang-time-s-04-1995-season-four |  |
| 54 | Fox Kids / Power Rangers | VR Troopers | 90 / 92 | MP4 · 360p · 8.9 | h264 640x480 / aac(und) | https://archive.org/details/vr-troopers_202508 | mostly 360p |
| 55 | Saturday Morning | Street Sharks | 41 / 40 | MP4 · 360p · 3.7 | h264 480x360 / aac(und) | https://archive.org/details/StreetSharksSharkWarsSeason3Episode13FullEpisode | only 360p |
| 56 | Cartoon Network 90s | Chowder | 49 / 49 | AVI/MKV · 480p · 10.2 | mpeg4 640x480 / ac3(untagged) | https://archive.org/details/chowder-the-complete-series_202606 | AVI/MKV |
| 57 | PBS KIDS Classic | Postcards from Buster | 55 / 55 | MKV · 480p · 29.0 | h264 640x480 / aac(und) | https://archive.org/details/PFBTVSeries2004 |  |
| 58 | Preschool (Nick Jr / Playhouse / PBS) | The Big Comfy Couch | 100 / 105 | MP4 · 360p · 11.6 | h264 480x360 / aac(und) | https://archive.org/details/the-big-comfy-couch | 360p |
| 59 | Preschool (Nick Jr / Playhouse / PBS) | Shining Time Station (home-video cuts) | 104 / 65 (has alternate cuts) | MP4 · 1080p · 79.6 | h264 1440x1080 / aac(und) | https://archive.org/details/shining-time-station-TV-series-CompleteHighQuality | 1080p60 upscale |
| 60 | Preschool (Nick Jr / Playhouse / PBS) | Busy World of Richard Scarry | 154 / 65 eps (154 segment files) | MP4/M4V · 480p · 28.6 | h264 720x480 / aac(eng) | https://archive.org/details/RichardScarrysBusyTown | files named 1.mp4 etc.; per-file mode needed |

## Rejected or skipped
- **Already in the lineup or in research.md:**
  - Goosebumps
  - Mighty Morphin Power Rangers S1–3
  - DuckTales (its IA item is also restricted, 401)
  - Darkwing Duck, TaleSpin, Pepper Ann, Proud Family and Fillmore!
  - Life with Louie, Dragon Tales, Clifford, Fetch! and Between the Lions
  - Bear in the Big Blue House, Billy & Mandy and Allegra's Window
  - SpongeBob and Fairly OddParents. research.md says the first 100 of each are already in his lineup. A 520-episode SpongeBob set exists (spongebob-squarepants_20250716) and a 173-episode FOP set (0x-08-scouts-honor) if he wants them complete.
- **No complete English set on IA:**
  - Boy Meets World, Full House, Family Matters, Fresh Prince and Step by Step
  - Sabrina, Sister Sister (S1 only) and Kenan & Kel (only a Spanish dub found)
  - Eerie, Indiana (5 of 19), Finders Keepers (9 of 65) and Bug Juice (no files)
  - The Weekenders S1 (8), Blue's Room (5) and Higglytown Heroes (7, 172p)
- **Too partial to make the main list:**
  - Mister Rogers (305 of 895, 480p): mister-rogers-neighborhood-complete-50th-anniversary-tv-series
  - Bob the Builder US (122 of 255, 720p): bob-the-builder-complete-classic-us-dub
  - Mighty Max (S1 only, 13 of 40, 1080p)
  - Lower-priority extras: Little Einsteins (59 of 67), Little Bill (48 of 52), Seven Little Monsters (40 of 52), George Shrinks (40 of 40), Corduroy (13 of 13, 720p), Timothy Goes to School (26 of 26, VP9/Opus), Hi-5 USA (70, 1080p), Thomas & Friends S1–17 (408, but only 276–352p), The Wiggles S2 (26), California Dreams S1–2 (31 of 78), Fraggle Rock animated (13).
- **Skipped for content:** Ren & Stimpy (not kid-appropriate, and partial).
- **Noise filtered out:** non-English dubs (Latino, Hindi, PT-BR, Cantonese, Greek, Norsk), DVD ISOs, VHS broadcast tapes and single-episode uploads.

## Build notes for later
- Garfield and Friends comes as 362 segment files, not 121 episodes. Fine for a shuffle channel.
- Busy World of Richard Scarry files are named `Disk N/1.mp4`. pick_videos groups them badly (30), so it needs a per-file mode.
- Saved by the Bell bundles Good Morning Miss Bliss (13) and The College Years (19), which can be filtered by folder.
- Sonic Underground is a full-bitrate MPEG-2 remux (about 0.9 GB per episode), which is heavy over Wi-Fi.
- GUTS S1 has 47 files against 40 aired episodes, because it includes extras/specials.
