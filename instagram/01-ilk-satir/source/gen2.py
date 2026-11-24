import html
E=html.escape
SPI='<svg class="sp"><use href="#sp"/></svg>'
NAVY='#0E1E44'; BLUE='#3E6AB3'; BRIGHT='#568DF0'
slides=[]
def head_R(n,tot=9):
    return f'<div class="eyebrow" style="color:{BLUE}">{SPI}<span style="color:{NAVY}">CARTOPIA REHBER</span></div><div class="count" style="color:{NAVY}">{n}/{tot}</div>'
def head_L(n,tot=5):
    return f'<div class="eyebrow">{SPI}ŞEFFAF RAPOR</div><div class="count">{n}/{tot}</div>'

# ================= R : 7 Altın Kural (light) =================
# R02 – rule 1: photo top, number badge, text below
slides.append(("R",2,f'''<div class="lightbg"></div>
<img class="ph" src="d_inspect.jpg" style="left:0;top:0;width:1080px;height:760px;border-radius:0 0 64px 64px;object-position:50% 40%">
<div class="fadeTop"></div>
{head_R(2)}
<div class="badge" style="left:84px;top:670px">1</div>
<h2 style="top:860px">Ekspertiz yaptırın</h2>
<p class="desc" style="top:960px">Bağımsız bir ekspertizde boya, değişen parça ve mekanik durumu kontrol ettirin.</p>'''))
# R03 – rule 2: full-bleed phone photo, navy side gradient
slides.append(("R",3,f'''<img class="ph" src="d_phone.jpg" style="left:380px;top:0;width:700px;height:1350px;object-position:8% 42%;-webkit-mask-image:linear-gradient(90deg,transparent 0%,#000 25%)">
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(21,42,86,.96) 0%,rgba(30,55,102,.9) 40%,rgba(44,80,150,.2) 66%,rgba(44,80,150,0) 100%)"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:420px;background:linear-gradient(180deg,rgba(243,247,255,0),#F3F7FF 64%)"></div>
<div class="eyebrow" style="color:#fff">{SPI}CARTOPIA REHBER</div><div class="count" style="color:#fff">3/9</div>
<div class="badge" style="left:84px;top:200px;background:#fff;color:{BLUE}">2</div>
<h2 style="top:430px;left:84px;width:560px;color:#fff;font-size:88px">TRAMER kaydını sorgulayın</h2>
<p class="desc" style="top:720px;left:84px;width:520px;color:#DCE7FB">Aracın hasar geçmişini plakayla sorgulayın. Kayıt varsa tutarına ve tarihine bakın.</p>
<div class="pill" style="position:absolute;left:84px;top:960px;background:#fff;color:{NAVY};border-color:#fff">Plaka → Hasar kaydı</div>'''))
# R04 – rule 3: odometer illustration
ticks=""
import math
for i in range(0,41):
    a=math.radians(200-i*5.5); r1=300; r2=300-(36 if i%5==0 else 18)
    x1=540+r1*math.cos(a); y1=640-r1*math.sin(a); x2=540+r2*math.cos(a); y2=640-r2*math.sin(a)
    ticks+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{NAVY if i%5==0 else BRIGHT}" stroke-width="{6 if i%5==0 else 3}" stroke-linecap="round"/>'
