# Jordan TV: Internet Archive research (millennial kids/family)

_Research only. Nothing has been added to the import JSON. Compiled Fri Nov 13, 2026 (ET)._

## Method
- Searched with IA advancedsearch (title queries, sorted by downloads) for more than 200 show and holiday queries. Candidates were then checked with the metadata API (file counts by format, original vs. derivative files, access restrictions).
- ffprobe was run on a mid-list sample episode per item. It was run on the original file and, for MKV/AVI items, on IA's auto-made `.mp4` derivative too.
- Excluded every identifier already in his JSON (49 identifiers). Show-level overlaps are noted, e.g. Static Shock S1, Recess, Lizzie, Phil, American Dragon, Arthur S8 and Timon & Pumbaa.
- Every item URL below returned 200 on `/details/<id>`, and a sample episode file returned 200/206 on `/download/` (98/98 checked).

## Key playback findings (relevant to the 360p complaint)
- **IA's auto-generated MP4 for MKV/AVI uploads is always ~480p or lower at ~800 kbps.** Examples: 640x480, 854x480, and Legend of Tarzan's 1080p MKV gets a 640x360 MP4. Feeding the app `.mp4` derivatives of HD MKVs caps quality at SD. For full resolution, point the app at the **original MKV** (his app already plays MKV, e.g. Gargoyles, X-Men, Pokemon) or pick items whose originals are MP4.
- Many HD originals are **HEVC (some 10-bit)**: Spider-Man TAS, Jackie Chan, Courage 1080p, Batman TAS Blu-ray, X-Men Evolution and Lizzie. The onn 4K box has HEVC hardware decode, but test one before bulk-adding.
- Avoid the "Multilanguage WEB-DL" items for Wizards of Waverly Place (`wizards-of-waverly-place-2007`) and Suite Life on Deck (`the-suite-life-on-deck`). Their **first audio track is Chinese** (English is track 6), so the app or the IA MP4 would likely play the wrong language.
- `DisneysTheLegendOfTarzan720pHDTV`: the Tarzan files have Russian as audio track 1.
- Some audio is EAC3/MP2 (As Told by Ginger, Weekenders, Clifford). Check that the player handles it, or use the IA MP4 (AAC).

## Excluded / not found
- `ChristmasSpecials` and `christmas-specials-2` are UK adult comedy/variety specials, so they're excluded. `christmas-episodes-and-specials` mixes in adult sitcoms (21 Jump Street, 30 Rock), so it was skipped.
- `ed-edd-n-eddy-full-series-1999-2009` is access-restricted. The alternate is listed below.
- No complete sets on IA were found for: Rugrats, Hey Arnold (20 eps only), Rocko (S1-2 only), CatDog, Angry Beavers, Wild Thornberrys, Aaahh!!! Real Monsters, Danny Phantom, Rocket Power, Nick's Doug, Samurai Jack, Goof Troop, Chip 'n Dale Rescue Rangers (laserdisc only), Hannah Montana, Suite Life. Paramount/Nick titles seem to get removed.
- Already in his lineup (skipped): Clifford, Dragon Tales, Bear in the Big Blue House, Pepper Ann, Buzz Lightyear, Quack Pack, Darkwing, TaleSpin, DuckTales, Gargoyles, Fairly OddParents, SpongeBob First 100, Kim Possible, Even Stevens, Proud Family (53 ≈ complete).

## Candidates (ranked within each channel idea)


