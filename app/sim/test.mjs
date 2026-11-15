import {spawn} from 'child_process'; import fs from 'fs';
const DIR='/tmp/jtstore', PORT=9401, BASE=`http://127.0.0.1:${PORT}/guide.html`;
fs.rmSync(DIR,{recursive:true,force:true}); fs.rmSync('/tmp/jtprof',{recursive:true,force:true});
const srv=spawn('node',['server.mjs',DIR,'/workspace/jordantv/v12/guide.built.html',String(PORT)],{stdio:'inherit'});
const chrome=spawn('google-chrome',['--headless=new','--no-sandbox','--disable-gpu','--user-data-dir=/tmp/jtprof','--remote-debugging-port=9334','--window-size=960,540','about:blank'],{stdio:'ignore'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let ws,id=0;const pend={}; const errors=[];
for(let i=0;i<60;i++){try{const l=await (await fetch('http://127.0.0.1:9334/json')).json();const p=l.find(x=>x.type==='page');if(p){ws=new WebSocket(p.webSocketDebuggerUrl);break;}}catch(e){}await sleep(200);}
await new Promise(r=>ws.onopen=r);
ws.onmessage=m=>{const d=JSON.parse(m.data);if(d.id&&pend[d.id]){pend[d.id](d);delete pend[d.id];} if(d.method==='Runtime.exceptionThrown') errors.push(d.params.exceptionDetails.exception?.description?.slice(0,200)||d.params.exceptionDetails.text);};
const send=(method,params={})=>new Promise(r=>{const i=++id;pend[i]=r;ws.send(JSON.stringify({id:i,method,params}));});
const ev=async e=>{const r=await send('Runtime.evaluate',{expression:e,awaitPromise:true,returnByValue:true}); if(r.result.exceptionDetails) return 'EXC '+JSON.stringify(r.result.exceptionDetails).slice(0,300); return r.result.result.value;};
await send('Page.enable');await send('Runtime.enable');
const go=async q=>{await send('Page.navigate',{url:BASE+(q||'')}); await sleep(3000);};
const summary=`JSON.stringify({stations:state.stations.length, videos:state.stations.reduce((a,s)=>a+s.videos.length,0), note, lsKey:(localStorage.getItem(KEY)||'').length, lsLogos:(localStorage.getItem('jordan-tv-logos')||'').length, firstTitle:state.stations[0].videos[0].title.slice(-12), logos:state.stations.filter(s=>s.logo).length})`;
const fsz=()=>Object.fromEntries(fs.existsSync(DIR)?fs.readdirSync(DIR).map(f=>[f,fs.statSync(DIR+'/'+f).size]):[]);
const out={};
const SLIM='/workspace/jordantv/r4/jordan-tv-import-full.before-slim.json', BIG='/workspace/jordantv/sim/nolimit/big3x.json';
// 1 control: no native store (old behaviour) -> quota error must not break import
await go('?nostore');
out.control=await ev(`(()=>{const x=new XMLHttpRequest();x.open('GET','/raw?path=${SLIM}',false);x.send();const t0=performance.now();window.applyImport(x.responseText);return JSON.stringify({ms:Math.round(performance.now()-t0), s:JSON.parse(${summary})});})()`);
await ev(`localStorage.clear()`);
// 2 before-slim through the bridge
for (const [label,f,expect] of [['slim',SLIM,32],['big3x',BIG,96]]) {
  await go();
  await (await fetch(`http://127.0.0.1:${PORT}/setpending?path=${f}`)).text();
  out[label+'_import']=await ev(`(()=>{const t0=performance.now();window.applyImportPending();const ms=Math.round(performance.now()-t0);const t1=performance.now();const p=save();return JSON.stringify({importMs:ms, resaveMs:Math.round(performance.now()-t1), resaveProblem:p, s:JSON.parse(${summary})});})()`);
  out[label+'_files']=fsz();
  await go();
  out[label+'_reload']=await ev(summary);
}
// 3 migration from localStorage (v1.1 -> v1.2 upgrade)
fs.rmSync(DIR,{recursive:true,force:true}); fs.mkdirSync(DIR);
await ev(`localStorage.clear()`);
await go('?nostore');
out.mig_seed=await ev(`(()=>{const x=new XMLHttpRequest();x.open('GET','/raw?path=/workspace/jordantv/jordan-tv-import-lite.json',false);x.send();window.applyImport(x.responseText);return ${summary};})()`);
await go(); await sleep(2500);
out.mig_after=await ev(summary); out.mig_files=fsz();
await go(); out.mig_reload=await ev(summary);
out.calls=await (await fetch(`http://127.0.0.1:${PORT}/calls`)).text();
out.pageErrors=errors;
console.log(JSON.stringify(out,null,1));
chrome.kill(); srv.kill(); process.exit(0);
