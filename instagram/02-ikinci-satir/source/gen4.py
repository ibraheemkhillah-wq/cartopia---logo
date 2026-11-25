NAVY='#0E1E44'; BLUE='#3E6AB3'; BRIGHT='#568DF0'; YEL='#FFE800'
SP='<svg class="sp"><use href="#sp"/></svg>'
def eb(label,count,dark=True):
    c='#fff' if dark else NAVY; s='#fff' if dark else BLUE
    return f'<div class="eyebrow" style="color:{s}">{SP}<span style="color:{c}">{label}</span></div><div class="count" style="color:{c}">{count}</div>'
S=[]  # (theme, id, body)
# ============ K : Kurumsal 100$ (dark) ============
K='KURUMSAL'
S.append(("K","K01",f'''<div class="bgK"></div><div class="grid"></div>
<img class="fadeimg" src="k_listings.jpg" style="top:560px;height:700px;object-position:50% 40%">
{eb(K,'KAYDIR →')}
<div class="ybadge" style="left:84px;top:170px">sahibinden.com</div>
<div style="position:absolute;left:84px;top:250px;font-size:44px;font-weight:600;opacity:.9">Kiralama şirketleri için</div>
<div style="position:absolute;left:84px;top:330px;font-weight:900;font-style:italic;font-size:96px;line-height:1">İlan başı</div>
<div class="mega" style="left:70px;top:420px">100$</div>
<div class="chips" style="bottom:200px"><span class="pill solid">Lisans yok</span><span class="pill">Abonelik yok</span><span class="pill">Araç şartı yok</span></div>'''))
probs=[("Lisans zorunluluğu","Sahibinden'de yayın lisansı almak uzun ve zahmetli."),("En az 10 araç","Belirli sayıda ilan verme zorunluluğu."),("Yüksek yıllık abonelik","Satış olmasa da her yıl ödeme.")]
pr="".join(f'<div class="prob"><i>✕</i><div><b>{a}</b><span>{b}</span></div></div>' for a,b in probs)
S.append(("K","K02",f'''<img class="full" src="k_stress.jpg" style="object-position:50% 20%;filter:saturate(.6)"><div class="washK"></div>
{eb(K,'2/7')}
<div class="ttl" style="top:170px">Satmak<br>neden bu kadar zor?</div>
<div style="position:absolute;left:84px;right:84px;top:560px;display:flex;flex-direction:column;gap:22px">{pr}</div>'''))
sol=["Lisans gerekmez","Yıllık abonelik yok","Minimum araç şartı yok","Hemen yayına başlayın"]
so="".join(f'<div class="ck2"><i>✓</i>{t}</div>' for t in sol)
S.append(("K","K03",f'''<div class="bgK"></div><div class="grid"></div>
<div class="halo" style="left:240px;top:180px;width:600px;height:600px"></div>
{eb(K,'3/7')}
<div class="lock"><span class="yS">sahibinden.com</span><span class="bar"></span><img src="logo_white.png"></div>
<div class="ttl" style="top:450px;text-align:center;font-size:84px;left:40px;right:40px">CarTopia Premium<br><span style="color:#A9C7F8">ile çözüm</span></div>
<div style="position:absolute;left:200px;right:160px;top:700px;display:flex;flex-direction:column;gap:22px">{so}</div>'''))
steps=[("Hesabınızı açıyoruz","Size özel kullanıcı hesabı"),("Sahibinden'e girin","Kendi hesabınızla"),("Araçlarınızı yayınlayın","İstediğiniz zaman"),("İlan yayında","CarTopia Premium sayfasında")]
st="".join(f'<div class="step" style="top:{330+i*190}px"><div class="snum">{i+1:02d}</div><div><b>{a}</b><span>{b}</span></div></div>' for i,(a,b) in enumerate(steps))
S.append(("K","K04",f'''<div class="bgK"></div><div class="grid"></div>
{eb(K,'4/7')}
<div class="ttl" style="top:170px">Nasıl çalışır?</div>
<div class="vline"></div>
{st}'''))
S.append(("K","K05",f'''<img class="full" src="k_handshake.jpg" style="object-position:40% 40%;filter:saturate(.7)"><div class="washK2"></div>
{eb(K,'5/7')}
<div class="ttl" style="top:170px">Kontrol<br>tamamen sizde</div>
<div class="lcard">
  <div class="lhead">İlan detayı <small>Örnek görsel</small></div>
  <div class="lrow"><span>İlandaki isim</span><b>Sizin personeliniz</b></div>
  <div class="lrow"><span>İletişim numarası</span><b>Sizin numaranız</b></div>
  <div class="lrow"><span>Müşteriyle görüşme</span><b>Doğrudan siz</b></div>
  <div class="lrow"><span>Satış süreci</span><b>Biz karışmıyoruz</b></div>
</div>'''))
S.append(("K","K06",f'''<div class="bgK"></div><div class="grid"></div>
<div class="halo" style="left:140px;top:250px;width:800px;height:800px"></div>
{eb(K,'6/7')}
<div style="position:absolute;left:0;right:0;top:200px;text-align:center;font-size:44px;font-weight:600;opacity:.9">Tek ücret</div>
<div class="mega" style="left:0;right:0;top:270px;text-align:center;font-size:400px">100$</div>
<div style="position:absolute;left:0;right:0;top:700px;text-align:center;font-weight:900;font-style:italic;font-size:70px">ilan başı</div>
<div class="row3c"><div><b>0$</b><span>yıllık abonelik</span></div><div><b>0</b><span>minimum araç</span></div><div><b>1</b><span>ilanla başlayın</span></div></div>
<div style="position:absolute;left:0;right:0;top:1090px;text-align:center;font-size:32px;opacity:.85">Sadece satmak istediğinizde ödeyin.</div>'''))
S.append(("K","K07",f'''<img class="full" src="k_typing.jpg" style="object-position:40% 50%"><div class="washK3"></div>
{eb(K,'7/7')}
<div class="ttl" style="top:560px;font-size:104px">Hemen<br>başlayalım.</div>
<div class="desc" style="top:800px">İlanınızı doğru yazmayı ve aracınızın güçlü yönlerini öne çıkarmayı da birlikte yapıyoruz.</div>
<div class="chips" style="bottom:200px"><span class="pill solid">Detaylar için DM</span><span class="pill">WhatsApp: +90 555 575 50 80</span></div>'''))