### Cartoon Network (new)

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Codename: Kids Next Door | https://archive.org/details/s-5-e-14-operation-z.-e.-r.-o | 80 files / 78 eps + Operation Z.E.R.O. | Complete | Direct MP4, 720p | MP4: h264 960x720 971kbps | Best CN pick. 960x720. |
| 2 | Cow and Chicken | https://archive.org/details/s-01-e-04-confused-the-molting-fairy-i.-r.-gentlemans | 52 / 52 | Complete | Direct MP4, 720p | MP4: h264 960x720 2042kbps | Tubi 720p rip. |
| 3 | Grim Adventures of Billy & Mandy | https://archive.org/details/s-01e-15-son-of-nergal | 77 / 78 | Complete (1 short) | Direct MP4, 720p | MP4: h264 960x720 1440kbps | Specials are in a separate item (see Christmas). |
| 4 | Johnny Bravo | https://archive.org/details/s-01-e-01-super-duped-bungled-in-the-jungle-bearly-enough-time | 68 / 67 | Complete | Direct MP4, 480p | MP4: h264 640x480 1722kbps | High bitrate 480p (1.7 Mbps). |
| 5 | Dexter's Laboratory | https://archive.org/details/dexters-laboratory-the-complete-series | 81 / 78 | Complete + extras | Direct MP4, 480p | MP4: h264 640x480 546kbps | An alternate 720p HEVC MKV set exists: dexters-laboratory_202507 (77 MKV). |
| 6 | The Powerpuff Girls (1998) | https://archive.org/details/powerpuff-girls-complete-series | 110 MP4 / 78 eps | Complete + movie/extras | Direct MP4, 480p | MP4: h264 718x480 558kbps; orig: h264 720x480 620kbps; IA MP4: h264 640x480 775kbps | the-powerpuff-girls-1998-the-complete-series has the same files. |
| 7 | Courage the Cowardly Dog | https://archive.org/details/courage-the-cowardly-dog-s-01-e-03_202602 | 53 / 52 | Complete | Direct MP4, 480p | MP4: h264 632x480 804kbps | HD option: courage-the-cowardly-dog-1080p-ai-upscale (66 HEVC MKV, 1446x1080). Spooky but TV-Y7. |
| 8 | Ed, Edd n Eddy | https://archive.org/details/ed-edd-n-eddys-big-picture-show_202509 | 70 / 69 eps + 4 specials + movie | Near-complete | Direct MP4, 576p | MP4: h264 768x576 1233kbps | The main ed-edd-n-eddy-full-series-1999-2009 item is access-restricted, so it's excluded. |
| 9 | Foster's Home for Imaginary Friends | https://archive.org/details/fosters-home-for-imaginary-friends-the-complete-series_202507 | 91 / 79 + movie + shorts | Complete | Direct MP4, 480p | MP4: h264 640x480 401kbps | Low bitrate (~400 kbps). |
| 10 | Teen Titans (2003) | https://archive.org/details/teen-titans-complete-series_202607_202607 | 78 MKV / 65 + Trouble in Tokyo | Complete | MKV (+480p IA MP4) | orig: h264 656x480 849kbps; IA MP4: h264 656x480 787kbps | Also fits the superhero channel. |

### Kids' WB (new)

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Static Shock | https://archive.org/details/static-shock-cartoon | 52 / 52 | Complete | Direct MP4, 1080p | MP4: h264 1440x1080 2018kbps | Fills out his Static Shock S1 (he has 13 eps in 02_20250625_...). |
| 2 | Batman Beyond | https://archive.org/details/dc-batman-beyond-1999-season-one_202309 | 52 eps + 4 crossovers | Complete | Direct MP4 (.ia.mp4), 1440x1080 ~2 Mbps | MP4: h264 1920x1080 2410kbps | Originals were removed and only the IA .ia.mp4 files are left. They play fine. |
| 3 | Jackie Chan Adventures | https://archive.org/details/jackie-chan-adventures-1080p-ai-upscale | 95 / 95 | Complete | MKV HEVC 1080p (+480p IA MP4) | orig: hevc 1440x1080 7550kbps; IA MP4: h264 640x480 788kbps | AI upscale. |
| 4 | Xiaolin Showdown | https://archive.org/details/XiaolinShowdown | 52 / 52 | Complete | Direct MP4, 480p widescreen | MP4: h264 852x480 1303kbps |  |
| 5 | Pinky and the Brain | https://archive.org/details/s-01-e-05-brainania_202608 | 65 / 65 | Complete | Direct MP4, 480p | MP4: h264 652x480 1271kbps |  |
| 6 | Histeria! | https://archive.org/details/histeria-1998-2000-the-complete-series | 52 / 52 | Complete | Direct MP4, 480p | MP4: h264 716x480 1243kbps |  |
| 7 | Freakazoid! | https://archive.org/details/freakazoid_202210 | 24 / 24 | Complete | Direct MP4, 384p | MP4: h264 512x384 924kbps |  |
| 8 | Animaniacs | https://archive.org/details/animaniacs-1993-1998-movie_202601 | 100 / 99 + Wakko's Wish | Complete | Direct MP4, 360p (low, 250 kbps) | MP4: h264 480x360 252kbps | Low quality, but the set is complete. |
| 9 | Tiny Toon Adventures | https://archive.org/details/tiny-toon-adventures-1990-1995_202512 | 101 / 98 + specials | Complete | Direct MP4, 360p (low) | MP4: h264 480x360 328kbps |  |
| 10 | Batman: The Animated Series (Blu-ray) | https://archive.org/details/batman-the-animated-series-1992-season-1-4-blu-ray-1080p-hevc-10bit-aac-2.0-rcvr | 101 / 85 + New Adventures | Complete | MKV only, HEVC 10-bit 1080p, NO MP4 derivative | orig: hevc 1436x1080 3058kbps | Test it on the onn box first. HEVC 10-bit needs hardware decode. |

