// Mock of tv.jordan.app.JtStore semantics backed by real files, plus page hosting.
import http from 'http'; import fs from 'fs'; import path from 'path';
const DIR = process.argv[2]; const PAGE = process.argv[3]; const PORT = Number(process.argv[4] || 9401);
fs.mkdirSync(DIR, { recursive: true });
let held = null, pending = null, wName = null, wFd = null; const calls = {};
const ok = n => /^[a-z0-9-]{1,40}$/.test(n || '');
const file = n => path.join(DIR, 'jt-' + n + '.json');
const MAX = 1 << 20;
const MOCK = `<script>(function(){
 function q(p, body){ const x=new XMLHttpRequest(); x.open(body==null?'GET':'POST','/s/'+p,false); x.send(body==null?null:body); return x.responseText; }
 window.JordanStore={ available:()=>true,
  open:n=>Number(q('open?name='+encodeURIComponent(n))), chunk:(s,m)=>q('chunk?start='+s+'&max='+m), close:()=>{q('close')},
  begin:n=>q('begin?name='+encodeURIComponent(n))==='true', append:p=>q('append',String(p))==='true', commit:()=>q('commit')==='true', remove:n=>q('remove?name='+n)==='true' };
 if (location.search.indexOf('nostore')>=0) delete window.JordanStore;
 window.JordanTube=new Proxy({}, {get:(t,k)=>{ if(k==='players') return ()=>'[]'; if(k==='player'||k==='archivePlayer') return ()=> 'guide'; return (...a)=>''; }});
})();</script>`;
http.createServer((req, res) => {
  const u = new URL(req.url, 'http://x'); const p = u.pathname; const qs = u.searchParams;
  const done = v => { res.writeHead(200, { 'content-type': 'text/plain; charset=utf-8' }); res.end(String(v)); };
  if (p === '/' || p === '/guide.html') { const html = fs.readFileSync(PAGE, 'utf8').replace('<head>', '<head>' + MOCK); res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' }); return res.end(html); }
  if (p === '/raw') { res.writeHead(200, { 'content-type': 'text/plain; charset=utf-8' }); return res.end(fs.readFileSync(qs.get('path'))); }
  if (p === '/calls') return done(JSON.stringify(calls));
  if (p === '/setpending') { pending = fs.readFileSync(qs.get('path'), 'utf8'); return done(pending.length); }
  const op = p.replace('/s/', ''); calls[op] = (calls[op] || 0) + 1;
  if (op === 'open') { const n = qs.get('name'); held = null; if (n === 'import') { held = pending; pending = null; } else if (ok(n) && fs.existsSync(file(n))) held = fs.readFileSync(file(n), 'utf8'); return done(held == null ? -1 : held.length); }
  if (op === 'chunk') { const s = Number(qs.get('start')); let m = Number(qs.get('max')); if (held == null || s < 0 || s >= held.length) return done(''); m = Math.max(1, Math.min(m <= 0 ? MAX : m, MAX)); let e = Math.min(held.length, s + m); const c = held.charCodeAt(e - 1); if (e < held.length && e - s > 1 && c >= 0xD800 && c <= 0xDBFF) e--; return done(held.slice(s, e)); }
  if (op === 'close') { held = null; return done(''); }
  if (op === 'begin') { const n = qs.get('name'); if (wFd) fs.closeSync(wFd); if (!ok(n)) return done(false); wName = n; wFd = fs.openSync(file(n) + '.tmp', 'w'); return done(true); }
  if (op === 'append') { const chunks = []; req.on('data', d => chunks.push(d)); req.on('end', () => { if (!wFd) return done(false); fs.writeSync(wFd, Buffer.concat(chunks)); done(true); }); return; }
  if (op === 'commit') { if (!wFd) return done(false); fs.fsyncSync(wFd); fs.closeSync(wFd); wFd = null; fs.renameSync(file(wName) + '.tmp', file(wName)); wName = null; return done(true); }
  if (op === 'remove') { const n = qs.get('name'); try { fs.unlinkSync(file(n)); return done(true); } catch (e) { return done(false); } }
  res.writeHead(404); res.end();
}).listen(PORT, () => console.log('listening ' + PORT));
