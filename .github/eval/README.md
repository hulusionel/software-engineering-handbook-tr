# Reviewer golden set

Handbook reviewer kalitesini ölçer. CI (kırık karakter, kırık link, lint) **ayrı ve birincil** deterministic katmandır; bu set LLM yargısını ölçer.

Fixture kasıtlı bozuk olduğu için `check_links.py` ve markdownlint bu klasörü taramaz. Fixture'ın "düzeltilmemesi" için `python3 .github/eval/verify_fixture.py` CI'da çalışır.

## Kör test

1. `handbook-reviewer` seç.
2. Şunu ver: `.github/eval/golden-fixture.md` dosyasını analiz et.
3. Reviewer **`expected-findings.md` okumamalı** (agent talimatında yasak).
4. Raporu `expected-findings.md` ile karşılaştır. Skor = yakalanan / 10.

Geçer not: **en az 8/10** (G1–G10). CI-yakalanır sapmalar (G1–G3) ile yalnızca modelin görebileceği sapmalar (G4–G10) karışıktır; hepsini yazması beklenir.