### Fox Kids (new)

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Spider-Man: The Animated Series | https://archive.org/details/spider-mantheanimatedseries | 65 / 65 | Complete | MKV HEVC 1440x1080 (+480p IA MP4) | orig: hevc 1440x1080 3237kbps; IA MP4: h264 640x480 793kbps | Also fits the X-Men/superhero channel. |
| 2 | Big Bad Beetleborgs | https://archive.org/details/sabans-big-bad-beetleborgs | 88 / 88 | Complete | MKV 480p (+IA MP4) | orig: h264 720x480 1998kbps; IA MP4: h264 640x480 799kbps |  |
| 3 | Mighty Morphin Power Rangers S1 | https://archive.org/details/mighty-morphin-power-rangers-season-1 | 61 / 60 | Complete | MKV HEVC 480p (+IA MP4) | orig: hevc 720x480 1903kbps; IA MP4: h264 640x480 803kbps | S2: mighty-morphin-power-rangers-season-2 (55/52). S3: mighty-morphin-power-rangers-season-3 (36/33). All complete. |
| 4 | Goosebumps (1995) | https://archive.org/details/GTVSeries1995 | 68 / 74 | Near-complete (92%) | MKV 576p (+480p IA MP4) | orig: h264 714x576 1042kbps; IA MP4: h264 634x480 785kbps | Kid-scary, TV-Y7. |
| 5 | Bobby's World | https://archive.org/details/bobbysworlds1ep11insearchoftheringbear480x640_201911 | 81 / 81 | Complete | Direct MP4, 480p | MP4: h264 640x480 623kbps |  |
| 6 | Life with Louie | https://archive.org/details/life-with-louie | 39 / 39 | Complete | AVI (+480p IA MP4) | orig: mpeg4 640x480 1417kbps; IA MP4: h264 640x480 775kbps |  |
| 7 | Eek! The Cat | https://archive.org/details/eekthecats01e01misereekextendedcut | 64 / 65 | Near-complete | MKV + AVI (+480p IA MP4) | orig: h264 720x576 1565kbps; IA MP4: h264 600x480 833kbps |  |
| 8 | Digimon: Digital Monsters (Adventure + 02) | https://archive.org/details/digimon-digital-monsters-the-complete-collection-saban-entertainment-edited-version | 104 / 104 | Complete | MKV 568p (+480p IA MP4) | orig: h264 710x568 1994kbps; IA MP4: h264 638x480 795kbps | Saban English dub. Could also go on the Pokemon channel. |

### One Saturday Morning / ABC fill

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Recess | https://archive.org/details/recessfullseries | 131 AVI (65 eps as segments + movies) | Complete | AVI (+480p IA MP4) | orig: mpeg4 640x480 1238kbps; IA MP4: h264 640x480 801kbps | He has only 8 Recess eps now. |
| 2 | Teacher's Pet | https://archive.org/details/teachers-pet-complete-tv-series | 39 / 39 | Complete | Direct MP4, 720p | MP4: h264 1280x720 1355kbps |  |
| 3 | The Emperor's New School | https://archive.org/details/emporers-new-school-complete-series_202601 | 52 / 52 | Complete | Direct MP4, 720p | MP4: h264 1280x720 784kbps | Also fits Disney Channel. |
| 4 | The Weekenders | https://archive.org/details/w33k3nde4s | 73 segments / 78 (39 eps) | Near-complete | Direct MP4, 480p (MP2 audio) | MP4: h264 720x480 794kbps | MP2 audio may not play on every player. The IA MP4 is AAC. |
| 5 | Lloyd in Space | https://archive.org/details/thepiratebay-6590308 | 39 / 39 | Complete | MKV 360p (+IA MP4) | orig: h264 640x360 475kbps; IA MP4: h264 640x360 832kbps |  |
| 6 | Fillmore! | https://archive.org/details/fillmore-1x-08-ingrid-third-public-enemy-1-pdtv | 26 / 26 | Complete | AVI 384p (+IA MP4) | orig: mpeg4 512x384 865kbps; IA MP4: h264 512x384 792kbps |  |
| 7 | Timon & Pumbaa (WEB-DL 1080p) + The Legend of Tarzan | https://archive.org/details/DisneysTheLegendOfTarzan720pHDTV | 85 T&P + 39 Tarzan | Complete (both) | MKV 1080p/720p (+IA MP4) | orig: h264 1920x1080 4389kbps; IA MP4: h264 640x360 830kbps | Upgrades his 18-ep Timon & Pumbaa. Tarzan files have a Russian 1st audio track (English is the 2nd), so pick English. AVI alternative: timonpumbaa (135 AVI). |

