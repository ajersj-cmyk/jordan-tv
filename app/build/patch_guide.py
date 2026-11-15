import sys
p='dec/assets/guide.html'; g=open('guide.orig.html').read()
def rep(old,new,count=1):
    global g
    n=g.count(old)
    assert n==count, (n, old[:80])
    g=g.replace(old,new)

# --- D: logos out of the save
rep('''function save() {
  rememberSpot();
  localStorage.setItem(KEY, JSON.stringify(state));''','''const LOGO_KEY = "jordan-tv-logos";
let savedLogos = null;
function save() {
  clearTimeout(saveTimer);
  saveTimer = 0;
  rememberSpot();
  localStorage.setItem(KEY, JSON.stringify(state, (k, v) => (k === "logo" ? undefined : v)));
  try {
    const logos = {};
    for (const item of state.stations) if (item.logo) logos[item.id] = item.logo;
    const text = JSON.stringify(logos);
    if (text !== savedLogos) { localStorage.setItem(LOGO_KEY, text); savedLogos = text; }
  } catch (e) { /* Logos are optional. */ }''')
rep('''    if (saved && Array.isArray(saved.stations) && saved.stations.length) {
      ensureSets(saved.stations);''','''    if (saved && Array.isArray(saved.stations) && saved.stations.length) {
      ensureSets(saved.stations);
      try {
        const logoText = localStorage.getItem("jordan-tv-logos");
        const logos = JSON.parse(logoText || "{}") || {};
        saved.stations.forEach((item) => { if (!item.logo && logos[item.id]) item.logo = logos[item.id]; });
      } catch (e) { /* No saved logos. */ }''')
# --- B: delayed save + one draw per frame
rep('''let tuned = null;
if (state.resume''','''let saveTimer = 0;
function saveSoon() {
  clearTimeout(saveTimer);
  saveTimer = setTimeout(() => { saveTimer = 0; save(); }, 800);
}
let drawQueued = false;
let navDraw = false;
function drawSoon() {
  navDraw = true;
  if (drawQueued) return;
  drawQueued = true;
  requestAnimationFrame(() => { drawQueued = false; draw(); });
}
window.addEventListener("pagehide", () => { if (saveTimer) save(); });
document.addEventListener("visibilitychange", () => { if (document.hidden && saveTimer) save(); });
let tuned = null;
if (state.resume''')
# --- A: cached shuffle order and totals
rep('''function orderedVideos(item) {
  const videos = playable(item);''','''const orderCache = new WeakMap();
function orderedVideos(item) {
  const list = item.videos || [];
  const sig = String(state.shuffleAt || 0) + "|" + item.mode + "|" + (item.skipShort ? 1 : 0) + "|" + list.length + "|" + (list[0] ? list[0].id : "") + "|" + (list.length ? list[list.length - 1].id : "");
  const hit = orderCache.get(item);
  if (hit && hit.sig === sig && hit.src === list) return hit.videos;
  const videos = orderedVideosRaw(item);
  orderCache.set(item, { sig, src: list, videos, total: videos.reduce((sum, video) => sum + Math.max(1, video.durationSec), 0) });
  return videos;
}
function orderTotal(item) {
  orderedVideos(item);
  return orderCache.get(item).total;
}
function orderedVideosRaw(item) {
  const videos = playable(item);''')
rep('''  const videos = orderedVideos(item);
  if (!videos.length) return null;
  const total = videos.reduce((sum, video) => sum + Math.max(1, video.durationSec), 0);
  let cursor = Math.floor(at / 1000) % total;
  for (let i = 0; i < videos.length; i++) {
    const length = Math.max(1, videos[i].durationSec);
    if (cursor < length) return { video: videos[i], offset: item.fromStart ? 0 : cursor, rest: videos.slice(i + 1).concat(videos.slice(0, i)) };
    cursor -= length;
  }
  return { video: videos[0], offset: 0, rest: videos.slice(1) };''','''  const videos = orderedVideos(item);
  if (!videos.length) return null;
  const total = orderTotal(item);
  let cursor = Math.floor(at / 1000) % total;
  const lazyRest = (show, i) => Object.defineProperty(show, "rest", { enumerable: true, get: () => videos.slice(i + 1).concat(videos.slice(0, i)) });
  for (let i = 0; i < videos.length; i++) {
    const length = Math.max(1, videos[i].durationSec);
    if (cursor < length) return lazyRest({ video: videos[i], offset: item.fromStart ? 0 : cursor, index: i }, i);
    cursor -= length;
  }
  return lazyRest({ video: videos[0], offset: 0, index: 0 }, 0);''')