na=math.radians(200-27*5.5)
slides.append(("R",4,f'''<div class="lightbg" style="background:radial-gradient(circle at 50% 42%,#FFFFFF 0%,#DCE8FC 60%,#C3D7F8 100%)"></div>
{head_R(4)}
<svg width="1080" height="1350" style="position:absolute;inset:0">
<circle cx="540" cy="640" r="330" fill="#fff" opacity=".7"/>
<path d="M {540+300*math.cos(math.radians(200)):.1f} {640-300*math.sin(math.radians(200)):.1f} A 300 300 0 1 1 {540+300*math.cos(math.radians(-20)):.1f} {640-300*math.sin(math.radians(-20)):.1f}" fill="none" stroke="#E3ECFC" stroke-width="20"/>
{ticks}
<line x1="540" y1="640" x2="{540+250*math.cos(na):.1f}" y2="{640-250*math.sin(na):.1f}" stroke="{BLUE}" stroke-width="12" stroke-linecap="round"/>
<circle cx="540" cy="640" r="26" fill="{NAVY}"/>
</svg>
<div class="odo"><span>0</span><span>2</span><span>9</span><span>5</span><span>0</span><span>0</span><em>km</em></div>
<div class="badge" style="left:84px;top:180px">3</div>
<h2 style="top:930px;text-align:center;left:40px;right:40px;font-size:74px">Kilometreyi kontrol edin</h2>
<p class="desc" style="top:1030px;text-align:center;left:120px;right:120px">Göstergedeki kilometreyi servis ve muayene kayıtlarıyla karşılaştırın.</p>'''))
# R05 – rule 4: circle photo
slides.append(("R",5,f'''<div class="lightbg"></div>
<div style="position:absolute;left:160px;top:150px;width:760px;height:760px;border-radius:50%;background:conic-gradient({BRIGHT},{BLUE},{BRIGHT});padding:14px"><img src="d_care.jpg" style="width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:50% 40%;border:10px solid #fff"></div>
{head_R(5)}
<div class="badge" style="left:760px;top:760px;width:190px;height:190px;font-size:120px">4</div>
<h2 style="top:950px;text-align:center;left:40px;right:40px;font-size:74px">Servis geçmişine bakın</h2>
<p class="desc" style="top:1045px;text-align:center;left:110px;right:110px">Düzenli bakım yapılmış mı? Bakım faturalarını ve servis kayıtlarını isteyin.</p>'''))
# R06 – rule 5: full bleed photo, glass card
slides.append(("R",6,f'''<img class="ph" src="h_dash_hq.jpg" style="inset:0;width:100%;height:100%;object-position:22% 45%;filter:blur(2.2px) saturate(.85)">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(234,241,253,.35),rgba(169,199,248,.25))"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(234,241,253,.55) 0%,rgba(234,241,253,0) 25%,rgba(234,241,253,0) 45%,rgba(234,241,253,.85) 75%)"></div>
{head_R(6)}
<div class="glass" style="top:820px;height:330px"></div>
<div class="badge" style="left:110px;top:700px">5</div>
<h2 style="top:900px;left:130px;font-size:80px">Test sürüşü yapın</h2>
<p class="desc" style="top:995px;left:130px;right:130px;font-size:34px">Motor sesini, vites geçişlerini, frenleri ve direksiyonu mutlaka deneyin.</p>'''))
# R07 – rule 6: photo band + bar chart
bars=[("İlan A","1.420.000 TL",88,BLUE,""),("İlan B","1.390.000 TL",86,BLUE,""),("İlan C","1.450.000 TL",90,BLUE,""),("Şüpheli ilan","990.000 TL",60,"#fff","dashed")]
bh=""
for i,(lbl,val,w,col,st) in enumerate(bars):
    y=760+i*92
    style=f"background:{col};" if not st else f"background:repeating-linear-gradient(45deg,#fff 0 14px,#EEF3FD 14px 28px);border:3px dashed {BLUE};"
    bh+=f'<div style="position:absolute;left:84px;top:{y}px;font-size:26px;font-weight:600;color:{NAVY};width:220px">{lbl}</div><div style="position:absolute;left:300px;top:{y-6}px;width:{w*6.4:.0f}px;height:54px;border-radius:14px;{style}"></div><div style="position:absolute;left:{316}px;top:{y+4}px;font-size:26px;font-weight:700;color:{"#fff" if not st else NAVY}">{val}</div>'
slides.append(("R",7,f'''<div class="lightbg"></div>
<img class="ph" src="d_coins.jpg" style="left:60px;top:170px;width:960px;height:360px;border-radius:40px;object-position:50% 55%">
{head_R(7)}
<div class="badge" style="left:84px;top:470px">6</div>
<h2 style="top:570px;left:300px;font-size:72px">Piyasa fiyatını araştırın</h2>
{bh}
<p class="desc" style="top:1100px;font-size:28px">Benzer ilanlarla karşılaştırın, piyasanın çok altındaki fiyatlara dikkat edin. <span style="opacity:.6">(Örnek)</span></p>'''))
# R08 – rule 7: checklist + tilted photo
items=["Kimlik","Araç ruhsatı","Geçerli trafik sigortası","Güvenli ödeme"]
ck="".join(f'<div class="ck"><i>✓</i>{E(t)}</div>' for t in items)
slides.append(("R",8,f'''<div class="lightbg" style="background:linear-gradient(160deg,#FFFFFF,#D6E4FC)"></div>
<div style="position:absolute;right:-50px;top:160px;width:520px;height:640px;transform:rotate(5deg);border-radius:40px;overflow:hidden;box-shadow:0 30px 60px rgba(14,30,68,.25);border:12px solid #fff"><img src="d_keys.jpg" style="width:100%;height:100%;object-fit:cover;object-position:35% 50%"></div>
{head_R(8)}
<div class="badge" style="left:84px;top:200px">7</div>
<h2 style="top:420px;width:470px;font-size:80px">Satışı noterde yapın</h2>
<div style="position:absolute;left:84px;top:690px;display:flex;flex-direction:column;gap:20px">{ck}</div>
<p class="desc" style="top:1110px;font-size:30px">Devri noterde tamamlayın, ödemeyi güvenli bir yöntemle yapın.</p>'''))
# R09 – CTA
slides.append(("R",9,f'''<img class="ph" src="d_showroom.jpg" style="inset:0;width:100%;height:100%;object-position:40% 50%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(236,243,255,.95) 0%,rgba(236,243,255,.8) 45%,rgba(236,243,255,.25) 75%,rgba(236,243,255,.9) 100%)"></div>
{head_R(9)}
<h2 style="top:230px;font-size:104px;line-height:1">Cartopia'da<br><span style="color:{BLUE}">içiniz rahat.</span></h2>
<p class="desc" style="top:500px">Her aracımızın ekspertiz ve hasar bilgisi sizinle açıkça paylaşılır.</p>
<div class="chips" style="top:640px;bottom:auto"><span class="pill dk">Kaydet</span><span class="pill lt">Paylaş</span><span class="pill lt">DM'den sor</span></div>'''))