### Toon Disney fill

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Aladdin: The Series | https://archive.org/details/disneys-aladdin-the-series-1994 | 85 / 86 | Near-complete | MKV 480p (+IA MP4) | orig: h264 640x480 1395kbps; IA MP4: h264 640x480 764kbps |  |
| 2 | Bonkers S1-4 | https://archive.org/details/disney-bonkers-season-1 | 22+11+23+9 = 65 / 65 | Complete across 4 items | MKV 480p (+IA MP4) | orig: h264 640x480 3126kbps; IA MP4: h264 654x480 797kbps | Other items: disney-bonkers-season-2, -season-3, -season-4. |
| 3 | Mighty Ducks: The Animated Series | https://archive.org/details/mighty-ducks-the-animated-series_20260115 | 26 / 26 | Complete | MKV HEVC 480p (+IA MP4) | orig: hevc 640x478 886kbps; IA MP4: h264 640x478 798kbps |  |
| 4 | House of Mouse | https://archive.org/details/disneys-house-of-mouse-full-series | 68 files / 52 eps | Complete | Direct MP4, 360p (low) | MP4: h264 538x360 442kbps |  |
| 5 | Adventures of the Gummi Bears S1-3 | https://archive.org/details/gummi-bears-s-01-e-09-a-gummi-by-any-other-name_202602 | 47 files (S1-3) | Partial (S1-3 of 6) | Direct MP4, 480p | MP4: h264 640x480 839kbps | Single-season items for S4-S6 also exist (gummi-bears-s-04-e-15-top-gum, etc.). |
| 6 | Dave the Barbarian | https://archive.org/details/DaveTheBarbarian | 21 / 21 | Complete | AVI (+480p IA MP4) | orig: mpeg4 512x384 1080kbps; IA MP4: h264 640x480 833kbps |  |

### Nickelodeon 90s fill

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Are You Afraid of the Dark? (1990-2000) | https://archive.org/details/are-you-afraid-of-the-dark-1992 | 91 / 91 | Complete | MKV HEVC 480p (+IA MP4) | orig: hevc 706x480 2233kbps; IA MP4: h264 626x480 791kbps | Mildly spooky, rated TV-Y7. |
| 2 | Jimmy Neutron (series + specials) | https://archive.org/details/0x-01-runaway-rocketboy_202304 | 70 / 52 eps + specials | Complete | Direct MP4, 480p | MP4: h264 640x480 731kbps |  |
| 3 | Invader Zim | https://archive.org/details/invader-zim-seasons-1-2-full-series | 27 / 27 | Complete | Direct MP4, 480p | MP4: h264 716x480 1007kbps |  |
| 4 | As Told by Ginger | https://archive.org/details/astoldbygingercomplete | 56 / 60 | Near-complete | Direct MP4, 576p (EAC3 audio) | MP4: h264 720x576 1018kbps | EAC3 audio may need a player that supports it. |
| 5 | Hey Arnold! (1080p) | https://archive.org/details/hey-arnold-1996 | 20 / 100 | Partial | MKV 1080p (+IA MP4) | orig: h264 1424x1080 2787kbps; IA MP4: h264 632x480 770kbps | No full Hey Arnold set on IA. Nick shows (Rugrats, Hey Arnold, Rocko, CatDog, Wild Thornberrys, Angry Beavers, Real Monsters) are mostly taken down. |
| 6 | Rocko's Modern Life S1 | https://archive.org/details/rockos-modern-life_202412 | 13 / 52 | Partial (S1 only) | Direct MP4, 480p | MP4: h264 720x480 853kbps | S2: rockos-modern-life-season-2. |

