# Handbook agent'leri

Bu handbook'u tutarlı tutmak için kullanılan review agent'ları. Dosyalar **GitHub Copilot custom agent** formatındadır (`*.agent.md`); VS Code'da Copilot Chat'in agent seçicisinden çağrılır.

Kurulumun hikâyesi: [67.000 Satırlık Türkçe Bir Handbook Yazarken Öğrendiklerim](https://medium.com/@hulusi.onel/67-000-sat%C4%B1rl%C4%B1k-t%C3%BCrk%C3%A7e-bir-handbook-yazarken-%C3%B6%C4%9Frendiklerim-115eeb7baf2e)

## Roller

Üç rol. Eski klasör-başı 17 işçi kaldırıldı; tekrarlayan protokol skill'de.

| Agent | Araçlar | Ne zaman |
|-------|---------|----------|
| `handbook-reviewer` | read, search | Tek klasör incelemesi |
| `handbook-fixer` | read, search, edit, execute | Onaylı düzeltme; tek yazar |
| `orchestrator` | read, search, agent, todo | Tam kitap: paralel review, sıralı fix |

## Tasarım ilkeleri

- **Okuyan çok, yazan tek.** Reviewer'lar paralel çalışır ama dosya yazamaz; tüm düzeltmeler tek fixer'dan sıralı geçer.
- **İnsan onayı.** Orchestrator fixer'ı kendiliğinden başlatmaz (`send: false` handoff).
- **Script yakalayabiliyorsa LLM'e bırakma.** Kırık karakter, kırık link ve markdown biçimi CI'da (`.github/scripts/check_links.py`, markdownlint) kontrol edilir; agent'lar yalnızca içerik yargısına odaklanır.
- **Reviewer da test edilir.** `.github/eval/` altındaki kör golden set reviewer kalitesini ölçer.

## Dosyalar

- Protokoller (skill): `.github/instructions/handbook-review.instructions.md`, `yapay-zeka-review.instructions.md`, `handbook-fix.instructions.md`, `review-standards.instructions.md`
- Bulgu takibi: `.github/REVIEW-FINDINGS.md` (yalnızca fixer yazar)
- Eval: `.github/eval/` (kör golden set)