# blocks: memo + 12 cells + use index from airing
rep('''function blocks(station) {
  const videos = orderedVideos(station);
  const on = airing(station, now);
  if (!videos.length || !on) return [];
  let index = Math.max(0, videos.findIndex((video) => video.id === on.video.id));''','''const GUIDE_CELLS = 12;
const blockCache = new Map();
function blocks(station) {
  const held = tuned && tuned.hold && tuned.stationId === station.id ? tuned.videoId : "";
  const videos = orderedVideos(station);
  const key = now + "|" + held + "|" + videos.length;
  const hit = blockCache.get(station.id);
  if (hit && hit.key === key && hit.videos === videos) return hit.row;
  const row = blocksRaw(station);
  blockCache.set(station.id, { key, videos, row });
  return row;
}
function blocksRaw(station) {
  const videos = orderedVideos(station);
  const on = airing(station, now);
  if (!videos.length || !on) return [];
  let index = Math.max(0, on.index || 0);''')
rep('''  while (row.length < 100) {''','''  while (row.length < GUIDE_CELLS) {''')
rep('''const next = blocks(station)[Math.min(focusSlot, 98) + 1];''','''const next = blocks(station)[Math.min(focusSlot, GUIDE_CELLS - 2) + 1];''')
# rows: only near rows get full cells
rep('''  const rows = state.stations.slice().sort((a, b) => a.number - b.number).map((station) => {
    const shows = blocks(station);''','''  const sortedRows = state.stations.slice().sort((a, b) => a.number - b.number);
  const activeRow = Math.max(0, sortedRows.findIndex((station) => item && station.id === item.id));
  const rows = sortedRows.map((station, rowIndex) => {
    const near = Math.abs(rowIndex - activeRow) <= 5;
    const allShows = blocks(station);
    const shows = near ? allShows : allShows.slice(0, 2);''')
# headerSlots: only near rows matter for width; keep but it's cached now. airMark only on change; delayed preview.
rep('''  mountPlayer(show);
  airMark();
  requestAnimationFrame(() => {''','''  const fromNav = navDraw;
  navDraw = false;
  clearTimeout(previewTimer);
  if (fromNav && !panel) {
    placeStage();
    previewTimer = setTimeout(() => { previewTimer = 0; const live = active(); mountPlayer(live ? currentShow(live) : null); warmAround(); }, 350);
  } else {
    mountPlayer(show);
  }
  airMark();
  requestAnimationFrame(() => {''')
rep('''  warmAround();
  const sheetPick''','''  if (!fromNav || panel) warmAround();
  const sheetPick''')
rep('''function airMark() {''','''let lastAirMark = null;
let previewTimer = 0;
function airMark() {''')
rep('''  window.JordanTube.airMark(station && station.logo ? station.logo : "", station ? station.number + "  " + station.name : "");''','''  const markLogo = station && station.logo ? station.logo : "";
  const markLabel = station ? station.number + "  " + station.name : "";
  const markKey = markLabel + "|" + markLogo.length + "|" + markLogo.slice(-64);
  if (markKey === lastAirMark) return;
  lastAirMark = markKey;
  window.JordanTube.airMark(markLogo, markLabel);''')
# tune: delayed save + coalesced draw
rep('''  held = null;
  save();
  draw();
}
window.onRemote''','''  held = null;
  saveSoon();
  drawSoon();
}
function refocus() {
  const item = active();
  const lineup = item ? blocks(item) : [];
  const row = document.querySelector(".row.on");
  if (!item || !row || !lineup.length) { drawSoon(); return; }
  const cells = row.querySelectorAll(".slot");
  if (focusSlot >= cells.length) { drawSoon(); return; }
  document.querySelectorAll(".slot.pick").forEach((cell) => cell.classList.remove("pick"));
  if (cells[focusSlot]) cells[focusSlot].classList.add("pick");
  const slot = lineup[Math.min(focusSlot, lineup.length - 1)];
  const next = lineup.length > 1 ? lineup[(Math.min(focusSlot, lineup.length - 1) + 1) % lineup.length] : null;
  const name = document.querySelector(".showname");
  const when = document.querySelector(".info .when");
  const after = document.querySelector(".info .next");
  if (name) name.textContent = slot && slot.video ? slot.video.title : "";
  if (when) when.textContent = slot ? clock(slot.start) + " – " + clock(slot.end) : "";
  if (after) after.textContent = next && next.video ? "NEXT: " + next.video.title : "";
  pinBlock();
  clearTimeout(previewTimer);
  previewTimer = setTimeout(() => { previewTimer = 0; mountPlayer(currentShow(active())); warmAround(); }, 350);
}
window.onRemote''')
rep('''    focusSlot = Math.max(0, focusSlot - 1);
    draw();
    return;''','''    focusSlot = Math.max(0, focusSlot - 1);
    refocus();
    return;''')
rep('''    focusSlot = Math.min(maxSlot, focusSlot + 1);
    draw();
    return;''','''    focusSlot = Math.min(maxSlot, focusSlot + 1);
    refocus();
    return;''')
# handOff should flush pending preview and save
rep('''function handOff() {
  const station = active();''','''function handOff() {
  clearTimeout(previewTimer);
  previewTimer = 0;
  const station = active();''')
open(p,'w').write(g)
print('ok', len(g))