### Disney Channel 2003-2008 fill

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Lizzie McGuire S1 + S2 | https://archive.org/details/lizzie-mcguire-season1 | 31 + 34 = 65 / 65 | Complete across 2 items | MKV HEVC 720p (+480p IA MP4) | orig: hevc 936x720 2630kbps; IA MP4: h264 624x480 790kbps | He has 46 eps. Second item: lizzie-mcguire-season2. |
| 2 | Phil of the Future | https://archive.org/details/phil-of-the-future | 43 / 43 | Complete | MP4 (HEVC inside), 480p | MP4: hevc 640x480 1696kbps | He has 21 eps. |
| 3 | American Dragon: Jake Long | https://archive.org/details/American-Dragon-Jake-Long-The-Complete-Series | 52 / 52 | Complete | Direct MP4, 1072x592 | MP4: h264 1072x592 2255kbps | He has 42 eps. |
| 4 | That's So Raven S2 | https://archive.org/details/AULVAC-thats-so-raven-season-2-complete-480p-hevc-10bit-aac-lc-mkv_202404 | 22 / 22 | Season complete | MKV HEVC 10-bit 480p (+IA MP4) | orig: hevc 630x478 1158kbps; IA MP4: h264 630x478 797kbps | He has 76 Raven eps, so check overlap first. |

### PBS KIDS 2000s fill

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Arthur (complete, as aired) | https://archive.org/details/arthur-1996-complete_202203 | 260 MKV | Complete (S1-25) | MKV 480p (+IA MP4) | orig: h264 720x480 3130kbps; IA MP4: h264 640x480 794kbps | He has 10 eps (S8). |
| 2 | The Magic School Bus | https://archive.org/details/MSBTVSeries | 52 / 52 | Complete | Direct MP4, 480p | MP4: h264 720x480 1705kbps |  |
| 3 | Zoboomafoo S1 + S2 | https://archive.org/details/zoboomafoo-season-1 | 40 + 25 = 65 / 65 | Complete across 2 items | Direct MP4, 720p | MP4: h264 1280x720 3407kbps | Second item: zoboomafoo.-season-2. |
| 4 | Wishbone (remastered) | https://archive.org/details/wishbonefullseriesremastered | 52 / 50 + 2 specials | Complete | MKV 480p (+IA MP4) | orig: h264 640x480 2135kbps; IA MP4: h264 640x480 804kbps |  |
| 5 | Cyberchase S1-5 | https://archive.org/details/CyberchaseS1S2 | 72 eps | Complete for the 2002-07 era | MKV 480p (+IA MP4) | orig: h264 640x480 783kbps; IA MP4: h264 640x480 761kbps |  |
| 6 | Between the Lions | https://archive.org/details/between-the-lions-2000 | 136 / 130 | Complete | Direct MP4, 480p | MP4: h264 640x480 842kbps |  |
| 7 | Maya & Miguel | https://archive.org/details/MMTVSeries | 129 MP4 (65 eps + segments) | Complete | Direct MP4, 480p | MP4: h264 640x480 540kbps; orig: h264 640x480 2196kbps; IA MP4: h264 640x480 828kbps |  |
| 8 | Fetch! with Ruff Ruffman | https://archive.org/details/FWRRTVSeries | 100 | Complete | Direct MP4, 480p | MP4: h264 640x480 785kbps |  |
| 9 | Sagwa, the Chinese Siamese Cat | https://archive.org/details/sagwa-the-chinese-siamese-cat-01 | 42 / 40 | Complete | Direct MP4, 720p | MP4: h264 962x720 773kbps |  |
| 10 | The Berenstain Bears (2003) | https://archive.org/details/TheBerenstainBearsFull | 40 / 40 | Complete | Direct MP4, 480p | MP4: h264 640x480 631kbps |  |
| 11 | Liberty's Kids | https://archive.org/details/LibertysKidsSeries | 41 / 40 | Complete | Direct MP4, 360p | MP4: h264 480x360 508kbps |  |
| 12 | ZOOM (1999-2005) | https://archive.org/details/zoom1999completionist | 207 | Almost complete | Direct MP4, 360p | MP4: h264 480x360 557kbps |  |

