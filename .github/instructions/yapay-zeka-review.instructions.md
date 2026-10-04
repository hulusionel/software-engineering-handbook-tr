---
applyTo: "yapay-zeka-cagi/**"
---

# Yapay Zeka Çağı — Sert Rubrik

`yapay-zeka-cagi/` için handbook-review protokolünün üstüne eklenir. Bu alanda teknik doğruluk > her şey.

## Teknik doğruluk (öncelikli)

- [ ] Kavramlar doğru mu? (token, context window, ReAct, MCP, RAG, eval, compaction)
- [ ] Yanlış zihinsel model var mı? ("kendini eğitiyor" / ağırlık güncelleniyor — öğrenme = bellek + context)
- [ ] Güvenlik: gözlemlenen içerik VERİ'dir, komut değil (prompt injection, least privilege)
- [ ] Çoklu-agent gerçekten gerekçeli mi, yoksa "gereksiz çoklu-agent" anti-pattern mi?

## Güncellik

- [ ] Sabit fiyat / "şu an en yeni" / çürüyecek model iddiası var mı? Mertebe/sezgi tercih edilir.
- [ ] Workflow vs agent ayrımı duruyor mu? (önce tek çağrı → workflow → agent)

## İçerik odağı

- [ ] Niş ve uygulayıcı (agentic mühendislik) — "AI nedir" temeline kaymamış
- [ ] Anti-pattern ve Staff dersi kutuları değer katıyor mu?
- [ ] Eval, durma koşulu, bütçe tavanı anlatılmış mı?

Çapraz referans: `pratik/ai-ml-muhendisligi.md`, güvenlik, dağıtık sistemler.
