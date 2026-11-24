SP='<svg class="sp"><use href="#sp"/></svg>'
def head(n): return f'<div class="eyebrow">{SP}ŞEFFAF RAPOR</div><div class="count">{n}</div>'
grid='<div class="grid"></div>'
S=[]
# ---------- 01 COVER ----------
words=[("Değişensiz",330),("Tramersiz",470),("Boyasız",610)]
w="".join(f'<div class="word" style="top:{y}px"><i>✓</i>{t}</div>' for t,y in words)
S.append(("01",f'''<div class="bgL"></div>{grid}
<div class="ghost" style="top:120px;left:-20px;font-size:300px">ŞEFFAF</div>
<div class="halo" style="left:470px;top:300px;width:700px;height:700px"></div>
<img class="person" src="ahmet_cut.png" style="left:400px;top:330px;width:880px">
<div class="fadeB"></div>
{head('KAYDIR →')}
{w}
<div style="position:absolute;left:84px;top:790px;font-weight:900;font-style:italic;font-size:92px;line-height:1;color:#A9C7F8">Ne demek?</div>
<div style="position:absolute;left:84px;top:905px;font-size:34px;font-weight:500;width:420px;opacity:.9">3 kelimeyi kısaca anlattık.</div>'''))
# ---------- 02 Değişensiz : scan ----------
calls=[("Kaput",250,330,"left"),("Ön Çamurluk",140,520,"left"),("Kapılar",640,560,"right"),("Tavan",620,260,"right")]
cl=""
for t,x,y,side in calls:
    if side=="left":
        cl+=f'<div class="dot" style="left:{x+260}px;top:{y+330}px"></div><div class="lead" style="left:{x+40}px;top:{y+330}px;width:220px"></div><div class="call" style="left:{x-170 if x>200 else 40}px;top:{y+300}px">{t}<b>Orijinal ✓</b></div>'
    else:
        cl+=f'<div class="dot" style="left:{x}px;top:{y+330}px"></div><div class="lead" style="left:{x+20}px;top:{y+330}px;width:180px"></div><div class="call" style="left:{x+200}px;top:{y+300}px">{t}<b>Orijinal ✓</b></div>'
S.append(("02",f'''<div class="bgL"></div>{grid}
{head('2/5')}
<div class="ttl" style="top:170px">01 · Değişensiz</div>
<div class="scanbox"><img src="x_scan.jpg"><div class="scanline"></div><i class="cn tl"></i><i class="cn tr"></i><i class="cn bl"></i><i class="cn br"></i><span class="scanlab">TARANIYOR · 100%</span></div>
{cl}
<div class="desc" style="top:1000px">Aracın hiçbir kaporta parçası değiştirilmemiş. Hepsi fabrikadan çıktığı gibi orijinal.</div>'''))
# ---------- 03 Tramersiz : phone ----------
S.append(("03",f'''<img class="full" src="x_dark.jpg" style="filter:blur(4px) saturate(.6);transform:scale(1.05)"><div class="wash3"></div>{grid}
<div class="ghost" style="top:250px;right:-40px;font-size:900px;line-height:.9">0</div>
{head('3/5')}
<div class="ttl" style="top:170px">02 · Tramersiz</div>
<div class="desc" style="top:300px;width:470px;right:auto">TRAMER'de hasar kaydı yok. Sigorta şirketlerine bildirilmiş bir kaza veya hasar ödemesi bulunmuyor.</div>
<div class="phone">
  <div class="notch"></div>
  <div class="scr">
    <div class="stop">{SP}<span>Hasar Sorgusu</span></div>
    <div class="plate">34 ••• •••</div>
    <div class="zero">0</div>
    <div class="zl">hasar kaydı</div>
    <div class="okbox">✓ Kayıt bulunamadı</div>
    <div class="srow"><span>Sigorta ödemesi</span><b>Yok</b></div>
    <div class="srow"><span>Toplam tutar</span><b>0 TL</b></div>
    <div class="ex">Örnek görsel</div>
  </div>
</div>
<div class="tag3"><i>✓</i>Tramersiz</div>'''))
# ---------- 04 Boyasız : paint points ----------
pts=[(260,560,"108"),(600,660,"112"),(830,520,"105"),(760,860,"110")]
pp="".join(f'<div class="pt" style="left:{x}px;top:{y}px"><span></span></div><div class="mchip" style="left:{x+30}px;top:{y-80}px">{v}<em>µm</em></div>' for x,y,v in pts)
S.append(("04",f'''<img class="full" src="v_22.jpg" style="object-position:50% 50%;filter:saturate(1.15) contrast(1.05)"><div class="wash4"></div>
{head('4/5')}
<div class="ttl" style="top:170px">03 · Boyasız</div>
<div class="desc" style="top:300px">Hiçbir parçada boya işlemi yapılmamış. Her panel tek tek ölçülür.</div>
{pp}
<div class="legend"><b>Tüm paneller</b><span>Fabrika boyası değerlerinde ✓</span><small>Örnek ölçüm</small></div>'''))
# ---------- 05 CTA : Ahmet ----------
S.append(("05",f'''<div class="bgL"></div>{grid}
<div class="ghost" style="top:150px;left:-30px;font-size:300px">KANIT</div>
<div class="halo" style="left:190px;top:330px;width:700px;height:700px"></div>
<img class="person" src="ahmet_cut.png" style="left:130px;top:420px;width:820px">
<div class="fadeB"></div>
{head('5/5')}
<div class="quote">Biz yazdığımızı<br>kanıtlıyoruz.</div>
<div class="name"><b>Ahmet</b><span>Cartopia</span></div>
<div class="chips" style="bottom:190px"><span class="pill solid">Detaylar için DM</span><span class="pill">Başakşehir · İstanbul</span></div>'''))