# ============ C : Karşılaştırma (light) ============
C='KARŞILAŞTIRMA'
S.append(("C","C01",f'''<div class="bgC"></div>
{eb(C,'KAYDIR →')}
<div class="ttl" style="top:160px;font-size:104px">Arona mı,<br>Passat mı?</div>
<div class="duo" style="left:50px;top:520px;transform:rotate(-4deg)"><img src="c_arona.jpg" style="object-position:45% 60%"><span>2024 Seat Arona</span></div>
<div class="duo" style="right:50px;top:560px;transform:rotate(4deg)"><img src="c_passat.jpg" style="object-position:60% 60%"><span>2016 VW Passat</span></div>
<div class="vs" style="left:470px;top:760px">VS</div>
<div class="chips" style="bottom:200px;justify-content:space-between"><span class="pill price">1.550.000 TL</span><span class="pill price">1.400.000 TL</span></div>'''))
for i,(img,name,yr,tags,pos) in enumerate([("c_arona.jpg","Seat Arona","2024",["1.0 EcoTSI Xperience","Benzin · Otomatik","Hatasız · Boyasız"],"45% 60%"),("c_passat.jpg","VW Passat","2016",["1.6 TDI BMT Comfortline","Dizel · Otomatik","İçi bej · Tertemiz"],"60% 60%")]):
    tg="".join(f'<span class="pill">{t}</span>' for t in tags)
    S.append(("C",f"C0{i+2}",f'''<div class="bgC"></div>
<img class="carcard" src="{img}" style="object-position:{pos}">
{eb(C,f'{i+2}/6')}
<div class="corner">{"A" if i==0 else "B"}</div>
<div style="position:absolute;left:84px;top:800px;font-size:40px;font-weight:700;opacity:.9">{yr}</div><div class="ttl" style="top:855px;font-size:96px">{name}</div>
<div class="chips" style="bottom:200px;flex-wrap:wrap">{tg}</div>'''))
rows=[("Model yılı","2024","2016"),("Kasa tipi","SUV","Sedan"),("Yakıt","Benzin","Dizel"),("Vites","Otomatik","Otomatik"),("Durum","Hatasız · Boyasız","Tertemiz · Düşük km"),("Fiyat","1.550.000 TL","1.400.000 TL")]
tb="".join(f'<div class="crow"><b>{a}</b><span>{b}</span><span>{c}</span></div>' for a,b,c in rows)
S.append(("C","C04",f'''<div class="bgC"></div>
{eb(C,'4/6')}
<div class="ttl" style="top:170px">Yan yana</div>
<div class="ctable"><div class="chead"><span></span><span>Arona</span><span>Passat</span></div>{tb}</div>'''))
S.append(("C","C05",f'''<div class="bgC"></div>
{eb(C,'5/6')}
<div class="ttl" style="top:170px">Kime uygun?</div>
<div class="who" style="left:84px"><img src="c_arona.jpg" style="object-position:45% 60%"><b>Arona</b><ul><li>Şehir içi kullanım</li><li>Yüksek sürüş pozisyonu</li><li>Yeni model arayanlar</li></ul></div>
<div class="who" style="right:84px"><img src="c_passat.jpg" style="object-position:60% 60%"><b>Passat</b><ul><li>Uzun yol</li><li>Geniş iç hacim</li><li>Dizel ekonomisi</li></ul></div>'''))
S.append(("C","C06",f'''<div class="bgC"></div>
<div class="ghost" style="left:30px;top:520px;font-size:420px">A / B</div>
{eb(C,'6/6')}
<div class="ttl" style="top:200px;font-size:110px">Siz hangisini<br>seçerdiniz?</div>
<div class="vote" style="top:600px"><span>A</span>Arona</div>
<div class="vote" style="top:760px"><span>B</span>Passat</div>
<div class="desc" style="top:950px">Yorumlara A veya B yazın. İki araç da vitrinimizde, test sürüşü için DM'den yazın.</div>'''))

