#!/usr/bin/env python3
"""
Handbook kalite denetleyicisi — harici bağımlılık YOK (yalnızca stdlib).

Kontrol ettikleri:
  1. Unicode replacement karakteri (U+FFFD, "�") — bozuk emoji/kodlama işareti.
  2. Kırık dahili dosya linkleri — [metin](yol) hedefi diskte yoksa.
  3. Kırık başlık (anchor) linkleri — [metin](dosya#anchor) hedefi, GitHub'ın
     slug algoritmasıyla üretilen başlık anchor'larıyla eşleşmiyorsa.

Kullanım:
    python3 .github/scripts/check_links.py

Çıkış kodu 0 = temiz, 1 = en az bir sorun bulundu.
`.github/` altındaki agent/talimat dosyaları (bozuk karakterleri örnek olarak
içerebildiği için) yalnızca link kontrolünden geçer, FFFD taramasından muaftır.
"""
import glob
import io
import os
import re
import sys
import unicodedata

ROOT = os.getcwd()
FFFD = "�"


def slug(heading_line: str) -> str:
    """GitHub (github-slugger) uyumlu anchor üretimi.

    - küçük harfe çevir
    - emoji/noktalama at; harf, rakam, birleşik işaret (İ->i̇), '-' ve '_' kalsın
    - boşluk -> '-'
    - baştaki/sondaki tireyi KIRPMA, çoklu tireyi BİRLEŞTİRME (GitHub da yapmaz)
    """
    h = re.sub(r"^#+\s*", "", heading_line).rstrip("\n").replace("`", "").lower()
    out = []
    for ch in h:
        if ch.isspace():
            out.append("-")
        elif ch.isalnum() or unicodedata.combining(ch) or ch in "-_":
            out.append(ch)
    return "".join(out)


def heading_anchors(text: str) -> set:
    seen, anchors = {}, set()
    for line in text.split("\n"):
        if re.match(r"^#{1,6}\s", line):
            base = slug(line)
            n = seen.get(base, 0)
            anchors.add(base if n == 0 else f"{base}-{n}")
            seen[base] = n + 1
    return anchors


def main() -> int:
    md_files = [
        f for f in glob.glob("**/*.md", recursive=True) if not f.startswith(".git/")
    ]
    anchors_by_file = {f: heading_anchors(io.open(f, encoding="utf-8").read()) for f in md_files}

    link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    fffd_hits, file_missing, anchor_missing = [], [], []

    for f in md_files:
        text = io.open(f, encoding="utf-8").read()
        # 1. replacement char (content dosyaları; .github/ muaf)
        if not f.startswith(".github/"):
            for i, line in enumerate(text.split("\n"), 1):
                if FFFD in line:
                    fffd_hits.append(f"{f}:{i}: {line.strip()}")
        # 2 & 3. linkler
        d = os.path.dirname(f)
        for m in link_re.finditer(text):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#!")):
                continue
            path, _, anchor = target.partition("#")
            if path == "":
                if anchor and anchor not in anchors_by_file.get(f, set()):
                    anchor_missing.append(f"{f} -> #{anchor}")
            else:
                full = os.path.normpath(os.path.join(d, path))
                if not os.path.exists(full):
                    file_missing.append(f"{f} -> {target}")
                elif anchor and full.endswith(".md") and anchor not in anchors_by_file.get(full, set()):
                    anchor_missing.append(f"{f} -> {target}")

    ok = True
    if fffd_hits:
        ok = False
        print(f"::error::Unicode replacement karakteri (U+FFFD) bulundu — {len(fffd_hits)} satır:")
        for h in fffd_hits:
            print("  ", h)
    if file_missing:
        ok = False
        print(f"::error::Kırık dosya linki — {len(file_missing)} adet:")
        for h in file_missing:
            print("  ", h)
    if anchor_missing:
        ok = False
        print(f"::error::Kırık başlık (anchor) linki — {len(anchor_missing)} adet:")
        for h in anchor_missing:
            print("  ", h)

    if ok:
        print(f"✅ Temiz — {len(md_files)} Markdown dosyası; bozuk karakter ve kırık dahili link yok.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