# ================= L : Şeffaf Rapor (dark) =================
# L02 – Değişensiz: car diagram + small photo
car=f'''<svg width="420" height="760" viewBox="0 0 420 760" style="position:absolute;left:560px;top:330px">
<rect x="40" y="20" width="340" height="720" rx="150" fill="rgba(255,255,255,.06)" stroke="#fff" stroke-width="6"/>
<path d="M70 210 Q210 150 350 210 L330 300 Q210 270 90 300 Z" fill="rgba(86,141,240,.35)" stroke="#fff" stroke-width="4"/>
<path d="M90 520 Q210 550 330 520 L350 590 Q210 640 70 590 Z" fill="rgba(86,141,240,.35)" stroke="#fff" stroke-width="4"/>
<rect x="95" y="310" width="230" height="200" rx="30" fill="rgba(86,141,240,.2)" stroke="#fff" stroke-width="4"/>
<line x1="40" y1="380" x2="95" y2="380" stroke="#fff" stroke-width="4"/><line x1="325" y1="380" x2="380" y2="380" stroke="#fff" stroke-width="4"/>
<line x1="40" y1="450" x2="95" y2="450" stroke="#fff" stroke-width="4"/><line x1="325" y1="450" x2="380" y2="450" stroke="#fff" stroke-width="4"/>
</svg>'''
parts=[("Kaput",400),("Çamurluklar",510),("Kapılar",620),("Tavan",730),("Bagaj",840)]
lab="".join(f'<div class="part" style="top:{y}px"><i>✓</i><b>{p}</b><span>Orijinal</span></div>' for p,y in parts)
slides.append(("L",2,f'''<div class="darkbg"></div>
<img class="ph" src="v_13.jpg" style="inset:0;width:100%;height:100%;object-position:50% 60%;opacity:.22;filter:grayscale(.4)">
{head_L(2)}
<div style="position:absolute;left:84px;top:190px;font-weight:900;font-style:italic;font-size:110px;line-height:1">01 · Değişensiz</div>
<div style="position:absolute;left:84px;top:330px;font-size:36px;font-weight:500;opacity:.92;width:900px">Aracın hiçbir kaporta parçası değiştirilmemiş, hepsi fabrikadan çıktığı gibi orijinal.</div>
<div style="position:absolute;left:0;top:0;transform:translate(-10px,140px) scale(.9);transform-origin:600px 400px">{car}</div>
<div style="position:absolute;left:84px;top:180px;width:460px">{lab}</div>'''))
# L03 – Tramersiz: blurred report bg + result card
slides.append(("L",3,f'''<img class="ph" src="d_report.jpg" style="inset:0;width:100%;height:100%;object-position:50% 30%;filter:blur(6px) saturate(.7);transform:scale(1.06)">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(21,42,86,.9),rgba(36,68,132,.82))"></div>
{head_L(3)}
<div style="position:absolute;left:84px;top:190px;font-weight:900;font-style:italic;font-size:110px;line-height:1">02 · Tramersiz</div>
<div style="position:absolute;left:84px;top:330px;font-size:36px;font-weight:500;opacity:.92;width:900px">TRAMER'de hasar kaydı yok. Sigorta şirketlerine bildirilmiş bir kaza veya hasar ödemesi bulunmuyor.</div>
<div class="rcard">
  <div class="rhead"><span>{SPI}</span>Hasar Kaydı Sorgusu<small>Örnek görsel</small></div>
  <div class="rrow"><span>Plaka</span><b>34 ••• •••</b></div>
  <div class="rrow"><span>Hasar kaydı</span><b class="ok">Yok ✓</b></div>
  <div class="rrow"><span>Sigorta ödemesi</span><b class="ok">Yok ✓</b></div>
  <div class="rrow"><span>Toplam tutar</span><b>0 TL</b></div>
</div>'''))
# L04 – Boyasız: close-up + paint gauge
slides.append(("L",4,f'''<img class="ph" src="v_22.jpg" style="inset:0;width:100%;height:100%;object-position:50% 45%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(21,42,86,.88) 0%,rgba(21,42,86,.35) 40%,rgba(21,42,86,.55) 65%,rgba(14,28,60,.95) 100%)"></div>
{head_L(4)}
<div style="position:absolute;left:84px;top:190px;font-weight:900;font-style:italic;font-size:110px;line-height:1">03 · Boyasız</div>
<div style="position:absolute;left:84px;top:330px;font-size:36px;font-weight:500;opacity:.92;width:880px">Hiçbir parçada boya işlemi yapılmamış. Her panel tek tek ölçülür.</div>
<div class="gauge">
  <div class="gscreen"><small>BOYA KALINLIĞI</small><b>112<em>µm</em></b><span>Fabrika boyası</span></div>
  <div class="gbar"><i style="left:38%"></i></div>
  <div class="glab"><span>İnce</span><span>Orijinal</span><span>Boyalı</span></div>
</div>
<div style="position:absolute;left:84px;bottom:180px;font-size:24px;opacity:.7">Örnek ölçüm</div>'''))
# L05 – CTA
slides.append(("L",5,f'''<img class="ph" src="v_21.jpg" style="inset:0;width:100%;height:100%;object-position:50% 25%">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(21,42,86,.75) 0%,rgba(21,42,86,.2) 35%,rgba(21,42,86,.6) 60%,rgba(14,28,60,.96) 100%)"></div>
{head_L(5)}
<div style="position:absolute;left:84px;top:690px;font-weight:900;font-style:italic;font-size:112px;line-height:.98">Biz yazdığımızı<br>kanıtlıyoruz.</div>
<div style="position:absolute;left:84px;top:940px;font-size:36px;font-weight:500;opacity:.92;width:900px">Her aracımızın ekspertiz bilgisi sizinle açıkça paylaşılır.</div>
<div class="chips"><span class="pill solid">Detaylar için DM</span><span class="pill">Başakşehir · İstanbul</span></div>'''))

