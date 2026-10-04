---
applyTo: "{mimari-tasarim,kod-kalitesi,veri-sistemler,kariyer-kultur,pratik,ileri-duzey-rehberler,yol-haritasi,templates,yapay-zeka-cagi,glossary}/**"
---

# Handbook Review Protokolü

Bu bir skill'dir: tekrarlayan inceleme prosedürü. Klasör-özel agent kopyalama.

Hedef klasördeki `.md` dosyalarını oku (README dahil). Deterministik taramayı yeniden icat etme: kırık `�`, dahili link ve markdownlint için `.github/scripts/check_links.py` + CI çıktısını tüket. Senin işin CI'nin yakalayamadığı **içerik yargısı**.

## Kontrol listesi

**İçerik kalitesi**
- [ ] Konu yeterli derinlikte mi? Kitap/rehber ana konseptleri kapsanmış mı?
- [ ] Örnekler, tablolar, diyagramlar isabetli mi?
- [ ] Niş/uygulayıcı odak korunuyor mu (gereksiz temele kaymamış mı)?

**Yapısal bütünlük**
- [ ] Başlık hiyerarşisi ve İçindekiler tutarlı mı?
- [ ] Çapraz referanslar doğru mu? README tüm dosyaları listeliyor mu?
- [ ] Markdown (tablo, link, kod bloğu) bozuk mu?

**Eksik / fazla**
- [ ] Önemli eksik var mı? Diğer dosyalarla gereksiz tekrar / çelişki var mı?
- [ ] Güncelliğini yitirmiş iddia var mı?

**Yazım ve dil**
- [ ] Türkçe typo
- [ ] Glossary ile terim tutarsızlığı (`glossary/terim-sozlugu.md`)
- [ ] İngilizce–Türkçe karışık kullanım sorunları

## Çıktı

Her bulguyu `dosya + bölüm/satır + somut kanıt` ile yaz. Skor A–F. Düzenleme YAPMA.