### Winnie the Pooh fill

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | The Book of Pooh | https://archive.org/details/s-01.-e-23-the-book-of-pooh-busy-as-a-spelling-bee-up-in-the-air-junior-bird-donkey | 51 eps | Complete | Direct MP4, 480p (2.7 Mbps) | MP4: h264 640x480 2730kbps | Playhouse Disney era. |

### Pokémon fill

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Pokémon: Adventures in the Orange Islands (S2) | https://archive.org/details/pokemon-adventures-in-the-orange-islands-the-complete-series-1999 | 36 / 36 | Complete | Direct MP4, 480p | MP4: h264 640x480 1451kbps | HD option: pokemon-1997-season-2 (36 MKV, 960x720). |
| 2 | Pokémon Kanto Movie Collection | https://archive.org/details/pokemon-kanto-movie-collection | 5 movies | Complete | MKV 480p (+IA MP4) | orig: h264 640x480 2139kbps; IA MP4: h264 640x480 797kbps |  |

### X-Men/Superhero fill

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | X-Men: Evolution | https://archive.org/details/x-men-evolution-1080p-ai-upscale | 49 / 52 | Near-complete | MKV HEVC 1080p (+480p IA MP4) | orig: hevc 1602x1078 6047kbps; IA MP4: h264 642x480 777kbps |  |
| 2 | Iron Man (1994) | https://archive.org/details/iron-man-1994-complete-series | 26 / 26 | Complete | Direct MP4, 480p | MP4: h264 640x480 721kbps |  |
| 3 | Fantastic Four (1994) | https://archive.org/details/fantastic-four-1994_202412 | 26 / 26 | Complete | MKV 480p (+IA MP4) | MP4: h264 640x480 1561kbps; orig: h264 640x480 1568kbps; IA MP4: h264 640x480 779kbps |  |
| 4 | Spider-Man Unlimited | https://archive.org/details/spider-man-unlimited-1999-2001 | 13 / 13 | Complete | MKV 480p (+IA MP4) | orig: h264 640x480 2168kbps; IA MP4: h264 640x480 807kbps |  |
| 5 | Silver Surfer | https://archive.org/details/silver-surfer-s01 | 13 / 13 | Complete | MKV 480p (+IA MP4) | orig: h264 640x480 1984kbps; IA MP4: h264 640x480 800kbps |  |

### Retro Saturday Morning (new)

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Adventures of Sonic the Hedgehog | https://archive.org/details/adventures-of-sonic-the-hedgehog-the-complete-collection | 67 / 65 + special | Complete | Direct MP4, 720p | MP4: h264 960x720 1254kbps |  |
| 2 | Cardcaptors (Nelvana dub) | https://archive.org/details/cardcaptors-07-the-mysterious-painting | 70 / 70 | Complete | AVI (+480p IA MP4) | orig: mpeg4 640x480 1698kbps; IA MP4: h264 640x480 801kbps | Kids' WB era. |
| 3 | Super Mario Bros. Super Show! | https://archive.org/details/the-super-mario-bros.-super-show-1989_20231118 | 52 MKV | Complete | MKV HEVC 576p only (no IA MP4) | orig: hevc 720x576 5242kbps | Needs HEVC support. |