# ============ S : Araba Sözlüğü – Hibrit (lighter) ============
L='ARABA SÖZLÜĞÜ'
S.append(("S","S01",f'''<div class="bgS"></div>
<img class="fadeimg" src="h_34_hq.jpg" style="top:470px;height:780px;object-position:40% 50%">
<div class="ghostN" style="right:40px;top:70px">H</div>
{eb(L,'KAYDIR →',dark=False)}
<h1 class="nv" style="top:170px;font-size:104px">Hibrit<br><span style="color:{BLUE}">nasıl çalışır?</span></h1>
<div class="chips" style="bottom:200px"><span class="pill wt">Kaydet, işine yarayacak</span></div>'''))
S.append(("S","S02",f'''<div class="bgS"></div>
{eb(L,'2/6',dark=False)}
<h1 class="nv" style="top:170px;font-size:96px">Hibrit =</h1>
<div class="eq" style="top:400px">
  <div class="eqc"><svg viewBox="0 0 64 64"><rect x="10" y="20" width="36" height="28" rx="4" fill="none" stroke="currentColor" stroke-width="4"/><path d="M46 28h8v12h-8M18 20v-6h20v6M10 34H4" fill="none" stroke="currentColor" stroke-width="4"/></svg><b>Benzinli motor</b></div>
  <div class="eqp">+</div>
  <div class="eqc"><svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="20" fill="none" stroke="currentColor" stroke-width="4"/><path d="M34 16l-10 18h10l-4 14 12-20H32z" fill="currentColor"/></svg><b>Elektrik motoru</b></div>
</div>
<div class="bat" style="top:840px"><svg viewBox="0 0 64 32"><rect x="2" y="4" width="54" height="24" rx="5" fill="none" stroke="currentColor" stroke-width="4"/><rect x="58" y="11" width="4" height="10" rx="2" fill="currentColor"/><rect x="8" y="10" width="30" height="12" rx="2" fill="currentColor"/></svg><span>+ batarya</span></div>
<p class="dsc" style="top:1010px">İki motor birlikte çalışır. Araç, duruma göre hangisinin kullanılacağına kendisi karar verir.</p>'''))
modes=[("Elektrik modu","Düşük hız ve şehir trafiği","Sadece elektrik motoru, sessiz ve yakıtsız."),("Hibrit mod","Hızlanma ve ara hızlar","Benzinli motor elektrik üretir, tekerleri elektrik motoru çevirir."),("Benzinli mod","Sabit yüksek hız","Uzun yolda benzinli motor doğrudan devreye girer.")]
md="".join(f'<div class="mode"><div class="mi">{i+1}</div><div><b>{a}</b><em>{b}</em><span>{c}</span></div></div>' for i,(a,b,c) in enumerate(modes))
S.append(("S","S03",f'''<div class="bgS"></div>
{eb(L,'3/6',dark=False)}
<h1 class="nv" style="top:170px;font-size:92px">3 sürüş modu</h1>
<div style="position:absolute;left:84px;right:84px;top:380px;display:flex;flex-direction:column;gap:26px">{md}</div>'''))
S.append(("S","S04",f'''<div class="bgS"></div>
<img class="ph" src="h_front_hq.jpg" style="left:84px;right:84px;top:170px;width:912px;height:470px;border-radius:40px;object-position:50% 55%">
{eb(L,'4/6',dark=False)}
<div class="regen" style="top:600px"><svg viewBox="0 0 120 120"><path d="M60 14a46 46 0 1 1-40 23" fill="none" stroke="{BLUE}" stroke-width="10" stroke-linecap="round"/><path d="M8 30l14 10 8-16" fill="none" stroke="{BLUE}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M64 34l-16 30h14l-6 22 20-32H62z" fill="{NAVY}"/></svg></div>
<h1 class="nv" style="top:820px;font-size:84px;text-align:center;left:40px;right:40px">Fren = şarj</h1>
<p class="dsc" style="top:930px;text-align:center;left:110px;right:110px">Yavaşlarken ve fren yaparken boşa giden enerji bataryaya geri döner.</p>'''))
S.append(("S","S05",f'''<div class="bgS"></div>
{eb(L,'5/6',dark=False)}
<div class="plug"><svg viewBox="0 0 120 120"><path d="M44 18v26M76 18v26M34 44h52v18a26 26 0 0 1-52 0zM60 88v20" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/><path d="M18 18l84 84" stroke="#E5484D" stroke-width="9" stroke-linecap="round"/></svg></div>
<h1 class="nv" style="top:560px;font-size:90px">Fişe takmanıza<br><span style="color:{BLUE}">gerek yok.</span></h1>
<div class="cmp2" style="top:820px"><div><b>Hibrit</b><span>Kendi kendini şarj eder</span></div><div><b>Plug-in hibrit</b><span>Prize takılarak da şarj edilir</span></div></div>'''))
S.append(("S","S06",f'''<div class="bgS"></div>
<img class="fadeimg" src="h_34b_hq.jpg" style="top:430px;height:760px;object-position:50% 50%">
{eb(L,'6/6',dark=False)}
<div class="ybadge" style="left:84px;top:170px;background:{NAVY};color:#fff">Vitrinimizde</div>
<h1 class="nv" style="top:250px;font-size:92px">2023 Honda ZR-V<br><span style="color:{BLUE}">Hibrit</span></h1>
<div class="chips" style="bottom:200px"><span class="pill dk">2.970.000 TL</span><span class="pill wt">29.500 km</span><span class="pill wt">DM'den yazın</span></div>'''))

