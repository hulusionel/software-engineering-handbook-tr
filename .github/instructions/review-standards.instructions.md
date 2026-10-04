---
description: "Use when reviewing any Turkish documentation in this handbook project. Provides shared review standards, Turkish language quality criteria, and scoring rubric."
applyTo: "**/*.md"
---

# Handbook Review Standartları

Bu proje bir Türkçe yazılım mühendisliği el kitabıdır. Tüm reviewer agent'lar bu standartları kullanır.

## Puanlama Rubriği

| Skor | Tanım |
|------|-------|
| **A** | Mükemmel — Kapsamlı, doğru, iyi yapılandırılmış, typo yok |
| **B** | İyi — Küçük eksikler veya birkaç typo var |
| **C** | Orta — Belirgin eksikler veya yapısal sorunlar var |
| **D** | Zayıf — Önemli içerik eksik veya çok fazla hata var |
| **F** | Yetersiz — Ciddi sorunlar, baştan gözden geçirilmeli |

## Türkçe Dil Kalitesi Kontrolleri

### Yaygın Typo Kalıpları
- "ğ" yerine "g" kullanımı
- "ş" yerine "s" kullanımı
- "ç" yerine "c" kullanımı
- "ü" yerine "u" kullanımı
- "ö" yerine "o" kullanımı
- "ı" yerine "i" kullanımı
- Büyük/küçük İ-i hataları

### Terim Tutarlılığı
- Aynı İngilizce terim farklı dosyalarda farklı çevrilmiş mi?
- Glossary (`glossary/terim-sozlugu.md`) ile tutarlılık
- Teknik terimlerde parantez içi İngilizce orijinal var mı?

### Markdown Kalite Kontrolleri
- Kırık linkler (`[text](broken-path)`)
- Boş başlıklar
- Tutarsız liste formatı (- vs *)
- Eksik satır boşlukları (başlık öncesi/sonrası)
- Tablo hizalama sorunları
- Kod bloğu dil belirteci eksikliği

## Raporlama Kuralları

1. Her bulguyu **dosya adı** ve **bölüm/başlık** ile referansla
2. Typo'lar için: `satır X: "yalnış" → "yanlış"` formatı kullan
3. Subjektif yorum yerine somut, doğrulanabilir bulgu raporla
4. Öncelik sıralaması: Yanlış bilgi > Eksik içerik > Yapısal sorun > Typo
5. Her zaman Türkçe raporla
