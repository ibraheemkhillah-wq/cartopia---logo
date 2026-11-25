"""Rule: no plain backgrounds. Insert a faded, topic-related photo behind every slide whose background is a flat colour.
usage: python3 apply_bg.py <html-file>"""
import re,sys
# id -> (image, opacity, blur px)
MAP={
 # Row 1 – Şeffaf Rapor (dark)
 'T01':('emp_hq.jpg',.30,6),'T02':('v_13.jpg',.35,5),'T05':('v_21.jpg',.32,6),
 # Row 1 – Honda (light)
 'M02':('h_front_hq.jpg',.45,18),'M03':('h_34_hq.jpg',.45,18),'M04':('h_dash_hq.jpg',.45,18),'M05':('h_seat_hq.jpg',.45,18),
 # Row 1 – Rehber (lighter)
 'R02':('d_inspect.jpg',.30,8),'R04':('h_dash_hq.jpg',.28,6),'R05':('d_care.jpg',.30,10),'R07':('d_coins.jpg',.30,8),'R08':('d_keys.jpg',.30,8),
 # Row 2 – Kurumsal (dark)
 'K03':('k_listings.jpg',.30,6),'K04':('k_tablet.jpg',.30,6),'K06':('k_woman.jpg',.30,6),
 # Row 2 – Karşılaştırma (light)
 'C01':('c_passat.jpg',.40,14),'C02':('c_arona.jpg',.45,16),'C03':('c_passat.jpg',.45,16),'C04':('c_arona.jpg',.35,10),'C05':('c_passat.jpg',.35,10),'C06':('d_showroom.jpg',.35,6),
 # Row 2 – Hibrit (lighter)
 'S01':('h_34_hq.jpg',.35,14),'S02':('h_34b_hq.jpg',.28,8),'S03':('h_dash_hq.jpg',.28,6),'S04':('h_front_hq.jpg',.30,14),'S05':('h_34_hq.jpg',.26,8),'S06':('h_34b_hq.jpg',.35,14),
}
BG=r'(lightbg|darkbg|mbg|bgL|bgK|bgC|bgS)'
f=sys.argv[1]; s=open(f).read(); n=0
for sid,(img,op,bl) in MAP.items():
    m=re.search(r'data-id="%s">\s*(<div class="%s"[^>]*></div>)'%(sid,BG),s)
    if not m: continue
    tag=f'<img class="bgph" src="{img}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:{op};filter:blur({bl}px) {'saturate(.55) brightness(1.45)' if sid[0] in 'RS' else 'saturate(.9)'};transform:scale(1.06)">'
    s=s[:m.end(1)]+tag+s[m.end(1):]; n+=1
open(f,'w').write(s); print(f,n)