### Christmas (new)

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Rankin/Bass Christmas Specials (1964-1985) | https://archive.org/details/rankin-bass-christmas-specials | 14 specials | Complete classic set | Direct MP4, 480p | MP4: h264 640x480 775kbps | Rudolph, Frosty, Santa Claus Is Comin', Year Without a Santa Claus, Little Drummer Boy, Nestor, Jack Frost, etc. |
| 2 | Nickelodeon Animated Christmas Specials & Shorts | https://archive.org/details/planktons-holiday-hits | 42 | Curated set | Direct MP4, up to 720p | MP4: h264 976x720 1190kbps | Rugrats, Hey Arnold, Doug, CatDog, Rocko, Real Monsters, Angry Beavers, Thornberrys, Ginger, Zim, Danny Phantom, FOP, Jimmy Neutron, Rocket Power, SpongeBob. |
| 3 | Cartoon Network Christmas/Winter Specials & Episodes | https://archive.org/details/001.-the-shanty-where-santy-claus-lives | 254 files (specials split into parts) | Large set | Direct MP4, 720p | MP4: h264 960x720 4750kbps | Dexter, PPG, Johnny Bravo, Ed Edd n Eddy, Billy & Mandy, KND, Pinky & Brain, Tiny Toons, Flintstones/Jetsons/Scooby. Specials are split into segments. |
| 4 | Holiday Specials (kids TV) | https://archive.org/details/christmas-specials_202412 | 444 MP4 | Large set, light curation | Direct MP4, 480p | MP4: h264 720x480 1200kbps; orig: mpeg4 640x480 3855kbps; IA MP4: h264 640x480 778kbps | Mostly kids TV holiday episodes (Rugrats, Arthur, Doug, Hey Arnold, Barney, Teletubbies, TMNT, SpongeBob...). Skim before adding. |
| 5 | PBS Kids Christmas Specials | https://archive.org/details/sesame-street-christmas-eve-on-sesame-street | 24 | Curated set | Direct MP4, 480p | MP4: h264 640x480 2129kbps | Arthur's Perfect Christmas, Magic School Bus, Cyberchase, Liberty's Kids, Maya & Miguel, Sesame Street. |
| 6 | Playhouse Disney / Disney Junior Christmas Specials | https://archive.org/details/mickey-mouse-clubhouse-mickey-saves-santa_202412 | 24 | Curated set | Direct MP4, 360p | MP4: h264 640x360 513kbps | Bear in the Big Blue House, Book of Pooh, Tigger & Pooh, Rolie Polie Olie, Mickey. |
| 7 | Nick Jr. Christmas Specials | https://archive.org/details/allegras-window-waiting-for-grandma_202412 | 20 | Curated set | Direct MP4, 480p | MP4: h264 640x480 778kbps | Blue's Clues, Dora, Little Bill, Gullah Gullah, Kipper, Backyardigans. |
| 8 | Christmas Movies (family) | https://archive.org/details/christmas-movies_07112025 | 44 | Mixed movie set | Direct MP4, 480p | MP4: h264 704x480 1201kbps | Home Alone 1+2, Polar Express, Christmas with the Kranks, Miracle on 34th St, Charlie Brown, Frosty, Rudolph, Barney, old classics. Already has Beauty & the Beast Enchanted Christmas. |
| 9 | A Muppet Family Christmas (+extras) | https://archive.org/details/a-muppet-family-christmas | 12 | Complete | MKV 480p (+IA MP4) | orig: h264 640x480 4193kbps; IA MP4: h264 640x480 756kbps |  |
| 10 | Billy & Mandy TV Movies & Specials | https://archive.org/details/the-grim-adventures-of-billy-and-mandy-s-2-billy-and-mandy-save-christmas-emory | 8 originals | Complete specials | MP4/AVI | MP4: h264 720x480 3087kbps; orig: mpeg4 512x384 1262kbps; IA MP4: h264 512x384 801kbps | Includes Billy & Mandy Save Christmas. |
| 11 | Holiday episodes grab-bag (CURATE) | https://archive.org/details/a-flintstone-christmas | 88 | Mixed. Pick kids' files only | Direct MP4, 360p | MP4: h264 480x360 485kbps | Has good kids' episodes (Kim Possible, KND, Static Shock, Proud Family, Recess Christmas, Danny Phantom) but ALSO American Dad, Simpsons, Aqua Teen, That '70s Show. Use only the hand-picked kids' files. |

### Wrestling fill

| # | Show | Item | Episodes (have / known) | Complete? | Playback | ffprobe sample | Notes |
|---|---|---|---|---|---|---|---|
| 1 | WCW 1997 | https://archive.org/details/wcw-1997-reupload-wwearchives | 66 MKV (in progress, complete through Oct 22 2025) | Large | MKV 1080p (+480p IA MP4) | orig: h264 1920x1080 7817kbps; IA MP4: h264 854x480 775kbps | Next year after his WCW 1996. Each file ~1.5 hr. |
| 2 | WCW Worldwide 1999 | https://archive.org/details/wcw.-worldwide.-complete_202406 | 51 / 51 | Complete | AVI (+480p IA MP4) | orig: mpeg4 640x480 1183kbps; IA MP4: h264 640x480 783kbps |  |


Total candidate rows: 87 (plus the alternate items named in the notes).
