# v1.2 "no storage limit": lineup + logos persist to app files via window.JordanStore
# (tv.jordan.app.JtStore) instead of WebView localStorage (~5M char cap).
# Run from a decoded tree root parent (expects ./dec) after patch_guide.py + patch_smali.py.
import sys
def rep(s, old, new, count=1):
    n = s.count(old); assert n == count, (n, old[:120]); return s.replace(old, new)

# ---------- smali: MainActivity ----------
M = 'dec/smali_classes2/tv/jordan/app/MainActivity.smali'
m = open(M).read()
# 1) register JordanStore next to JordanTube
m = rep(m, '''    const-string v9, "JordanTube"

    invoke-virtual {v6, v8, v9}, Landroid/webkit/WebView;->addJavascriptInterface(Ljava/lang/Object;Ljava/lang/String;)V
''', '''    const-string v9, "JordanTube"

    invoke-virtual {v6, v8, v9}, Landroid/webkit/WebView;->addJavascriptInterface(Ljava/lang/Object;Ljava/lang/String;)V

    new-instance v8, Ltv/jordan/app/JtStore;

    invoke-direct {v8, p0}, Ltv/jordan/app/JtStore;-><init>(Landroid/content/Context;)V

    const-string v9, "JordanStore"

    invoke-virtual {v6, v8, v9}, Landroid/webkit/WebView;->addJavascriptInterface(Ljava/lang/Object;Ljava/lang/String;)V
''')
# 2) onActivityResult import: no 8MB read cap, and hand text to JS via the bridge
a = m.index('.method protected onActivityResult(')
e = m.index('.end method', a)
seg = m[a:e]
seg = rep(seg, '''    const v5, 0x7a1200

    if-ge v3, v5, :cond_5''', '''    const v5, 0x7ffffff0

    if-ge v3, v5, :cond_5''')
seg = rep(seg, '''    invoke-static {v3}, Lorg/json/JSONObject;->quote(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    .line 1824''', '''    sput-object v3, Ltv/jordan/app/JtStore;->pendingImport:Ljava/lang/String;

    const-string v3, ""

    .line 1824''')
seg = rep(seg, 'const-string v7, "window.applyImport&&window.applyImport("',
          'const-string v7, "window.applyImportPending&&window.applyImportPending("')
m = m[:a] + seg + m[e:]
open(M, 'w').write(m)

# ---------- guide.html ----------
P = 'dec/assets/guide.html'
g = open(P).read()
HELPERS = r'''function nativeStore() {
  const s = window.JordanStore;
  return s && s.available ? s : null;
}
function storeRead(name) {
  const s = nativeStore();
  if (!s) return null;
  const n = s.open(name);
  if (n < 0) { s.close(); return null; }
  const parts = [];
  let i = 0;
  while (i < n) {
    const part = s.chunk(i, 1048576);
    if (!part) break;
    parts.push(part);
    i += part.length;
  }
  s.close();
  if (i !== n) throw new Error("storage read was cut short");
  return parts.join("");
}
function storeWrite(name, text) {
  const s = nativeStore();
  if (!s) return false;
  if (!s.begin(name)) throw new Error("couldn't open app storage");
  for (let i = 0; i < text.length;) {
    let end = Math.min(text.length, i + 1048576);
    if (end < text.length) { const c = text.charCodeAt(end - 1); if (c >= 0xD800 && c <= 0xDBFF) end--; }
    if (!s.append(text.slice(i, end))) throw new Error("couldn't write app storage");
    i = end;
  }
  if (!s.commit()) throw new Error("couldn't finish saving");
  return true;
}
function lsGet(key) { try { return localStorage.getItem(key); } catch (e) { return null; } }
function lsSet(key, value) { try { localStorage.setItem(key, value); return true; } catch (e) { return false; } }
function lsDel(key) { try { localStorage.removeItem(key); } catch (e) { /* ignore */ } }
function parseLineup(text) {
  try {
    const saved = JSON.parse(text || "null");
    return saved && Array.isArray(saved.stations) && saved.stations.length ? saved : null;
  } catch (e) { return null; }
}
function load() {
  try {
    let fromFile = false;
    let saved = null;
    try { saved = parseLineup(storeRead("lineup")); fromFile = !!saved; } catch (e) { saved = null; }
    if (!saved) saved = parseLineup(lsGet(KEY));
    if (saved) {
      ensureSets(saved.stations);
      try {
        let logoText = null;
        try { logoText = storeRead("logos"); } catch (e) { logoText = null; }
        if (logoText == null) logoText = lsGet("jordan-tv-logos");
        const logos = JSON.parse(logoText || "{}") || {};
        saved.stations.forEach((item) => { if (!item.logo && logos[item.id]) item.logo = logos[item.id]; });
      } catch (e) { /* No saved logos. */ }
      // Older versions kept the lineup in localStorage: copy it into app storage once.
      if (!fromFile && nativeStore()) setTimeout(() => { try { save(); } catch (e) { /* Retried on next save. */ } }, 1500);
      return saved;
    }
  } catch (e) {}
  return {'''
