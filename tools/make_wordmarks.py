#!/usr/bin/env python3
"""Nostalgia-style wide wordmarks for Jordan TV: 480x104 transparent WebP.
One typeface (Anton), 2-3 flat colors, thick outline, soft shadow, small themed emblem."""
import math, io, base64, json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ANTON = "/usr/share/fonts/truetype/sand-box/google/Anton/Anton-Regular.ttf"
OUT = Path("/workspace/jordantv/logos"); OUT.mkdir(exist_ok=True)
S = 2                      # supersample
W, H = 480 * S, 104 * S
EM = 92 * S                # emblem box

def F(sz): return ImageFont.truetype(ANTON, sz)

# ---------- emblems: draw(d, box, fill, line, accent) on RGBA layer, box=(x0,y0,x1,y1)
def _c(b): x0, y0, x1, y1 = b; return (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2
LW = 6 * S
def star_pts(cx, cy, r, n=5, inner=0.45, rot=-90):
    pts = []
    for i in range(n * 2):
        rr = r if i % 2 == 0 else r * inner
        a = math.radians(rot + i * 180 / n)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts
def e_star(d, b, f, l, a):
    cx, cy, r = _c(b); d.polygon(star_pts(cx, cy, r * .95), fill=f, outline=l, width=LW)
def e_tree(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.polygon([(cx, cy - r), (cx + r * .8, cy + r * .6), (cx - r * .8, cy + r * .6)], fill=f, outline=l, width=LW)
    d.rectangle((cx - r * .15, cy + r * .6, cx + r * .15, cy + r), fill=l)
    d.polygon(star_pts(cx, cy - r * .92, r * .25), fill=a)
def e_candy(d, b, f, l, a):
    cx, cy, r = _c(b)
    w = r * .32
    d.arc((cx - r * .55, cy - r, cx + r * .45, cy), 180, 360, fill=l, width=int(w + LW * 2))
    d.line((cx + r * .45 - 0, cy - r * .5, cx + r * .45, cy + r), fill=l, width=int(w + LW * 2))
    d.arc((cx - r * .55, cy - r, cx + r * .45, cy), 180, 360, fill=f, width=int(w))
    d.line((cx + r * .45, cy - r * .5, cx + r * .45, cy + r * .95), fill=f, width=int(w))
    for k in range(4):
        y = cy - r * .2 + k * r * .32
        d.line((cx + r * .45 - w / 2, y, cx + r * .45 + w / 2, y - w * .6), fill=a, width=int(w * .35))
    for ang in (200, 245, 290, 335):
        t = math.radians(ang); rx, ry = r * .5, r * .5
        x = cx - r * .05 + rx * math.cos(t); y = cy - r * .5 + ry * math.sin(t)
        d.ellipse((x - w * .2, y - w * .2, x + w * .2, y + w * .2), fill=a)
def e_ornament(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.rectangle((cx - r * .2, cy - r, cx + r * .2, cy - r * .6), fill=a, outline=l, width=LW // 2)
    d.ellipse((cx - r * .8, cy - r * .7, cx + r * .8, cy + r * .9), fill=f, outline=l, width=LW)
    d.line((cx - r * .7, cy + r * .1, cx + r * .7, cy + r * .1), fill=a, width=LW * 2)
def e_wreath(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=l)
    d.ellipse((cx - r + LW, cy - r + LW, cx + r - LW, cy + r - LW), fill=f)
    d.ellipse((cx - r * .45, cy - r * .45, cx + r * .45, cy + r * .45), fill=(0, 0, 0, 0), outline=l, width=LW)
    for k in range(8):
        t = math.radians(k * 45); x, y = cx + r * .73 * math.cos(t), cy + r * .73 * math.sin(t)
        d.ellipse((x - r * .1, y - r * .1, x + r * .1, y + r * .1), fill=a)
    d.polygon([(cx, cy + r * .55), (cx - r * .35, cy + r), (cx + r * .35, cy + r)], fill=a)
def e_belt(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.rounded_rectangle((b[0] - 4 * S, cy - r * .32, b[2] + 4 * S, cy + r * .32), radius=8 * S, fill=l)
    pts = [(cx + r * .95 * math.cos(math.radians(30 + 60 * k)), cy + r * .8 * math.sin(math.radians(30 + 60 * k))) for k in range(6)]
    d.polygon(pts, fill=f, outline=l, width=LW)
    d.polygon(star_pts(cx, cy, r * .42), fill=a)
def e_bolt(d, b, f, l, a):
    cx, cy, r = _c(b)
    pts = [(cx + r * .2, cy - r), (cx - r * .6, cy + r * .1), (cx - r * .05, cy + r * .1), (cx - r * .3, cy + r), (cx + r * .65, cy - r * .2), (cx + r * .08, cy - r * .2)]
    d.polygon(pts, fill=f, outline=l, width=LW)
def e_badge(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=f, outline=l, width=LW)
    d.polygon(star_pts(cx, cy, r * .6), fill=a, outline=l, width=LW // 2)
def e_sun(d, b, f, l, a):
    cx, cy, r = _c(b)
    for k in range(12):
        t = math.radians(k * 30)
        d.line((cx + r * .6 * math.cos(t), cy + r * .6 * math.sin(t), cx + r * math.cos(t), cy + r * math.sin(t)), fill=a, width=LW + 2 * S)
    d.ellipse((cx - r * .58, cy - r * .58, cx + r * .58, cy + r * .58), fill=f, outline=l, width=LW)
def e_checker(d, b, f, l, a):
    x0, y0, x1, y1 = b; n = 4; s = (x1 - x0) / n
    for i in range(n):
        for j in range(n):
            d.rectangle((x0 + i * s, y0 + j * s, x0 + (i + 1) * s, y0 + (j + 1) * s), fill=f if (i + j) % 2 else a)
    d.rectangle(b, outline=l, width=LW)
def e_shield(d, b, f, l, a):
    cx, cy, r = _c(b)
    pts = [(cx - r * .85, cy - r * .9), (cx + r * .85, cy - r * .9), (cx + r * .85, cy + r * .1), (cx, cy + r), (cx - r * .85, cy + r * .1)]
    d.polygon(pts, fill=f, outline=l, width=LW)
    d.polygon(star_pts(cx, cy - r * .05, r * .42), fill=a)
def e_splat(d, b, f, l, a):
    cx, cy, r = _c(b)
    pts = []
    for k in range(20):
        t = math.radians(k * 18); rr = r * (0.95 if k % 2 == 0 else 0.62) * (0.9 + 0.1 * math.sin(k * 1.7))
        pts.append((cx + rr * math.cos(t), cy + rr * math.sin(t)))
    d.polygon(pts, fill=f, outline=l, width=LW)
    d.ellipse((cx + r * .55, cy + r * .6, cx + r * .8, cy + r * .85), fill=f, outline=l, width=LW // 2)
def e_burst(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.polygon(star_pts(cx, cy, r, n=12, inner=0.62), fill=f, outline=l, width=LW)
    d.ellipse((cx - r * .32, cy - r * .32, cx + r * .32, cy + r * .32), fill=a)
def e_tv(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.line((cx - r * .4, cy - r, cx, cy - r * .55), fill=l, width=LW); d.line((cx + r * .4, cy - r, cx, cy - r * .55), fill=l, width=LW)
    d.rounded_rectangle((cx - r, cy - r * .55, cx + r, cy + r * .85), radius=12 * S, fill=f, outline=l, width=LW)
    d.rounded_rectangle((cx - r * .75, cy - r * .32, cx + r * .45, cy + r * .62), radius=8 * S, fill=a)
def e_bars(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.rounded_rectangle((cx - r, cy - r * .7, cx + r, cy + r * .7), radius=10 * S, fill=l)
    cols = [(240, 240, 240), (240, 220, 0), (0, 220, 230), (0, 200, 60), (230, 0, 200), (230, 30, 30), (30, 40, 230)]
    w = (2 * r - 2 * LW) / 7
    for i, c in enumerate(cols):
        d.rectangle((cx - r + LW + i * w, cy - r * .7 + LW, cx - r + LW + (i + 1) * w, cy + r * .7 - LW), fill=c)
def e_tape(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.rounded_rectangle((cx - r, cy - r * .62, cx + r, cy + r * .62), radius=8 * S, fill=f, outline=l, width=LW)
    d.rectangle((cx - r * .6, cy - r * .3, cx + r * .6, cy + r * .25), fill=l)
    for x in (cx - r * .32, cx + r * .32):
        d.ellipse((x - r * .17, cy - r * .2, x + r * .17, cy + r * .14), fill=a)
def e_reel(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=f, outline=l, width=LW)
    for k in range(6):
        t = math.radians(k * 60 + 30); x, y = cx + r * .52 * math.cos(t), cy + r * .52 * math.sin(t)
        d.ellipse((x - r * .2, y - r * .2, x + r * .2, y + r * .2), fill=l)
    d.ellipse((cx - r * .12, cy - r * .12, cx + r * .12, cy + r * .12), fill=a)
def e_pot(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.ellipse((cx - r * .85, cy - r * .55, cx + r * .85, cy + r), fill=f, outline=l, width=LW)
    d.rounded_rectangle((cx - r * .7, cy - r * .8, cx + r * .7, cy - r * .45), radius=6 * S, fill=f, outline=l, width=LW)
    d.text((cx, cy + r * .25), "HUNNY", font=F(int(r * .38)), fill=l, anchor="mm")
def e_bag(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.arc((cx - r * .4, cy - r, cx + r * .4, cy - r * .2), 180, 360, fill=l, width=LW)
    d.rounded_rectangle((cx - r * .8, cy - r * .55, cx + r * .8, cy + r), radius=8 * S, fill=f, outline=l, width=LW)
    d.text((cx, cy + r * .25), "$", font=F(int(r * .9)), fill=a, anchor="mm")
def e_cam(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.rounded_rectangle((cx - r, cy - r * .55, cx + r * .45, cy + r * .6), radius=10 * S, fill=f, outline=l, width=LW)
    d.polygon([(cx + r * .45, cy - r * .1), (cx + r, cy - r * .45), (cx + r, cy + r * .5), (cx + r * .45, cy + r * .15)], fill=f, outline=l, width=LW)
    d.ellipse((cx - r * .55, cy - r * .3, cx + r * .05, cy + r * .3), fill=a, outline=l, width=LW // 2)
def e_brush(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.ellipse((cx - r, cy - r * .75, cx + r * .9, cy + r * .8), fill=f, outline=l, width=LW)
    for (x, y, c) in ((-.45, -.25, a), (0, -.42, (60, 120, 230)), (.4, -.18, (40, 170, 70)), (-.4, .3, (250, 200, 30))):
        d.ellipse((cx + x * r - r * .16, cy + y * r - r * .16, cx + x * r + r * .16, cy + y * r + r * .16), fill=c)
    d.ellipse((cx + r * .25, cy + r * .2, cx + r * .6, cy + r * .55), fill=(0, 0, 0, 0), outline=l, width=LW // 2)
def e_paw(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.ellipse((cx - r * .55, cy - r * .05, cx + r * .55, cy + r * .85), fill=f, outline=l, width=LW)
    for (x, y) in ((-.75, -.35), (-.28, -.8), (.28, -.8), (.75, -.35)):
        d.ellipse((cx + x * r - r * .24, cy + y * r - r * .24, cx + x * r + r * .24, cy + y * r + r * .24), fill=f, outline=l, width=LW)
def e_sparkle(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.polygon(star_pts(cx - r * .1, cy + r * .05, r * .9, n=4, inner=0.28, rot=-90), fill=f, outline=l, width=LW)
    d.polygon(star_pts(cx + r * .62, cy - r * .62, r * .35, n=4, inner=0.3, rot=-90), fill=a)
def e_bowl(d, b, f, l, a):
    cx, cy, r = _c(b)
    for (x, y, c) in ((-.4, -.25, a), (0, -.4, (255, 120, 40)), (.4, -.25, (90, 200, 255)), (-.15, -.05, (250, 230, 60)), (.25, -.02, a)):
        d.ellipse((cx + x * r - r * .2, cy + y * r - r * .2, cx + x * r + r * .2, cy + y * r + r * .2), fill=c, outline=l, width=LW // 3)
    d.chord((cx - r, cy - r * .5, cx + r, cy + r), 0, 180, fill=f, outline=l, width=LW)
def e_popcorn(d, b, f, l, a):
    cx, cy, r = _c(b)
    for (x, y) in ((-.45, -.55), (0, -.75), (.45, -.55), (-.2, -.35), (.25, -.35)):
        d.ellipse((cx + x * r - r * .28, cy + y * r - r * .28, cx + x * r + r * .28, cy + y * r + r * .28), fill=(255, 245, 210), outline=l, width=LW // 2)
    d.polygon([(cx - r * .75, cy - r * .3), (cx + r * .75, cy - r * .3), (cx + r * .5, cy + r), (cx - r * .5, cy + r)], fill=f, outline=l, width=LW)
    d.line((cx, cy - r * .3, cx, cy + r), fill=a, width=LW * 2)
def e_fox(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.polygon([(cx - r * .95, cy - r), (cx - r * .35, cy - r * .45), (cx + r * .35, cy - r * .45), (cx + r * .95, cy - r), (cx + r * .8, cy + r * .1), (cx, cy + r), (cx - r * .8, cy + r * .1)], fill=f, outline=l, width=LW)
    d.polygon([(cx - r * .55, cy + r * .15), (cx, cy + r * .95), (cx + r * .55, cy + r * .15), (cx, cy + r * .35)], fill=a)
    for x in (-.35, .35): d.ellipse((cx + x * r - r * .1, cy - r * .2, cx + x * r + r * .1, cy), fill=l)
def e_snow(d, b, f, l, a):
    cx, cy, r = _c(b)
    for k in range(6):
        t = math.radians(k * 60)
        d.line((cx, cy, cx + r * math.cos(t), cy + r * math.sin(t)), fill=l, width=LW * 2)
    for k in range(6):
        t = math.radians(k * 60)
        d.line((cx, cy, cx + r * .9 * math.cos(t), cy + r * .9 * math.sin(t)), fill=f, width=LW)
    d.ellipse((cx - r * .2, cy - r * .2, cx + r * .2, cy + r * .2), fill=a)
def e_planet(d, b, f, l, a):
    cx, cy, r = _c(b)
    d.ellipse((cx - r * .62, cy - r * .62, cx + r * .62, cy + r * .62), fill=f, outline=l, width=LW)
    d.arc((cx - r, cy - r * .35, cx + r, cy + r * .35), -20, 200, fill=l, width=LW * 2)
    d.arc((cx - r, cy - r * .35, cx + r, cy + r * .35), -20, 200, fill=a, width=LW)


def e_pumpkin(d, b, f, l, a):
    cx, cy, r = _c(b)
    # pumpkin body
    d.ellipse((cx - r * .95, cy - r * .55, cx + r * .95, cy + r * .95), fill=f, outline=l, width=LW)
    d.ellipse((cx - r * .7, cy - r * .6, cx + r * .7, cy + r * .95), fill=f, outline=l, width=max(LW//2, 2))
    # stem
    d.rounded_rectangle((cx - r * .12, cy - r * .95, cx + r * .12, cy - r * .45), radius=4 * S, fill=a, outline=l, width=LW // 2)
    # jack-o-lantern face
    d.polygon([(cx - r * .45, cy - r * .15), (cx - r * .15, cy - r * .15), (cx - r * .3, cy + r * .08)], fill=l)
    d.polygon([(cx + r * .15, cy - r * .15), (cx + r * .45, cy - r * .15), (cx + r * .3, cy + r * .08)], fill=l)
    d.polygon([(cx - r * .35, cy + r * .35), (cx - r * .2, cy + r * .18), (cx + r * .2, cy + r * .18), (cx + r * .35, cy + r * .35), (cx, cy + r * .5)], fill=l)

def e_frog(d, b, f, l, a):
    cx, cy, r = _c(b)
    # head
    d.ellipse((cx - r * .85, cy - r * .35, cx + r * .85, cy + r * .85), fill=f, outline=l, width=LW)
    # eyes
    for x in (-.42, .42):
        d.ellipse((cx + x * r - r * .32, cy - r * .95, cx + x * r + r * .32, cy - r * .15), fill=f, outline=l, width=LW)
        d.ellipse((cx + x * r - r * .16, cy - r * .72, cx + x * r + r * .16, cy - r * .32), fill=l)
        d.ellipse((cx + x * r - r * .06, cy - r * .62, cx + x * r + r * .06, cy - r * .44), fill=a)
    # smile
    d.arc((cx - r * .55, cy + r * .05, cx + r * .55, cy + r * .7), 20, 160, fill=l, width=LW)

def e_blocks(d, b, f, l, a):
    cx, cy, r = _c(b)
    for (x, y, sz, c, t) in ((-.5, .5, .94, f, "A"), (.5, .5, .94, a, "B"), (0, -.48, .94, (90, 200, 255), "C")):
        x0, y0 = cx + x * r - sz * r / 2 * 1.0, cy + y * r - sz * r / 2
        d.rounded_rectangle((x0, y0, x0 + sz * r, y0 + sz * r), radius=int(r * .08), fill=c, outline=l, width=LW)
        fo = F(int(sz * r * .72)); bb = fo.getbbox(t)
        d.text((x0 + sz * r / 2 - (bb[0] + bb[2]) / 2, y0 + sz * r / 2 - (bb[1] + bb[3]) / 2), t, font=fo, fill=l)

# key: (station name, main text, sub text, fill, outline, accent, emblem)
WHITE=(255,255,255); BLACK=(12,8,20); GOLD=(255,200,40); RED=(210,30,40); GREEN=(30,150,70); NAVY=(20,30,90)
SPECS = [
 ("christmas-cartoons","Christmas Cartoons","XMAS TOONS","",WHITE,RED,GREEN,e_tree),
 ("bluey","Bluey","BLUEY","",(130,200,255),NAVY,(255,190,90),e_paw),
 ("family-vids","Family Vids","FAMILY VIDS","",GOLD,(90,40,10),(240,90,40),e_cam),
 ("wdw-christmas","Walt Disney World Christmas Day ","WDW XMAS","",WHITE,NAVY,GOLD,e_sparkle),
 ("christmas-paintings","Christmas Paintings","XMAS ART","",(255,235,200),(120,20,30),RED,e_brush),
 ("vhs-kids","VHS Kids Movies","VHS KIDS","",(255,230,140),BLACK,(240,90,40),e_tape),
 ("disney-channel","Disney Channel 2003-2008 era","DISNEY 03-08","",WHITE,(20,60,120),(80,220,240),e_sparkle),
 ("pbs-kids","PBS KIDS 2000's","PBS KIDS","",(120,230,80),(20,60,20),(255,170,30),e_sun),
 ("disney-animated","Disney Animated-In Order","CLASSICS","",(255,220,120),(60,20,90),WHITE,e_reel),
 ("toon-disney","Toon Disney","TOON DISNEY","",(255,150,30),(60,20,100),(140,220,60),e_splat),
 ("nickelodeon-90s","Nickelodeon 90s","NICK 90s","",(255,140,20),(70,20,110),(140,230,40),e_splat),
 ("qvc-90s","QVC 90s","QVC 90s","",(255,220,80),(0,70,110),(255,255,255),e_bag),
 ("disneytoon","DisneyToon Studios Films (1990-2","TOON FILMS","",(230,200,255),(60,20,100),GOLD,e_reel),
 ("pooh","The New Adventures of Winnie the","POOH","",(255,200,60),(120,50,10),RED,e_pot),
 ("abc-saturday","ABC Saturday Morning 2000's","SAT AM 2000s","",(255,215,0),BLACK,(255,90,60),e_bowl),
 ("dcom","Disney Channel Original Movies C","DCOM","",WHITE,(20,60,120),(255,90,170),e_popcorn),
 ("wcw","WCW","WCW","",(255,214,0),BLACK,(255,255,255),e_belt),
 ("wwf","WWF","WWF","",WHITE,(150,0,0),GOLD,e_belt),
 ("superhero","X-Men/TMNT/SuperHeroShows","HEROES","",(255,220,40),(20,30,110),RED,e_bolt),
 ("pokemon","Pokémon: Indigo League","INDIGO","",(255,220,50),(30,40,120),(230,40,40),e_badge),
 ("fox-kids","Fox Kids","FOX KIDS","",(255,230,40),(20,90,30),(255,120,0),e_fox),
 ("cn-90s","Cartoon Network 90s","CN 90s","",WHITE,BLACK,(255,200,0),e_checker),
 ("kids-wb","Kids' WB","KIDS' WB","",(255,170,30),(10,20,80),(255,230,80),e_shield),
 ("christmas-specials","Christmas Specials","XMAS SPECIALS","",WHITE,(20,90,40),RED,e_wreath),
 ("tgif","TGIF","TGIF","",(255,210,0),(70,20,110),(60,200,255),e_tv),
 ("retro-ads","Retro Commercials","RETRO ADS","",WHITE,BLACK,(255,60,160),e_bars),
 ("christmas-movies","Christmas Movies","XMAS MOVIES","",WHITE,(20,100,45),RED,e_candy),
 ("holiday-episodes","Holiday Episodes","HOLIDAY TOONS","",(255,240,210),(130,15,25),(40,170,80),e_ornament),
 ("anime","Toonami Anime","ANIME","",WHITE,(20,15,70),(255,120,0),e_planet),
 ("saturday-morning","Retro Saturday Morning","SAT MORNING","",WHITE,(30,60,160),(255,200,0),e_sun),
 ("preschool","Preschool","PRESCHOOL","",(255,225,70),(110,30,140),(255,95,120),e_blocks),
 ("90s-classics","90s Classics","90s CLASSICS","",(255,220,70),(70,15,120),(255,90,180),e_popcorn),
    ("halloween","Halloween","HALLOWEEN","",(255,145,40),(40,8,70),(250,230,90),e_pumpkin),
    ("muppets","Muppets","MUPPETS","",(80,200,70),(12,50,18),(255,220,50),e_frog),
]

def fit(text, maxw, maxh):
    for sz in range(int(maxh * 1.35), 10, -2):
        f = F(sz); bb = f.getbbox(text, stroke_width=0)
        if bb[2] - bb[0] <= maxw and bb[3] - bb[1] <= maxh: return f
    return F(12)

def render(spec):
    key, name, main, sub, fill, line, acc, emb = spec
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    pad = 6 * S; box = (pad + 2 * S, (H - EM) // 2, pad + 2 * S + EM, (H - EM) // 2 + EM)
    emb(d, box, fill if emb not in (e_checker,) else WHITE, line, acc)
    x0 = box[2] + 12 * S; maxw = W - x0 - pad - 6 * S
    stroke = 6 * S
    if sub:
        fm = fit(main, maxw - 2 * stroke, 50 * S); fs = fit(sub, maxw - 2 * stroke, 27 * S)
        bm = fm.getbbox(main); bs = fs.getbbox(sub)
        hm, hs, gap = bm[3] - bm[1], bs[3] - bs[1], 8 * S
        top = (H - (hm + gap + hs)) / 2
        d.text((x0 + stroke - bm[0], top - bm[1]), main, font=fm, fill=fill, stroke_width=stroke, stroke_fill=line)
        d.text((x0 + stroke - bs[0], top + hm + gap - bs[1]), sub, font=fs, fill=acc, stroke_width=stroke // 2, stroke_fill=line)
    else:
        fm = fit(main, maxw - 2 * stroke, 70 * S); bm = fm.getbbox(main)
        hm = bm[3] - bm[1]
        d.text((x0 + stroke - bm[0], (H - hm) / 2 - bm[1]), main, font=fm, fill=fill, stroke_width=stroke, stroke_fill=line)
    # soft shadow
    alpha = layer.split()[3]
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh.putalpha(alpha.point(lambda v: int(v * 0.65)))
    sh = sh.filter(ImageFilter.GaussianBlur(5 * S))
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    canvas.alpha_composite(sh, (3 * S, 4 * S))
    canvas.alpha_composite(layer)
    img = canvas.resize((480, 104), Image.Resampling.LANCZOS)
    img.save(OUT / f"{key}.png")
    best = None
    for n in (28, 24, 20, 16):
        q = img.quantize(colors=n, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).convert("RGBA")
        b = io.BytesIO(); q.save(b, "WEBP", lossless=True, quality=100, method=6)
        best = b.getvalue()
        if len(best) <= 4000: break
    (OUT / f"{key}.webp").write_bytes(best)
    return key, name, len(best)

def preview(results):
    dark = (10, 6, 18); rows = []
    cols = 3; cw = 480 + 40
    sheet_h = 90 + len(SPECS) // cols * 0 
    n = len(SPECS); r = math.ceil(n / cols)
    # top: guide-size (240x52) column; below: full size
    W2 = cols * cw + 40
    H2 = 80 + r * (52 + 22) + 40 + r * (104 + 26) + 40
    sh = Image.new("RGB", (W2, H2), dark); d = ImageDraw.Draw(sh)
    d.text((20, 20), "JORDAN TV  CHANNEL LOGOS   guide size (52px tall)", font=F(30), fill=(255, 220, 120))
    y0 = 70
    for i, s in enumerate(SPECS):
        im = Image.open(OUT / f"{s[0]}.webp").convert("RGBA").resize((240, 52), Image.Resampling.LANCZOS)
        x = 20 + (i % cols) * cw; y = y0 + (i // cols) * 74
        d.rectangle((x - 6, y - 6, x + 300, y + 58), fill=(16, 3, 24))
        d.text((x - 2, y + 12), "", font=F(20))
        sh.paste(im, (x + 50, y), im)
        d.text((x, y + 12), str(i + 1), font=F(24), fill=(61, 240, 255))
    y1 = y0 + r * 74 + 30
    d.text((20, y1), "full size 480x104 (on-air bug size on a 1080p screen)", font=F(30), fill=(255, 220, 120))
    y1 += 50
    for i, s in enumerate(SPECS):
        im = Image.open(OUT / f"{s[0]}.webp").convert("RGBA")
        x = 20 + (i % cols) * cw; y = y1 + (i // cols) * 130
        sh.paste(im, (x, y), im)
    sh.save("/workspace/jordantv/icons-preview.png")

if __name__ == "__main__":
    import sys
    only = sys.argv[1:]
    res = [render(s) for s in SPECS if not only or s[0] in only]
    for r in res: print(r)
    json.dump({s[1]: s[0] for s in SPECS}, open(OUT / "name-map.json", "w"), indent=1)
    preview(res)
    print("max", max(r[2] for r in res), "avg", sum(r[2] for r in res) // len(res))
