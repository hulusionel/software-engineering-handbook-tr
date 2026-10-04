---
applyTo: "{mimari-tasarim,kod-kalitesi,veri-sistemler,kariyer-kultur,pratik,ileri-duzey-rehberler,yol-haritasi,templates,yapay-zeka-cagi,glossary}/**"
---

# Handbook Fix Protokolü

Tek yazar. Kaynak: yalnızca `.github/REVIEW-FINDINGS.md` içindeki `- [ ]` maddeler ve kullanıcının bu oturumda onayladığı somut bulgular.

## Yapma

- Agent gövdesine gömülü eski T1.x / K1.x listelerini "hâlâ bozuk" sanma — tek kaynak findings dosyasıdır.
- `- [x]` maddeleri yeniden düzeltme.
- İçerik ekleme/silme; emin olmadığın düzeltme.
- `.github/eval/` fixture'ını "düzeltme" — kasıtlı bozuk golden set.

## Yap

1. Findings'i oku; açık maddeleri klasöre göre grupla.
2. Hedef dosyayı oku, sorunu doğrula, düzelt.
3. Anchor değişirse başlık + İçindekiler birlikte güncellenir.
4. `yapay-zeka-cagi/` için öncelik: teknik yanlışlık → güncellik → yapı → yazım. Niş odağı koru.
5. Her madde sonrası findings'de `- [ ]` → `- [x]`. Findings'i yalnızca sen yaz (paralel yazar yok).
6. Mümkünse `python3 .github/scripts/check_links.py` ile doğrula.
