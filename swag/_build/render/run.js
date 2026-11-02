const {chromium}=require('playwright');const fs=require('fs');
const REPO='/home/user/smoky-woods-assets/tumbler/';
const CFG=JSON.parse(process.argv[2]||'[["20","Black",false]]');
(async()=>{
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1400,height:1100},deviceScaleFactor:1});
 const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(/licatja\.github\.io\/smoky-woods-assets\/tumbler\//,r=>{
  const u=r.request().url();const f=u.split('/tumbler/')[1].split('?')[0];
  const hdr={'access-control-allow-origin':'*'};
  if(f==='logo-default.png') return r.fulfill({path:'/tmp/claude-0/s/rend/at-logo.png',headers:hdr,contentType:'image/png'});
  const path=REPO+f; if(!fs.existsSync(path)) return r.fulfill({status:404,headers:hdr});
  r.fulfill({path,headers:hdr,contentType:f.endsWith('.json')?'application/json':f.endsWith('.webp')?'image/webp':'image/png'});});
 await p.route(/fonts\.(googleapis|gstatic)\.com|cdnjs|jsdelivr|unpkg/,r=>r.abort());
 await p.goto('file:///tmp/claude-0/s/rend/designer.html');
 await p.waitForFunction(()=>window.__d,null,{timeout:15000});await p.waitForTimeout(2500);
 for(const [size,color,handle] of CFG){
  await p.evaluate(([size,color,handle])=>{const d=window.__d;const s=d.st();s.size=size;s.color=color;s.hcolor=color;s.handle=handle;s.example=true;d.fixColor();d.fitDefault();d.syncControls();d.rebuild();d.renderAll();},[size,color,handle]);
  await p.waitForTimeout(500);
  const url=await p.evaluate(()=>window.__d.viewCanvas.toDataURL('image/png'));
  fs.writeFileSync(`/tmp/claude-0/s/rend/out-${size}-${color.replace(/ /g,'')}-${handle?'h':'n'}.png`,Buffer.from(url.split(',')[1],'base64'));
 }
 console.log('errs',errs);await b.close();})();
