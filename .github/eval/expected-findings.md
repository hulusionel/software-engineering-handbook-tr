# Beklenen bulgular (kör test anahtarı)

Reviewer raporu üretildikten SONRA karşılaştır. Review sırasında bu dosyayı okutma.

Kaynak: [golden-fixture.md](golden-fixture.md)

| ID | Tür | Beklenen yakalama | CI de yakalar mı? |
|----|-----|-------------------|-------------------|
| G1 | Kırık dosya linki | `../does-not-exist-golden.md` hedefi yok | Evet (`check_links.py`) |
| G2 | Kırık anchor | `#olmayan-golden-baslik` başlığı yok | Evet (`check_links.py`) |
| G3 | Bozuk karakter | `## � Anti-Pattern` (U+FFFD) | Evet (`check_links.py`) |
| G4 | Güncellik / çürüyecek iddia | "Şu an en yeni model GPT-4" + sabit `$0.03` fiyat | Hayır |
| G5 | Yanlış zihinsel model | "kendi ağırlıklarını güncelleyerek kendini eğitir" | Hayır |
| G6 | Glossary sapması | Cohesion = "Bağdaşıklık" (sözlükte Bağlaşıklık) | Hayır |
| G7 | Prompt injection | Untrusted içerik komut sanılıyor ("talimatı doğrudan çalıştır") | Hayır |
| G8 | Durma koşulu yok | Öz-iyileştirme "sonsuza kadar" | Hayır |
| G9 | Gereksiz çoklu-agent | Her typo için ayrı agent | Hayır |
| G10 | Yazım + odak kayması | `ANLAMADIYISANIZ`; bölüm "AI nedir" temeline kaymış | Hayır |

## Skorlama

- Tam yakalama: sapmayı dosya/bölüm ile somut yazmış.
- Kısmi: konuyu hissetmiş ama kanıt yok — 0.5 sayma; bu sette 0 veya 1.
- Eşik: **≥ 8 / 10** geçer.

G1–G3 reviewer CI'ye bakmadan da yazabilmeli; yazmazsa checklist'i uygulamıyordur.