head='''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,800;1,900&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0}
body{background:#222;font-family:Poppins,sans-serif;display:flex;gap:40px;padding:40px;flex-wrap:wrap}
.post{width:1080px;height:1350px;position:relative;overflow:hidden;color:#fff}
.post.S{color:#0E1E44}
.eyebrow{position:absolute;left:84px;top:92px;display:flex;align-items:center;gap:14px;font-weight:600;font-size:28px;letter-spacing:.16em;z-index:8}
.count{position:absolute;right:84px;top:92px;font-size:28px;font-weight:600;letter-spacing:.08em;z-index:8}
.sp{width:30px;height:30px}
.line{position:absolute;left:0;right:0;bottom:150px;height:3px;background:rgba(255,255,255,.9);z-index:9}
.S .line{background:rgba(14,30,68,.75)}
.line svg{position:absolute;left:50%;top:50%;width:46px;height:46px;transform:translate(-50%,-50%)}
.logo{position:absolute;left:50%;bottom:56px;transform:translateX(-50%);height:62px;z-index:9}
.bgK{position:absolute;inset:0;background:radial-gradient(circle at 75% 40%,#3A66B0 0%,#22427F 40%,#152A57 75%,#0F2047 100%)}
.bgC{position:absolute;inset:0;background:linear-gradient(90deg,#2E5AA6,#4F86E6)}
.bgS{position:absolute;inset:0;background:linear-gradient(90deg,#9DBEF7,#E3EDFD)}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.05) 2px,transparent 2px);background-size:90px 90px;-webkit-mask-image:radial-gradient(circle at 60% 45%,#000 20%,transparent 75%)}
.halo{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(86,141,240,.7) 0%,rgba(86,141,240,.2) 45%,transparent 70%)}
.fadeimg{position:absolute;left:0;width:1080px;object-fit:cover;-webkit-mask-image:linear-gradient(180deg,transparent 0%,#000 22%,#000 80%,transparent 100%)}
.full{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ph{position:absolute;object-fit:cover}
.washK{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,32,71,.95) 0%,rgba(21,42,86,.82) 40%,rgba(15,32,71,.96) 100%)}
.washK2{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,32,71,.94) 0%,rgba(21,42,86,.6) 45%,rgba(15,32,71,.95) 100%)}
.washK3{position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,32,71,.55) 0%,rgba(21,42,86,.75) 40%,rgba(15,32,71,.97) 75%)}
.ttl{position:absolute;left:84px;right:84px;font-weight:900;font-style:italic;font-size:96px;line-height:1;z-index:5}
h1.nv{position:absolute;left:84px;right:84px;font-weight:900;font-style:italic;line-height:1;color:#0E1E44;z-index:5}
.desc{position:absolute;left:84px;right:84px;font-size:36px;line-height:1.4;font-weight:500;opacity:.92;z-index:5}
.dsc{position:absolute;left:84px;right:84px;font-size:36px;line-height:1.4;font-weight:500;color:#2A3A5E}
.mega{position:absolute;font-weight:900;font-style:italic;font-size:300px;line-height:1;letter-spacing:-.03em;background:linear-gradient(180deg,#FFFFFF 40%,#A9C7F8);-webkit-background-clip:text;color:transparent;text-shadow:0 20px 60px rgba(0,0,0,.25);z-index:5}
.ybadge{position:absolute;padding:10px 22px;border-radius:14px;background:#FFE800;color:#1A1A1A;font-weight:800;font-size:28px;z-index:6}
.chips{position:absolute;left:84px;right:84px;bottom:200px;display:flex;flex-wrap:wrap;gap:16px;z-index:7}
.pill{display:inline-flex;align-items:center;padding:14px 26px;border-radius:999px;font-size:30px;font-weight:600;background:rgba(255,255,255,.16);border:2px solid rgba(255,255,255,.55);backdrop-filter:blur(6px);color:#fff}
.pill.solid{background:#fff;color:#1A3060;border-color:#fff}
.pill.price{background:#fff;color:#1A3060;border-color:#fff;font-weight:800;font-size:36px}
.pill.wt{background:#fff;color:#0E1E44;border-color:#fff}
.pill.dk{background:#0E1E44;color:#fff;border-color:#0E1E44;font-weight:800}
.prob{display:flex;gap:26px;align-items:flex-start;background:rgba(255,255,255,.1);border:2px solid rgba(255,255,255,.2);border-radius:28px;padding:28px 32px;backdrop-filter:blur(6px)}
.prob i{flex:none;width:64px;height:64px;border-radius:50%;background:#E5484D;display:grid;place-items:center;font-style:normal;font-size:34px;font-weight:800}
.prob b{display:block;font-size:40px;font-weight:800}
.prob span{display:block;font-size:30px;opacity:.85;margin-top:4px}
.lock{position:absolute;left:0;right:0;top:250px;display:flex;align-items:center;justify-content:center;gap:34px;z-index:5}
.lock .yS{background:#FFE800;color:#1A1A1A;font-weight:800;font-size:44px;padding:16px 26px;border-radius:18px}
.lock .bar{width:3px;height:110px;background:#fff;opacity:.8}
.lock img{height:74px}
.ck2{display:flex;align-items:center;gap:22px;font-size:42px;font-weight:700}
.ck2 i{flex:none;width:66px;height:66px;border-radius:50%;background:#fff;color:#2C5096;display:grid;place-items:center;font-style:normal;font-size:38px}
.vline{position:absolute;left:150px;top:370px;width:4px;height:600px;background:linear-gradient(180deg,#568DF0,rgba(86,141,240,.2))}
.step{position:absolute;left:84px;right:84px;display:flex;align-items:center;gap:36px}
.snum{flex:none;width:136px;height:136px;border-radius:50%;background:linear-gradient(135deg,#568DF0,#3E6AB3);display:grid;place-items:center;font-weight:900;font-style:italic;font-size:56px;border:6px solid #0F2047;box-shadow:0 0 0 3px #568DF0}
.step b{display:block;font-size:44px;font-weight:800}
.step span{display:block;font-size:30px;opacity:.8}
.lcard{position:absolute;left:84px;right:84px;top:540px;background:#fff;color:#0E1E44;border-radius:40px;padding:30px 44px;box-shadow:0 30px 70px rgba(0,0,0,.4)}
.lhead{font-size:36px;font-weight:800;padding-bottom:18px;border-bottom:3px solid #E3EBF8;display:flex;align-items:center}
.lhead small{margin-left:auto;font-size:22px;font-weight:500;color:#8A93A6}
.lrow{display:flex;justify-content:space-between;padding:24px 0;border-bottom:2px solid #EEF2FA;font-size:32px}
.lrow:last-child{border-bottom:0}
.lrow span{color:#596173}
.lrow b{color:#3E6AB3}
.row3c{position:absolute;left:84px;right:84px;top:860px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.row3c div{background:rgba(255,255,255,.12);border:2px solid rgba(255,255,255,.25);border-radius:28px;padding:24px;text-align:center;display:flex;flex-direction:column}
.row3c b{font-size:64px;font-weight:900;font-style:italic}
.row3c span{font-size:26px;opacity:.85}
.duo{position:absolute;width:470px;height:520px;border-radius:36px;overflow:hidden;border:10px solid #fff;box-shadow:0 30px 60px rgba(14,30,68,.4);background:#fff}
.duo img{width:100%;height:440px;object-fit:cover;display:block}
.duo span{display:block;text-align:center;color:#0E1E44;font-weight:800;font-size:30px;padding-top:16px}
.vs{position:absolute;width:140px;height:140px;border-radius:50%;background:#0E1E44;color:#fff;display:grid;place-items:center;font-weight:900;font-style:italic;font-size:56px;border:8px solid #fff;z-index:6;box-shadow:0 0 0 10px rgba(255,255,255,.25)}
.carcard{position:absolute;left:84px;top:170px;width:912px;height:590px;border-radius:44px;object-fit:cover;box-shadow:0 30px 70px rgba(14,30,68,.35);border:8px solid rgba(255,255,255,.9)}
.corner{position:absolute;right:120px;top:120px;width:130px;height:130px;border-radius:50%;background:#0E1E44;color:#fff;display:grid;place-items:center;font-weight:900;font-style:italic;font-size:70px;border:8px solid #fff;z-index:6}
.ctable{position:absolute;left:84px;right:84px;top:330px;background:#fff;border-radius:40px;overflow:hidden;color:#0E1E44;box-shadow:0 30px 70px rgba(14,30,68,.35)}
.chead,.crow{display:grid;grid-template-columns:1.1fr 1fr 1fr;align-items:center}
.chead{background:#0E1E44;color:#fff;font-weight:800;font-size:34px;padding:26px 36px}
.chead span:nth-child(2),.chead span:nth-child(3){text-align:center}
.crow{padding:26px 36px;border-bottom:2px solid #EEF2FA;font-size:30px}
.crow:nth-child(odd){background:#F5F8FE}
.crow b{color:#596173;font-weight:600}
.crow span{text-align:center;font-weight:700}
.who{position:absolute;top:330px;width:440px;background:#fff;color:#0E1E44;border-radius:40px;overflow:hidden;box-shadow:0 30px 70px rgba(14,30,68,.35)}
.who img{width:100%;height:300px;object-fit:cover;display:block}
.who b{display:block;font-size:48px;font-weight:900;font-style:italic;padding:24px 32px 6px}
.who ul{list-style:none;padding:0 32px 32px;display:flex;flex-direction:column;gap:14px}
.who li{font-size:30px;font-weight:600;padding-left:44px;position:relative}
.who li:before{content:"✓";position:absolute;left:0;top:0;width:32px;height:32px;border-radius:50%;background:#3E6AB3;color:#fff;font-size:20px;display:grid;place-items:center}
.ghost{position:absolute;font-weight:900;font-style:italic;line-height:1;color:transparent;-webkit-text-stroke:3px rgba(255,255,255,.22);white-space:nowrap}
.ghostN{position:absolute;font-weight:900;font-style:italic;font-size:460px;line-height:1;color:rgba(62,106,179,.16)}
.vote{position:absolute;left:84px;right:84px;height:120px;border-radius:30px;background:#fff;color:#0E1E44;display:flex;align-items:center;gap:30px;padding:0 24px;font-size:48px;font-weight:800;box-shadow:0 20px 50px rgba(14,30,68,.3)}
.vote span{width:84px;height:84px;border-radius:22px;background:#3E6AB3;color:#fff;display:grid;place-items:center;font-style:italic;font-weight:900}
.eq{position:absolute;left:84px;right:84px;display:flex;align-items:center;justify-content:space-between}
.eqc{width:380px;height:380px;border-radius:44px;background:#fff;box-shadow:0 30px 60px rgba(14,30,68,.18);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;color:#3E6AB3}
.eqc svg{width:170px;height:170px}
.eqc b{font-size:36px;font-weight:800;color:#0E1E44}
.eqp{font-size:120px;font-weight:900;color:#3E6AB3}
.bat{position:absolute;left:0;right:0;display:flex;align-items:center;justify-content:center;gap:24px;color:#0E1E44;font-size:44px;font-weight:800}
.bat svg{width:150px;height:76px;color:#3E6AB3}
.mode{display:flex;gap:30px;align-items:flex-start;background:#fff;border-radius:36px;padding:34px 36px;box-shadow:0 20px 50px rgba(14,30,68,.14)}
.mi{flex:none;width:96px;height:96px;border-radius:50%;background:linear-gradient(135deg,#568DF0,#3E6AB3);color:#fff;display:grid;place-items:center;font-weight:900;font-style:italic;font-size:50px}
.mode b{display:block;font-size:44px;font-weight:900;font-style:italic}
.mode em{display:block;font-style:normal;color:#3E6AB3;font-weight:700;font-size:28px;margin:4px 0 8px}
.mode span{display:block;font-size:28px;color:#2A3A5E;line-height:1.35}
.regen{position:absolute;left:50%;transform:translateX(-50%);width:220px;height:220px;border-radius:50%;background:#fff;box-shadow:0 20px 50px rgba(14,30,68,.25);display:grid;place-items:center;z-index:5}
.regen svg{width:150px;height:150px}
.plug{position:absolute;left:50%;top:180px;transform:translateX(-50%);width:330px;height:330px;border-radius:50%;background:#fff;box-shadow:0 30px 60px rgba(14,30,68,.18);display:grid;place-items:center}
.plug svg{width:210px;height:210px}
.cmp2{position:absolute;left:84px;right:84px;display:grid;grid-template-columns:1fr 1fr;gap:20px}
.cmp2 div{background:#fff;border-radius:32px;padding:30px;display:flex;flex-direction:column;gap:8px;box-shadow:0 20px 50px rgba(14,30,68,.14)}
.cmp2 div:first-child{background:#0E1E44;color:#fff}
.cmp2 b{font-size:40px;font-weight:900;font-style:italic}
.cmp2 span{font-size:28px;opacity:.85}
</style></head><body>
<svg width="0" height="0" style="position:absolute"><symbol id="sp" viewBox="0 0 24 24"><path d="M12 0C12.9 6.6 17.4 11.1 24 12 17.4 12.9 12.9 17.4 12 24 11.1 17.4 6.6 12.9 0 12 6.6 11.1 11.1 6.6 12 0Z" fill="currentColor"/></symbol></svg>'''
out=[head]
for th,sid,body in S:
    lc='#0E1E44' if th=='S' else '#fff'; logo='logo_navy.png' if th=='S' else 'logo_white.png'
    out.append(f'<div class="post {th}" data-id="{sid}">{body}<div class="line"><svg style="color:{lc}"><use href="#sp"/></svg></div><img class="logo" src="{logo}"></div>')
out.append('</body></html>')
open('row2.html','w').write("\n".join(out))
print(len(S))
