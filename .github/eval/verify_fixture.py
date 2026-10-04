#!/usr/bin/env python3
"""Golden fixture hâlâ kasıtlı bozuk mu? (eval setinin 'düzeltilmesini' yakala)

Kullanım: python3 .github/eval/verify_fixture.py
Çıkış 0 = 10 işaret duruyor; 1 = fixture bozulmuş.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = Path(__file__).resolve().parent / "golden-fixture.md"

# (id, açıklama, fixture içinde geçmesi gereken alt dizgi)
MARKERS: list[tuple[str, str, str]] = [
    ("G1", "kırık dosya linki", "does-not-exist-golden.md"),
    ("G2", "kırık anchor", "#olmayan-golden-baslik"),
    ("G3", "U+FFFD bozuk karakter", "\ufffd"),
    ("G4", "stale model/fiyat iddiası", "en yeni model GPT-4"),
    ("G5", "kendini eğitiyor yanılgısı", "kendi ağırlıklarını güncelleyerek"),
    ("G6", "glossary sapması Bağdaşıklık", "Bağdaşıklık"),
    ("G7", "untrusted içerik = komut", "talimatı doğrudan çalıştır"),
    ("G8", "durma koşulu yok", "sonsuza kadar"),
    ("G9", "gereksiz çoklu-agent", "ayrı bir agent başlat"),
    ("G10", "typo ANLAMADIYISANIZ", "ANLAMADIYISANIZ"),
]


def main() -> int:
    if not FIXTURE.is_file():
        print(f"::error::Fixture yok: {FIXTURE.relative_to(ROOT)}")
        return 1
    text = FIXTURE.read_text(encoding="utf-8")
    missing = [f"{i} ({desc})" for i, desc, needle in MARKERS if needle not in text]
    if missing:
        print("::error::Golden fixture işaretleri eksik — eval seti bozulmuş olabilir:")
        for m in missing:
            print("  ", m)
        return 1
    print(f"✅ Golden fixture sağlam — {len(MARKERS)} işaret duruyor ({FIXTURE.relative_to(ROOT)}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
