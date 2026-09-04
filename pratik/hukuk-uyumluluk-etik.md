# ⚖️ Hukuk, Uyumluluk ve Etik

> **"Compliance is the floor, not the ceiling."**

Bu doküman mühendisin **bilmek zorunda olduğu** hukuki / regülatif çerçeveleri özetler: GDPR, KVKK, PCI-DSS, SOC 2, açık kaynak lisans hijyeni, etik AI.

---

## 📑 İçindekiler

1. [Niye Mühendis İlgilenir?](#1-niye-mühendis-i̇lgilenir)
2. [GDPR — AB Veri Koruması](#2-gdpr--ab-veri-koruması)
3. [KVKK — Türkiye Kişisel Verileri Koruma](#3-kvkk--türkiye-kişisel-verileri-koruma)
4. [Diğer Major Düzenlemeler](#4-diğer-major-düzenlemeler)
5. [PCI-DSS](#5-pci-dss)
6. [SOC 2](#6-soc-2)
7. [Açık Kaynak Lisans Hijyeni](#7-açık-kaynak-lisans-hijyeni)
8. [Patent ve IP](#8-patent-ve-ip)
9. [Etik AI ve Algoritmik Hesap Verebilirlik](#9-etik-ai-ve-algoritmik-hesap-verebilirlik)
10. [Açık Mühendislik Sorumluluğu](#10-açık-mühendislik-sorumluluğu)

---

## 1. Niye Mühendis İlgilenir?

> **"Yasa bilmiyordum"** kişisel sorumluluktan kurtarmaz. Bilmemek **organizasyonu** kurtarmaz.

### Riskler

- 📉 **Para cezası**: GDPR'da yıllık global cironun %4'ü veya €20M.
- 🔒 **İşlem kısıtlaması**: Veri işleme yasağı.
- 📰 **İtibar kaybı**: Public breach disclosure.
- ⚖️ **Bireysel sorumluluk**: CTO/DPO'nun cezai sorumluluğu.
- 🚪 **Kişisel kovuşturma**: Bazı jurisdiksiyonlarda mühendis sorumlu tutulabilir.

### Mühendisin "ben sadece kod yazıyorum" savunması

Sınırlıdır:
- ✅ İşveren talimatı.
- ❌ Etik / hukuki net açık ihlal.
- ❌ Bilgi sahibi olduğun ihlal (whistleblowing yükümlülüğü bazı jurisdiksiyonlarda).

> **Volkswagen "Dieselgate" 2015**: Mühendisler emisyon test sahteciliği koduna eklendi. Bireysel mahkum oldu.

---

## 2. GDPR — AB Veri Koruması

> **General Data Protection Regulation** (2016, yürürlük 2018).

### Kim kapsamda?

- AB'de yerleşik organizasyon.
- AB **vatandaşına** mal/hizmet sunan herhangi bir org (Türkiye'den AB'ye satan e-ticaret dahil).
- AB vatandaşının davranışını izleyen.

### Temel kavramlar

- **Personal Data**: Kimliklendirilebilir gerçek kişiyle ilgili **her** veri (IP, cookie, location, pseudonymized data dahil).
- **Special Category** (sensitive): Sağlık, ırk, din, siyasi görüş, biometric, genetik, sexual orientation.
- **Data Controller**: Amaç ve araçları belirleyen.
- **Data Processor**: Controller adına işleyen (çoğu SaaS).
- **DPO** (Data Protection Officer): Belirli kriterlerde zorunlu.

### 7 ilke

1. Lawfulness, fairness, transparency.
2. Purpose limitation.
3. Data minimization.
4. Accuracy.
5. Storage limitation.
6. Integrity and confidentiality.
7. Accountability.

### Hak temelleri (Lawful basis)

| Basis | Anlam |
|---|---|
| **Consent** | Açık, spesifik, geri alınabilir |
| **Contract** | Sözleşme ifasi için gerekli |
| **Legal obligation** | Yasal zorunluluk |
| **Vital interests** | Yaşamsal çıkar |
| **Public task** | Kamu görevi |
| **Legitimate interests** | Meşru çıkar (balancing test gerekir) |

### Data Subject Rights

| Hak | Açıklama |
|---|---|
| **Access** | Kendi verisine erişim (DSAR) |
| **Rectification** | Düzeltme |
| **Erasure** ("right to be forgotten") | Silme |
| **Restriction** | İşleme kısıtlaması |
| **Portability** | Makine-okunabilir export |
| **Objection** | İtiraz |
| **Automated decision** | Otomatik karara karşı insan müdahalesi talebi |

### Mühendislikte ne yapar?

- ✅ **Soft delete + scheduled hard delete** (right to erasure).
- ✅ **Audit log**: Kim hangi PII'a erişti.
- ✅ **DSAR endpoint**: Export tüm user data (cross-system).
- ✅ **Consent log**: Onay tarihi, versiyonu, scope.
- ✅ **Data minimization in code**: Gereken alanlar.
- ✅ **Pseudonymization** at rest.
- ✅ **Encryption** in transit + at rest.
- ✅ **Data residency**: AB user → AB region.
- ✅ **Cross-border transfer**: Standard Contractual Clauses, BCR, adequacy decision.

### Breach notification

- 72 saat regulator (autoriteit, CNIL, AEPD, ICO, ...).
- Affected user'a "without undue delay" if high risk.

### Teknik önerimler

```sql
-- Soft delete + retention scheduler
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email TEXT,
  ...
  deleted_at TIMESTAMP NULL,
  scheduled_purge_at TIMESTAMP NULL  -- 30-90 gün sonra hard delete
);
```

```python
# Right-to-erasure: cross-system fan-out
def delete_user(user_id):
    db.soft_delete(user_id, purge_in_days=30)
    kafka.publish('user.deletion_requested', {'user_id': user_id})
    # Downstream: search index, cache, analytics, backup, replicas
    audit_log('user_deletion', user_id, actor='self_service')
```

---

## 3. KVKK — Türkiye Kişisel Verileri Koruma

> **6698 sayılı Kişisel Verilerin Korunması Kanunu** (2016).

### GDPR ile karşılaştırma

| | GDPR | KVKK |
|---|---|---|
| Yıl | 2018 yürürlük | 2016 |
| Para cezası | %4 cirou veya €20M | İdari para cezası, küçük (örn. 2024'te 7M-10M TL aralığı) |
| Right to erasure | Açık | "Silme, yok etme, anonim hale getirme" |
| DPO | Belirli kriterlerde | Verbis kayıt zorunlu |
| Cross-border | SCC, BCR, adequacy | KVKK Kurulu kararı + açık rıza veya istisna |

### Verbis (VERBİS)

> Veri Sorumluları Sicil Bilgi Sistemi.
> Belirli eşikleri aşan veri sorumluları kayıtlı olmalı.

### Anonimleştirme

- KVKK'da **anonim hale getirilmiş** veri kişisel veri sayılmaz.
- Re-identification testleri zorunlu.
- k-anonymity, l-diversity, differential privacy.

### Pratik öneriler

- ✅ Verbis kayıt + güncel tut.
- ✅ Aydınlatma metni (privacy notice).
- ✅ Açık rıza (explicit consent) gereken yerler.
- ✅ Veri envanteri (data inventory).
- ✅ Veri güvenliği teknik tedbirler (KVKK rehberi).
- ✅ Veri ihlal bildirimi 72 saat (önemli vakalarda).

---

## 4. Diğer Major Düzenlemeler

### CCPA / CPRA (California)

- ABD California eyalet yasası.
- "Right to know, delete, opt-out of sale".
- Threshold: \$25M revenue veya 50K+ resident.

### LGPD (Brezilya)

- GDPR-inspired.
- 2020 yürürlük.

### PIPL (Çin)

- Cross-border transfer çok kısıtlı.
- Çin user data → Çin'de tutulmalı (genelde).

### India DPDP (2023)

- Yeni, GDPR-inspired ama "consent" odaklı.

### NIS2 (AB) — Network and Information Security

- Critical infrastructure cyber security.
- Reporting, governance, supply chain.

### DORA (AB) — Digital Operational Resilience Act

- Finansal sektör için ICT risk management.
- 2025 yürürlük.

### EU AI Act (2024)

- AI sistemleri için risk-based regulation.
- High-risk AI: assessment, transparency, human oversight.
- Foundation model: TE (technical documentation).

---

## 5. PCI-DSS

> **Payment Card Industry Data Security Standard**. Visa/MC/Amex card data işleyen herkes.

### 4 SAQ Level

| Level | Volume |
|---|---|
| 1 | 6M+ tx/year |
| 2 | 1-6M |
| 3 | 20K-1M |
| 4 | < 20K |

### 12 ana gereksinim

1. Firewall.
2. No vendor default.
3. Cardholder data protection.
4. Encryption in transit.
5. Anti-malware.
6. Secure development.
7. Access restriction.
8. User identification.
9. Physical access.
10. Network monitoring.
11. Security testing.
12. Information security policy.

### Mühendislikte

- **Tokenization**: Card data Stripe/Adyen'de saklanır, sen token tutarsın.
- **Network segmentation**: CDE (Cardholder Data Environment) izole.
- **Encryption**: AES-256 at rest, TLS 1.2+ in transit.
- **Audit log**: 1 yıl retention.
- **Quarterly vulnerability scan** (ASV).
- **Annual penetration test**.

### Anti-pattern

- 🚫 Card number app log'unda.
- 🚫 Email body'de PAN.
- 🚫 Cleartext database'de.
- 🚫 Test data prod card number ile.

---

## 6. SOC 2

> AICPA standardı. 5 trust principle:

1. **Security** (zorunlu).
2. **Availability**.
3. **Processing Integrity**.
4. **Confidentiality**.
5. **Privacy**.

### Type 1 vs Type 2

| | Type 1 | Type 2 |
|---|---|---|
| Süre | Bir an | 6-12 ay gözlem |
| Test | Design only | Operating effectiveness |
| Auditor | Tek vizit | Periyodik |
| Trust | Düşük | Yüksek |

### Mühendislikte

- **Access control**: SSO, RBAC, audit log.
- **Change management**: PR review, deploy log.
- **Incident management**: Runbook, postmortem, ticket.
- **Vendor management**: 3rd party risk assessment.
- **Backup + DR**: Tested.
- **Monitoring**: SIEM, alert.
- **Vulnerability management**: Scan + patch SLA.

### Effort

- İlk SOC 2: 6-12 ay hazırlık + 6-12 ay gözlem = ~1 yıl total.
- Tools: Vanta, Drata, Tugboat Logic, Secureframe — **çok yardımcı** (\$10-30K/yıl).

---

## 7. Açık Kaynak Lisans Hijyeni

### Lisans aileleri

| Aile | Örnek | Yükümlülük |
|---|---|---|
| **Permissive** | MIT, BSD-3, Apache-2 | Attribution |
| **Weak copyleft** | LGPL, MPL-2 | Modify olduysa source |
| **Strong copyleft** | GPL-2, GPL-3 | Combined work full source |
| **Network copyleft** | AGPL-3 | SaaS olarak sunulsa bile source |
| **Source-available** | BSL, SSPL, ELv2 | Belirli kullanım kısıtlamalı |
| **Public domain** | CC0, Unlicense | Hiç |

### "Fork & relicense" furtinası

- 2018+: MongoDB SSPL, Elastic SSPL, Redis SSPL, HashiCorp BSL.
- Reaction: AWS forks (OpenSearch, Valkey, OpenTofu).
- Mühendis için: lisansa **dikkat**, "open source" fonun maliyet senin tarafına geçebilir.

### Compliance araçları

- **FOSSA, Black Duck, Snyk Open Source** — license + vulnerability scan.
- **REUSE** (FSFE) — file-level licensing.
- **CycloneDX SBOM** — license metadata included.
- **SPDX** — license expression standard.

### Pratik kurallar

- ✅ Dependency lisanslarını **bil**.
- ✅ GPL'i closed-source'a katma (ya AGPL-network etkilenir ya GPL-3 viral).
- ✅ Apache-2 patent grant (savunma).
- ✅ MIT/BSD attribution disclosure (LICENSES.txt).
- ✅ Lisans değişimi (relicense) gözlem altında — "version" pin et.

---

## 8. Patent ve IP

### Software patent

- 🇺🇸 US: Software patent geçerli ama Alice 2014 sonrası dar.
- 🇪🇺 EU: "Pure software" patent yok, ama "technical effect" varsa OK.
- 🇹🇷 TR: AB patentleri benzeri.

### Defensive patent

- **Open Invention Network** (OIN): Linux ekosistemi için cross-license patent havuzu.
- **Apache 2.0 patent grant**: Patentini sunucuyla beraber lisansla.
- Açık kaynaklamak savunma değildir; **patent license** clause olmalı.

### Trade secret

- Kod **gizli tutulduğu sürece** korunur.
- Açık kaynak yapınca trade secret kaybolur.
- NDA, employment agreement, access control.

### Çalışan IP

- **Work for hire** çoğu jurisdiksiyonda → işverenin.
- Açık kaynak katkı yapmadan önce şirket policy'sine bak (CLA gerekebilir).
- Kişisel proje vs iş projesi ayrımı kontratta olmalı.

---

## 9. Etik AI ve Algoritmik Hesap Verebilirlik

### Bilinen sorunlar

- **Bias**: Eğitim verisindeki toplumsal bias model'e geçer.
- **Hallucination**: LLM yanlış ama kendinden emin cevap verir.
- **Privacy**: Eğitim verisinde PII, output'ta sızıntı.
- **Copyright**: Eğitim verisinin lisansı.
- **Manipulation**: Deep fake, disinformation.
- **Job displacement**: Geniş ekonomik etki.

### Frameworks

- **NIST AI RMF** (2023) — voluntary risk management.
- **EU AI Act** (2024) — risk-based regulation, high-risk için zorunlu.
- **ISO/IEC 42001** (2023) — AI management system standard.
- **OECD AI Principles** (2019).

### "AI Ethics" pillarları

| | Anlam |
|---|---|
| **Fairness** | Bias minimal, equal treatment |
| **Accountability** | Sorumluluk takibi |
| **Transparency** | Açıklanabilirlik (explainability) |
| **Privacy** | Kullanıcı veri koruması |
| **Safety** | Zararlı output önleme |
| **Human oversight** | Kritik kararlarda insan |

### Mühendislikte

- ✅ **Model card** (Margaret Mitchell 2019): Model kapasiteleri, sınırları, eğitim verisi, bias, intended use.
- ✅ **Datasheet for datasets**: Veri seti dokümentasyonu.
- ✅ **A/B testing fairness**: Demographic parity ölçümü.
- ✅ **Red-teaming**: Adversarial testing.
- ✅ **Output filter**: Toxic, copyright, PII filtreler.
- ✅ **Audit log**: Inference + model version + input hash.
- ✅ **Human-in-the-loop**: Yüksek-risk decision insan onayı.

---

## 10. Açık Mühendislik Sorumluluğu

### Ethical Engineer Duties

> ACM Code of Ethics, IEEE Code of Ethics özeti:

1. **Public good** — kamu yararı önce.
2. **Avoid harm**.
3. **Be honest** — abartı, sahtecilik yok.
4. **Be fair** — discrimination yok.
5. **Respect privacy**.
6. **Honor confidentiality**.
7. **Maintain professionalism**.
8. **Continuous learning**.

### Whistleblowing

- Yasa dışı / etik dışı işveren faaliyeti.
- Internal escalation önce (ombudsperson, legal).
- External (regulator, press) son çare.
- Yasal koruma jurisdiksiyona göre değişir (US SOX, EU Whistleblower Directive 2019).

### "Resign or implement" durumu

> Etik dışı bir özellik implement etmen istendiğinde:

1. **Internal escalation**: Manager → skip-level → ombudsperson → CTO.
2. **Document**: Yazılı concern.
3. **Refusal**: Bazı jurisdiksiyonlarda etik refuse legally protected.
4. **Resignation**: Son çare ama **dokümante** et.

### Profesyonel sorumluluk örnekleri

- **Therac-25 (1985-1987)**: Medikal cihaz race condition → 6 ölüm. Mühendis duruşunda mahkum.
- **Volkswagen Dieselgate (2015)**: Emisyon sahtecilik kodu. Mühendis personal mahkum.
- **Boeing 737 MAX (2018-2019)**: MCAS sistem tasarım. Soruşturma sürüyor.
- **Theranos (2003-2018)**: Sahte tıbbi cihaz. Yönetim mahkum.

---

## 🎯 Staff+ Kontrol Listesi

### Ürün / servis launch öncesi

- [ ] Hangi data tipleri (PII, PCI, PHI) işleniyor?
- [ ] Hangi jurisdiksiyondaki user'lar etkileniyor?
- [ ] Lawful basis (GDPR) belirlendi mi?
- [ ] Privacy notice + cookie consent var mı?
- [ ] Data inventory + retention policy?
- [ ] DSAR + erasure flow implement edildi mi?
- [ ] Cross-border transfer mekanizması (SCC, vs.)?
- [ ] Encryption at rest + in transit?
- [ ] Audit log + retention?
- [ ] Breach response plan?

### Engineering practice

- [ ] Açık kaynak lisansları taranıyor mu (CI'da)?
- [ ] SBOM üretiliyor mu?
- [ ] CLA (Contributor License Agreement) gerekli mi?
- [ ] Patent grant veren lisans tercihi (Apache-2 default)?
- [ ] AI features → model card + bias testing?
- [ ] Mühendis etik eğitim alıyor mu?

---

## 📚 İleri Okuma

- *Privacy Engineering* — Cronk
- ACM Code of Ethics
- IEEE Code of Ethics
- *Ethics in Tech* — Vali (CC-BY)
- IAPP (International Association of Privacy Professionals) — CIPM, CIPT certifications
- Bruce Schneier — *Click Here to Kill Everybody*
- *Weapons of Math Destruction* — Cathy O'Neil
- *The Alignment Problem* — Brian Christian
- KVKK Kurulu yayınları, GDPR.eu rehberleri

> [⬅️ Pratik klasörü](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
