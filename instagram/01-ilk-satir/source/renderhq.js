// usage: node renderhq.js <dir> <html> <outPrefix> <css-selector> [startIndex]
const {chromium}=require('playwright');
(async()=>{
  const [d,html,prefix,sel,start]=process.argv.slice(2);
  const b=await chromium.launch();
  const p=await b.newPage({viewport:{width:1200,height:1500},deviceScaleFactor:2});
  await p.goto('file://'+d+'/'+html,{waitUntil:'networkidle'});
  await p.evaluate(()=>document.fonts.ready);
  const els=await p.$$(sel); let i=parseInt(start||'1');
  for(const e of els){await e.screenshot({path:`${d}/${prefix}_${String(i).padStart(2,'0')}.png`});i++;}
  await b.close();
})();