head=open('posts.html').read().split('</style>')[0]
extra=f'''
.count{{position:absolute;right:84px;top:92px;font-size:28px;font-weight:600;letter-spacing:.08em;opacity:.9;z-index:5}}
.eyebrow{{z-index:5}}
.sp{{width:30px;height:30px}}
.lightbg{{position:absolute;inset:0;background:linear-gradient(180deg,#F3F7FF,#DCE8FC)}}
.darkbg{{position:absolute;inset:0;background:radial-gradient(circle at 80% 40%,#2F5596 0%,#1A3060 55%,#14264D 100%)}}
.ph{{position:absolute;object-fit:cover}}
.fadeTop{{position:absolute;left:0;right:0;top:0;height:220px;background:linear-gradient(180deg,rgba(243,247,255,.92),rgba(243,247,255,0))}}
h2{{position:absolute;left:84px;right:84px;font-weight:900;font-style:italic;font-size:88px;line-height:1.02;color:{NAVY}}}
.desc{{position:absolute;left:84px;right:84px;font-size:36px;line-height:1.4;font-weight:500;color:#2A3A5E}}
.badge{{position:absolute;width:170px;height:170px;border-radius:50%;background:linear-gradient(135deg,{BRIGHT},{BLUE});color:#fff;display:grid;place-items:center;font-weight:900;font-style:italic;font-size:110px;box-shadow:0 18px 40px rgba(62,106,179,.45);border:8px solid #fff}}
.numout{{position:absolute;font-weight:900;font-style:italic;font-size:400px;line-height:1;color:transparent;-webkit-text-stroke:6px #fff}}
.numghost{{position:absolute;right:40px;top:120px;font-weight:900;font-style:italic;font-size:560px;line-height:1;color:transparent;-webkit-text-stroke:8px rgba(255,255,255,.85)}}
.glass{{position:absolute;left:84px;right:84px;border-radius:40px;background:rgba(255,255,255,.82);backdrop-filter:blur(10px);box-shadow:0 20px 50px rgba(14,30,68,.18)}}
.odo{{position:absolute;left:50%;top:760px;transform:translateX(-50%);display:flex;gap:8px;align-items:center;background:{NAVY};padding:16px 22px;border-radius:22px}}
.odo span{{width:62px;height:84px;border-radius:10px;background:#fff;color:{NAVY};display:grid;place-items:center;font-size:56px;font-weight:700}}
.odo em{{font-style:normal;color:#fff;font-size:34px;font-weight:600;margin-left:10px}}
.ck{{display:flex;align-items:center;gap:18px;font-size:38px;font-weight:600;color:{NAVY}}}
.ck i{{width:56px;height:56px;border-radius:16px;background:{BLUE};color:#fff;display:grid;place-items:center;font-style:normal;font-size:34px}}
#R .pill.dk{{background:{NAVY};color:#fff;border-color:{NAVY}}}
#R .pill.lt{{background:rgba(255,255,255,.75);color:{NAVY};border-color:rgba(14,30,68,.25)}}
.pill.solid{{background:#fff;color:#1A3060;border-color:#fff}}
.part{{position:absolute;left:0;display:flex;align-items:center;gap:16px;font-size:34px}}
.part i{{width:50px;height:50px;border-radius:50%;background:{BRIGHT};display:grid;place-items:center;font-style:normal;font-size:28px;color:#fff}}
.part b{{font-weight:700;width:250px}}
.part span{{opacity:.75;font-size:28px}}
.rcard{{position:absolute;left:120px;right:120px;top:560px;background:#fff;border-radius:40px;padding:36px 48px;color:{NAVY};box-shadow:0 30px 70px rgba(0,0,0,.35)}}
.rhead{{display:flex;align-items:center;gap:14px;font-size:38px;font-weight:700;padding-bottom:22px;border-bottom:3px solid #E3EBF8;color:{NAVY}}}
.rhead span{{color:{BLUE}}}
.rhead small{{margin-left:auto;font-size:22px;font-weight:500;color:#8A93A6}}
.rrow{{display:flex;justify-content:space-between;padding:26px 0;border-bottom:2px solid #EEF2FA;font-size:36px}}
.rrow:last-child{{border-bottom:0}}
.rrow span{{color:#596173}}
.rrow b.ok{{color:{BLUE}}}
.gauge{{position:absolute;left:150px;right:150px;top:640px;background:rgba(255,255,255,.95);border-radius:44px;padding:40px;color:{NAVY};box-shadow:0 30px 70px rgba(0,0,0,.35)}}
.gscreen{{background:linear-gradient(135deg,#1E3766,#2C5096);border-radius:28px;color:#fff;padding:30px;text-align:center;display:flex;flex-direction:column;gap:4px}}
.gscreen small{{font-size:24px;letter-spacing:.14em;opacity:.8}}
.gscreen b{{font-size:120px;font-weight:800;line-height:1}}
.gscreen em{{font-style:normal;font-size:44px;margin-left:8px}}
.gscreen span{{font-size:30px;font-weight:600;color:#A9C7F8}}
.gbar{{position:relative;height:26px;border-radius:13px;margin-top:34px;background:linear-gradient(90deg,#A9C7F8,{BRIGHT} 30%,{BLUE} 50%,#1E3766 75%,#0E1E44)}}
.gbar i{{position:absolute;top:-12px;width:10px;height:50px;border-radius:5px;background:{NAVY};box-shadow:0 0 0 5px #fff}}
.glab{{display:flex;justify-content:space-between;font-size:26px;font-weight:600;margin-top:16px;color:#596173}}
'''
out=[head+extra+'</style></head><body>\n<svg width="0" height="0" style="position:absolute"><symbol id="sp" viewBox="0 0 24 24"><path d="M12 0C12.9 6.6 17.4 11.1 24 12 17.4 12.9 12.9 17.4 12 24 11.1 17.4 6.6 12.9 0 12 6.6 11.1 11.1 6.6 12 0Z" fill="currentColor"/></symbol></svg>']
for col,i,body in slides:
    sid=f"{col}{i:02d}"
    lc=NAVY if col=="R" else "#fff"; logo="logo_navy.png" if col=="R" else "logo_white.png"
    out.append(f'<div class="post s" id="{col}" data-id="{sid}">{body}<div class="line" style="z-index:6"><svg style="color:{lc}"><use href="#sp"/></svg></div><img class="logo" style="z-index:6" src="{logo}"></div>')
out.append('</body></html>')
open('slides.html','w').write("\n".join(out))
print(len(slides))
