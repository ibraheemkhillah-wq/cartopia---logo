# Instagram · İkinci Satır (السطر الثاني)

| المجلد | المحتوى |
|---|---|
| `carousels/4_Kurumsal_100` | Kurumsal · İlan başı 100$ · 7 سلايدات (الغامق) |
| `carousels/5_Arona_vs_Passat` | Karşılaştırma · Arona mı, Passat mı? · 6 سلايدات (الفاتح) |
| `carousels/6_Hibrit_Nasil_Calisir` | Araba Sözlüğü · Hibrit nasıl çalışır? · 6 سلايدات (الأفتح) |
| `preview/` | الأغلفة جنب بعض، الشبكة، وشكل الصفحة |
| `source/` | ملف التصميم `gen4.py` والصور |

كل الصور 2160×2700. ترتيب النشر بنفس اليوم: 6 ← 5 ← 4. القص 4:5.

إعادة التصدير من `source/`:

```bash
python3 gen4.py && node renderhq.js "$PWD" row2.html out/K ".post[data-id^='K']" 1
```