head_css=open('posts.html').read().split('</style>')[0]
css='''
.count{position:absolute;right:84px;top:92px;font-size:28px;font-weight:600;letter-spacing:.08em;z-index:8}
.eyebrow{z-index:8}
.sp{width:30px;height:30px}
.bgL{position:absolute;inset:0;background:radial-gradient(circle at 75% 40%,#3A66B0 0%,#22427F 40%,#152A57 75%,#0F2047 100%)}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.05) 2px,transparent 2px);background-size:90px 90px;-webkit-mask-image:radial-gradient(circle at 60% 45%,#000 20%,transparent 75%)}
.ghost{position:absolute;font-weight:900;font-style:italic;line-height:1;color:transparent;-webkit-text-stroke:3px rgba(169,199,248,.22);letter-spacing:-.02em;white-space:nowrap}
.halo{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(86,141,240,.75) 0%,rgba(86,141,240,.25) 45%,transparent 70%)}
.person{position:absolute;height:auto;filter:drop-shadow(0 0 2px rgba(255,255,255,.9)) drop-shadow(0 0 30px rgba(120,170,255,.55)) drop-shadow(0 40px 60px rgba(0,0,0,.45))}
.fadeB{position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(180deg,rgba(15,32,71,0),#0F2047 70%)}
.word{position:absolute;left:84px;display:flex;align-items:center;gap:22px;font-weight:900;font-style:italic;font-size:84px;line-height:1;text-shadow:0 6px 24px rgba(0,0,0,.35)}
.word i{flex:none;width:72px;height:72px;border-radius:50%;background:#fff;color:#2C5096;display:grid;place-items:center;font-style:normal;font-size:44px;box-shadow:0 0 0 8px rgba(255,255,255,.18)}
.ttl{position:absolute;left:84px;right:84px;font-weight:900;font-style:italic;font-size:100px;line-height:1;z-index:5}
.desc{position:absolute;left:84px;right:84px;font-size:36px;line-height:1.4;font-weight:500;opacity:.92;z-index:5}
.scanbox{position:absolute;left:84px;right:84px;top:330px;height:620px;border-radius:30px;overflow:hidden;border:2px solid rgba(169,199,248,.35)}
.scanbox img{width:100%;height:100%;object-fit:cover;filter:saturate(.7) brightness(.85)}
.scanbox:after{content:"";position:absolute;inset:0;background:linear-gradient(rgba(86,141,240,.12) 2px,transparent 2px) 0 0/100% 12px;mix-blend-mode:screen}
.scanline{position:absolute;left:0;right:0;top:56%;height:140px;background:linear-gradient(180deg,rgba(86,141,240,0),rgba(120,170,255,.45) 85%,#CFE0FF 100%);border-bottom:3px solid #E6EEFF;box-shadow:0 6px 30px #8FB4F6}
.cn{position:absolute;width:70px;height:70px;border:6px solid #fff}
.cn.tl{left:24px;top:24px;border-right:0;border-bottom:0;border-radius:18px 0 0 0}
.cn.tr{right:24px;top:24px;border-left:0;border-bottom:0;border-radius:0 18px 0 0}
.cn.bl{left:24px;bottom:24px;border-right:0;border-top:0;border-radius:0 0 0 18px}
.cn.br{right:24px;bottom:24px;border-left:0;border-top:0;border-radius:0 0 18px 0}
.scanlab{position:absolute;right:110px;top:40px;font-size:22px;font-weight:700;letter-spacing:.18em;background:rgba(14,30,68,.7);padding:8px 16px;border-radius:10px}
.dot{position:absolute;width:26px;height:26px;margin:-13px 0 0 -13px;border-radius:50%;background:#fff;box-shadow:0 0 0 10px rgba(255,255,255,.25),0 0 30px #8FB4F6;z-index:6}
.lead{position:absolute;height:3px;background:rgba(255,255,255,.85);z-index:5}
.call{position:absolute;z-index:6;background:rgba(255,255,255,.95);color:#0E1E44;border-radius:18px;padding:12px 20px;font-size:26px;font-weight:600;display:flex;flex-direction:column;line-height:1.2;box-shadow:0 12px 30px rgba(0,0,0,.3)}
.call b{color:#3E6AB3;font-size:24px}
.full{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.wash3{position:absolute;inset:0;background:linear-gradient(135deg,rgba(21,42,86,.92),rgba(36,68,132,.82))}
.phone{position:absolute;right:70px;top:300px;width:430px;height:860px;border-radius:64px;background:#0B1020;padding:18px;transform:rotate(6deg);box-shadow:0 40px 90px rgba(0,0,0,.55),0 0 0 3px rgba(169,199,248,.4);z-index:6}
.notch{position:absolute;left:50%;top:30px;transform:translateX(-50%);width:120px;height:32px;border-radius:16px;background:#000;z-index:2}
.scr{width:100%;height:100%;border-radius:48px;background:linear-gradient(180deg,#F3F7FF,#FFFFFF);color:#0E1E44;padding:90px 34px 30px;display:flex;flex-direction:column;align-items:stretch;gap:14px}
.stop{display:flex;align-items:center;gap:10px;font-size:26px;font-weight:700;color:#3E6AB3}
.stop span{color:#0E1E44}
.plate{align-self:flex-start;border:3px solid #0E1E44;border-radius:10px;padding:4px 14px;font-weight:700;font-size:26px;letter-spacing:.06em}
.zero{font-weight:900;font-style:italic;font-size:200px;line-height:.9;text-align:center;color:#3E6AB3;margin-top:10px}
.zl{text-align:center;font-size:26px;font-weight:600;margin-top:-6px}
.okbox{background:#E3EDFD;color:#2C5096;border-radius:16px;padding:14px;text-align:center;font-weight:700;font-size:26px}
.srow{display:flex;justify-content:space-between;font-size:24px;padding:10px 0;border-bottom:2px solid #EEF2FA}
.srow span{color:#596173}
.ex{text-align:center;font-size:18px;color:#8A93A6;margin-top:auto}
.tag3{position:absolute;left:84px;top:760px;display:flex;align-items:center;gap:18px;font-weight:900;font-style:italic;font-size:70px;z-index:5}
.tag3 i{width:70px;height:70px;border-radius:50%;background:#fff;color:#2C5096;display:grid;place-items:center;font-style:normal;font-size:40px}
.wash4{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,32,71,.95) 0%,rgba(21,42,86,.6) 32%,rgba(21,42,86,.15) 55%,rgba(15,32,71,.85) 88%)}
.pt{position:absolute;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;border:4px solid #fff;box-shadow:0 0 0 14px rgba(255,255,255,.18),0 0 40px #CFE0FF;z-index:5}
.pt span{position:absolute;inset:10px;border-radius:50%;background:#fff}
.mchip{position:absolute;z-index:6;background:#fff;color:#0E1E44;border-radius:16px;padding:8px 18px;font-size:38px;font-weight:800;box-shadow:0 12px 30px rgba(0,0,0,.35)}
.mchip em{font-style:normal;font-size:24px;margin-left:4px;color:#3E6AB3}
.legend{position:absolute;left:84px;right:84px;bottom:190px;background:rgba(255,255,255,.14);border:2px solid rgba(255,255,255,.35);backdrop-filter:blur(8px);border-radius:28px;padding:22px 30px;display:flex;align-items:center;gap:18px;font-size:30px;z-index:6}
.legend b{font-weight:800}
.legend small{margin-left:auto;font-size:20px;opacity:.7}
.quote{position:absolute;left:84px;right:84px;top:170px;font-weight:900;font-style:italic;font-size:96px;line-height:1;z-index:7;text-shadow:0 8px 30px rgba(0,0,0,.35)}
.qm{position:absolute;left:-10px;top:-150px;font-size:220px;color:#568DF0;opacity:.9}
.name{position:absolute;right:84px;top:880px;z-index:7;background:#fff;color:#0E1E44;border-radius:22px;padding:14px 26px;display:flex;flex-direction:column;line-height:1.15;box-shadow:0 16px 40px rgba(0,0,0,.35)}
.name b{font-size:38px;font-weight:800}
.name span{font-size:24px;color:#3E6AB3;font-weight:600}
.chips{z-index:7}
.pill.solid{background:#fff;color:#1A3060;border-color:#fff}
.line,.logo{z-index:9}
'''
out=[head_css+css+'</style></head><body>\n<svg width="0" height="0" style="position:absolute"><symbol id="sp" viewBox="0 0 24 24"><path d="M12 0C12.9 6.6 17.4 11.1 24 12 17.4 12.9 12.9 17.4 12 24 11.1 17.4 6.6 12.9 0 12 6.6 11.1 11.1 6.6 12 0Z" fill="currentColor"/></symbol></svg>']
for n,body in S:
    out.append(f'<div class="post" data-id="T{n}">{body}<div class="line"><svg style="color:#fff"><use href="#sp"/></svg></div><img class="logo" src="logo_white.png"></div>')
out.append('</body></html>')
open('slides3.html','w').write("\n".join(out))
