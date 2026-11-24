# Instagram · İlk Satır (أول سطر)

ثلاث بوستات كاروسيل لصفحة `@cartopia_tr`، بالتدرّج: غامق ← فاتح ← أفتح.

## المجلدات

| المجلد | المحتوى |
|---|---|
| `carousels/1_Seffaf_Rapor` | Şeffaf Rapor · 5 سلايدات (العمود الغامق) |
| `carousels/2_Honda_ZR-V` | 2023 Honda ZR-V · 7 سلايدات (العمود الفاتح) |
| `carousels/3_7_Altin_Kural` | İkinci El Alırken 7 Altın Kural · 9 سلايدات (العمود الأفتح) |
| `preview/ucu-yan-yana.jpg` | الأغلفة الثلاثة جنب بعض |
| `preview/grid-gorunumu.jpg` | شكلها بالشبكة (قص 3:4) |
| `preview/instagram-profil.jpg` | شكلها على صفحة الإنستغرام |
| `source/` | ملفات التصميم (HTML + Python) والصور المستعملة |

كل الصور مقاس **2160×2700** (ضعف 1080×1350).

## ترتيب النشر (بنفس اليوم)

1. `3_7_Altin_Kural`
2. `2_Honda_ZR-V`
3. `1_Seffaf_Rapor`

عند النشر اختاروا قص **4:5**.

## إعادة التصدير من المصدر

من داخل `source/`:

```bash
python3 gen.py && node renderhq.js "$PWD" slides.html out/2_Honda_ZR-V ".post[data-id^='M']" 2
python3 gen2.py && node renderhq.js "$PWD" slides.html out/3_7_Altin_Kural ".post[data-id^='R']" 2
python3 gen3.py && node renderhq.js "$PWD" slides3.html out/1_Seffaf_Rapor ".post" 1
node renderhq.js "$PWD" posts.html out/2_Honda_ZR-V "#M" 1
node renderhq.js "$PWD" posts.html out/3_7_Altin_Kural "#R" 1
```

يحتاج Python 3 و Node.js مع Playwright (Chromium). الخط: Poppins من Google Fonts.

## ملاحظات

- أرقام الميكرون بسلايد Boyasız وشاشة TRAMER وأسعار سلايد السوق أمثلة توضيحية (مكتوب عليها «Örnek»).
- بعض الصور من بروفايل الشركة؛ تأكدوا من حقوق استخدامها بالإعلانات.
