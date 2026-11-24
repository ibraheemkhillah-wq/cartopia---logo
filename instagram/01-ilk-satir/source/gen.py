import html
SP='<svg class="sp"><use href="#sp"/></svg>'
def esc(s): return html.escape(s)
slides=[]
# ---------- L : Şeffaf Rapor (dark) ----------
L=[("Değişensiz","01","Aracın hiçbir kaporta parçası değiştirilmemiş.","Kapı, kaput, çamurluk ve tavan fabrikadan çıktığı gibi orijinal.","h_34_hq.jpg","30% 50%"),
   ("Tramersiz","02","TRAMER'de hasar kaydı yok.","Sigorta şirketlerine bildirilmiş bir kaza veya hasar ödemesi bulunmuyor.","h_front_hq.jpg","50% 50%"),
   ("Boyasız","03","Hiçbir parçada boya işlemi yapılmamış.","Her panel boya kalınlığı ölçümüyle tek tek kontrol edilir.","h_34b_hq.jpg","60% 50%")]
for i,(w,n,a,b,img,pos) in enumerate(L):
    slides.append(("L",i+2,5,f'''<img class="bg" src="{img}" style="object-position:{pos}"><div class="wash"></div><div class="vig"></div>
<div class="eyebrow">{SP}ŞEFFAF RAPOR</div><div class="count">{i+2}/5</div>
<div class="bignum">{n}</div>
<h1 style="top:600px;font-size:132px">{esc(w)}</h1>
<div class="sub" style="top:780px;font-size:46px;font-weight:700">{esc(a)}</div>
<div class="sub" style="top:920px;opacity:.9">{esc(b)}</div>'''))
slides.append(("L",5,5,f'''<img class="bg" src="emp_hq.jpg" style="object-position:50% 20%"><div class="wash"></div><div class="vig"></div>
<div class="eyebrow">{SP}ŞEFFAF RAPOR</div><div class="count">5/5</div>
<h1 style="top:640px;font-size:112px">Biz yazdığımızı<br>kanıtlıyoruz.</h1>
<div class="sub" style="top:900px">Her aracımızın ekspertiz bilgisi sizinle açıkça paylaşılır.</div>
<div class="chips"><span class="pill solid">Detaylar için DM</span><span class="pill">Başakşehir · İstanbul</span></div>'''))
# ---------- M : Honda (light) ----------
photos=[("h_front_hq.jpg","Ön Görünüm"),("h_34_hq.jpg","Showroom'da"),("h_dash_hq.jpg","İç Mekan"),("h_seat_hq.jpg","Ön Koltuklar")]
for i,(img,label) in enumerate(photos):
    slides.append(("M",i+2,7,f'''<div class="mbg"></div><img class="photo" src="{img}">
<div class="eyebrow">{SP}2023 HONDA ZR-V</div><div class="count">{i+2}/7</div>
<div class="tag">{esc(label)}</div>'''))
rows=[("Model Yılı","2023"),("Kilometre","29.500 km"),("Motor","Hibrit · 184 hp"),("Vites","Otomatik"),("Durum","Değişensiz · Tramersiz"),("Ekstra","PPF Kaplama")]
tbl="".join(f'<div class="row"><span>{a}</span><b>{b}</b></div>' for a,b in rows)
slides.append(("M",6,7,f'''<div class="mbg"></div><img class="photo dim" src="h_34b_hq.jpg">
<div class="eyebrow">{SP}2023 HONDA ZR-V</div><div class="count">6/7</div>
<h1 style="top:190px;font-size:96px">Teknik<br>Bilgiler</h1>
<div class="card">{tbl}</div>'''))
slides.append(("M",7,7,f'''<div class="mbg"></div><img class="photo dim" src="h_34b_hq.jpg">
<div class="eyebrow">{SP}2023 HONDA ZR-V</div><div class="count">7/7</div>
<h1 style="top:250px;font-size:72px;font-style:normal;font-weight:600">Fiyat</h1>
<h1 style="top:340px;font-size:124px;white-space:nowrap">2.970.000 TL</h1>
<div class="sub" style="top:520px;font-weight:600">Ekspertiz bilgisi hazır · Test sürüşü için randevu alın</div>
<div class="contact"><div><small>WhatsApp</small><b>+90 555 575 50 80</b></div><div><small>Adres</small><b>Başakşehir · İstanbul</b></div><div><small>Instagram</small><b>DM'den yazın</b></div></div>'''))
# ---------- R : 7 Kural (lighter) ----------
rules=[("Ekspertiz yaptırın","Bağımsız bir ekspertizde boya, değişen parça ve mekanik durumu kontrol ettirin."),
("TRAMER kaydını sorgulayın","Aracın hasar geçmişini plakayla sorgulayın. Kayıt varsa tutarına ve tarihine bakın."),
("Kilometreyi kontrol edin","Göstergedeki kilometreyi servis ve muayene kayıtlarıyla karşılaştırın."),
("Servis geçmişine bakın","Düzenli bakım yapılmış mı? Bakım faturalarını ve servis kayıtlarını isteyin."),
("Test sürüşü yapın","Motor sesini, vites geçişlerini, frenleri ve direksiyonu mutlaka deneyin."),
("Piyasa fiyatını araştırın","Benzer ilanlarla karşılaştırın. Piyasanın çok altındaki fiyatlara dikkat edin."),
("Satışı noterde yapın","Devri noterde tamamlayın, ödemeyi güvenli bir yöntemle yapın.")]
bgs=["h_34_hq.jpg","h_front_hq.jpg","h_dash_hq.jpg","h_seat_hq.jpg","h_dash_hq.jpg","h_34b_hq.jpg","h_seat_hq.jpg"]
for i,(t,d) in enumerate(rules):
    slides.append(("R",i+2,9,f'''<img class="bg" src="{bgs[i]}"><div class="wash"></div><div class="vig"></div>
<div class="eyebrow" style="color:#3E6AB3">{SP}<span style="color:#0E1E44">CARTOPIA REHBER</span></div><div class="count">{i+2}/9</div>
<div class="rnum">{i+1}</div>
<h1 style="top:700px;font-size:96px">{esc(t)}</h1>
<div class="sub" style="top:{940 if len(t)<20 else 1000}px">{esc(d)}</div>'''))
slides.append(("R",9,9,f'''<img class="bg" src="h_34b_hq.jpg"><div class="wash"></div><div class="vig"></div>
<div class="eyebrow" style="color:#3E6AB3">{SP}<span style="color:#0E1E44">CARTOPIA REHBER</span></div><div class="count">9/9</div>
<h1 style="top:260px;font-size:100px">Cartopia'da<br><span style="color:#3E6AB3">içiniz rahat.</span></h1>
<div class="sub" style="top:560px">Her aracımızın ekspertiz ve hasar bilgisi sizinle açıkça paylaşılır.</div>
<div class="chips"><span class="pill solid">Kaydet</span><span class="pill">Paylaş</span><span class="pill">DM'den sor</span></div>'''))
head=open('posts.html').read().split('</style>')[0]
extra='''
.count{position:absolute;right:84px;top:92px;font-size:28px;font-weight:600;letter-spacing:.08em;opacity:.85}
.sp{width:30px;height:30px}
.bignum{position:absolute;right:50px;top:150px;font-weight:900;font-style:italic;font-size:420px;line-height:1;color:rgba(255,255,255,.12)}
.rnum{position:absolute;left:70px;top:170px;font-weight:900;font-style:italic;font-size:480px;line-height:1;color:#3E6AB3;opacity:.9}
.pill.solid{background:#fff;color:#1A3060;border-color:#fff}
#R .pill.solid{background:#0E1E44;color:#fff;border-color:#0E1E44}
.mbg{position:absolute;inset:0;background:linear-gradient(90deg,#2E5AA6,#4F86E6)}
.photo{position:absolute;left:60px;right:60px;top:200px;width:960px;height:920px;object-fit:cover;border-radius:36px;box-shadow:0 30px 60px rgba(10,20,48,.35)}
.photo.dim{left:0;right:0;top:0;width:100%;height:100%;border-radius:0;opacity:.28;filter:blur(3px)}
.tag{position:absolute;left:100px;top:1040px;padding:14px 28px;border-radius:999px;background:rgba(255,255,255,.92);color:#1A3060;font-size:30px;font-weight:700}
.card{position:absolute;left:84px;right:84px;top:470px;background:rgba(255,255,255,.95);border-radius:36px;padding:20px 48px;color:#0E1E44}
.card .row{display:flex;justify-content:space-between;align-items:center;padding:26px 0;border-bottom:2px solid #E3EBF8;font-size:34px}
.card .row:last-child{border-bottom:0}
.card .row span{color:#596173;font-weight:500}
.card .row b{font-weight:700}
.contact{position:absolute;left:84px;right:84px;top:700px;display:flex;flex-direction:column;gap:22px}
.contact div{background:rgba(255,255,255,.95);color:#0E1E44;border-radius:28px;padding:24px 36px;display:flex;flex-direction:column}
.contact small{font-size:24px;color:#596173;font-weight:500}
.contact b{font-size:42px;font-weight:700}
'''
out=[head+extra+'</style></head><body>\n<svg width="0" height="0" style="position:absolute"><symbol id="sp" viewBox="0 0 24 24"><path d="M12 0C12.9 6.6 17.4 11.1 24 12 17.4 12.9 12.9 17.4 12 24 11.1 17.4 6.6 12.9 0 12 6.6 11.1 11.1 6.6 12 0Z" fill="currentColor"/></symbol></svg>']
for col,i,tot,body in slides:
    sid=f"{col}{i:02d}"
    lc="#0E1E44" if col=="R" else "#fff"; logo="logo_navy.png" if col=="R" else "logo_white.png"
    out.append(f'<div class="post s" id="{col}" data-id="{sid}">{body}<div class="line"><svg style="color:{lc}"><use href="#sp"/></svg></div><img class="logo" src="{logo}"></div>')
out.append('</body></html>')
open('slides.html','w').write("\n".join(out))