g = rep(g, '''function load() {
  try {
    const saved = JSON.parse(localStorage.getItem(KEY) || "null");
    if (saved && Array.isArray(saved.stations) && saved.stations.length) {
      ensureSets(saved.stations);
      try {
        const logoText = localStorage.getItem("jordan-tv-logos");
        const logos = JSON.parse(logoText || "{}") || {};
        saved.stations.forEach((item) => { if (!item.logo && logos[item.id]) item.logo = logos[item.id]; });
      } catch (e) { /* No saved logos. */ }
      return saved;
    }
  } catch (e) {}
  return {''', HELPERS)
g = rep(g, '''  rememberSpot();
  localStorage.setItem(KEY, JSON.stringify(state, (k, v) => (k === "logo" ? undefined : v)));
  try {
    const logos = {};
    for (const item of state.stations) if (item.logo) logos[item.id] = item.logo;
    const text = JSON.stringify(logos);
    if (text !== savedLogos) { localStorage.setItem(LOGO_KEY, text); savedLogos = text; }
  } catch (e) { /* Logos are optional. */ }
''', '''  rememberSpot();
  // Returns "" when saved, else a short reason. Never throws.
  let problem = "";
  try {
    const text = JSON.stringify(state, (k, v) => (k === "logo" ? undefined : v));
    const logos = {};
    for (const item of state.stations) if (item.logo) logos[item.id] = item.logo;
    const logoText = JSON.stringify(logos);
    let stored = false;
    if (nativeStore()) {
      try {
        storeWrite("lineup", text);
        if (logoText !== savedLogos) { storeWrite("logos", logoText); savedLogos = logoText; }
        stored = true;
        if (!savedToFile) { lsDel(KEY); lsDel(LOGO_KEY); savedToFile = true; }
      } catch (e) { problem = String((e && e.message) || e); }
    }
    if (!stored) {
      if (lsSet(KEY, text)) {
        problem = "";
        if (logoText !== savedLogos && lsSet(LOGO_KEY, logoText)) savedLogos = logoText;
      } else if (!problem) problem = "the lineup is too big for browser storage";
    }
  } catch (e) { problem = String((e && e.message) || e); }
''')
g = rep(g, '''let savedLogos = null;
function save() {''', '''let savedLogos = null;
let savedToFile = false;
function save() {''')
# save() returns the problem string
g = rep(g, '''    try { window.JordanTube.remember(JSON.stringify(ordered().map((item) => ({ id: item.id, name: item.name, number: item.number })))); } catch (e) { /* The phone list refreshes next time. */ }
  }
}''', '''    try { window.JordanTube.remember(JSON.stringify(ordered().map((item) => ({ id: item.id, name: item.name, number: item.number })))); } catch (e) { /* The phone list refreshes next time. */ }
  }
  return problem;
}''')
# import: pull text through the bridge; always draw, show save errors
g = rep(g, '''window.applyImport = (text) => {''', '''window.applyImportPending = () => {
  let text = "";
  try { text = storeRead("import") || ""; } catch (e) { note = "Couldn't read that file."; draw(); return; }
  window.applyImport(text);
};
window.applyImport = (text) => {''')
g = rep(g, '''  note = "Imported " + clean.length + " channels.";
  save();
  draw();''', '''  let problem = "";
  try { problem = save() || ""; } catch (e) { problem = String((e && e.message) || e); }
  note = "Imported " + clean.length + " channels." + (problem ? " Couldn't save it (" + problem + "), so it will reset on restart." : "");
  draw();''')
g = rep(g, '''  localStorage.setItem("jordan-player", playerId);''', '''  lsSet("jordan-player", playerId);''')
open(P, 'w').write(g)
print('storage ok')
