# 💰 FinOps — Cloud Maliyet Disiplini

> **"Cloud cost is now an engineering problem, not a finance problem."**

Bu doküman cloud maliyetini staff+ mühendisin perspektifinden ele alır: birim ekonomisi, FinOps framework, optimization patterns, anti-pattern'ler.

---

## 📑 İçindekiler

1. [Niye FinOps?](#1-niye-finops)
2. [FinOps Framework (3 Faz)](#2-finops-framework-3-faz)
3. [Unit Economics](#3-unit-economics)
4. [Cloud Bill Anatomi](#4-cloud-bill-anatomi)
5. [Compute Optimizasyonu](#5-compute-optimizasyonu)
6. [Storage Optimizasyonu](#6-storage-optimizasyonu)
7. [Network / Egress Tuzakları](#7-network--egress-tuzakları)
8. [Veritabanı Maliyeti](#8-veritabanı-maliyeti)
9. [Observability Maliyeti](#9-observability-maliyeti)
10. [Showback vs Chargeback](#10-showback-vs-chargeback)
11. [Anti-Pattern'ler](#11-anti-patternler)

---

## 1. Niye FinOps?

### Ölçek

> 2024: Global cloud spend > \$700 milyar. Ortalama org cloud bill'inin **%30'u israf** (Flexera 2024 State of the Cloud).

### Engineering problem

- Her API call, her log line, her query → **doğrudan fatura kalemi**.
- Tasarım kararları (region count, replica, retention) maliyeti **10x** etkiler.
- Cost-aware engineering = velocity penalty değil; **doğru velocity**.

### Mühendisin rolü

| Rol | Sorumluluk |
|---|---|
| Engineer | Tasarımda cost-awareness, code-level optimization |
| Manager | Budget allocation, prioritization |
| Finance | Forecasting, variance analysis |
| FinOps team | Tooling, governance, education |

> **Ortak dil**: FinOps Foundation framework.

---

## 2. FinOps Framework (3 Faz)

### Phase 1: Inform

> Görünürlük. Kim ne harcıyor?

- Tagging strategy (team, env, service, cost-center).
- Cost dashboard (CloudWatch Billing, GCP Billing, Azure Cost Mgmt, CloudHealth, Vantage).
- Daily/weekly cost report by team.
- Anomaly detection (sudden spike alert).

### Phase 2: Optimize

> Aksiyon. Ne kesilebilir, ne yeniden tasarlanabilir?

- Right-sizing (compute).
- Reserved/savings plan.
- Spot/preemptible instances.
- Storage tiering.
- Idle resource cleanup.
- Architecture refactoring (e.g. expensive service → cheaper alternative).

### Phase 3: Operate

> Sürdürülebilir. Yeni proje cost-aware başlamış mı?

- Cost gate in design review.
- Budget alert per team.
- Showback dashboard (her ekip kendi maliyetini görür).
- KPI: cost per unit (transaction, user, GB ingested).

---

## 3. Unit Economics

### Niye?

> "Toplam fatura artıyor" anlamsız. **Per-unit** ne maliyet?

```
Cost per active user / month
Cost per request
Cost per GB processed
Cost per video minute
Cost per AI inference
```

### Hesap örneği

```
Aylık compute: $50,000
Aylık MAU: 5,000,000
→ $0.01 / user / month

Bu sürdürülebilir mi?
   Free tier user'dan ARPU $0 → $0.01 zarar / user
   Premium user'dan ARPU $5 → $4.99 marjin / user
   Free:premium ratio = 100:1 → blended margin: ($5 - 100 * $0.01 - $0.01) / 101 = ~$0.04 / user
```

> Mühendisin işi: **denominator'ü büyütmek** (verim) veya **numerator'u küçültmek** (optimize).

### "Cost per request" örneği

```
Compute: $1000/ay, 100M req/ay
   = $0.00001 / request = $10 per million

Bu DDoS'ta ne olur?
   Attacker 10K req/s → 25 günde 100M req artış → $1000 ek
   Attacker hedefi senin değil, free tier maliyetin → kim öder?
```

→ **Cost amplification** saldırı surface (Lambda, S3 GET, AI API'leri için kritik).

---

## 4. Cloud Bill Anatomi

### Tipik dağılım (medium SaaS)

| Kalem | % |
|---|---|
| Compute (EC2, K8s, Lambda) | 40-50 |
| Storage (S3, EBS, RDS) | 15-20 |
| Network egress | 10-20 |
| Database (RDS, DynamoDB) | 10-15 |
| Observability (CloudWatch, Datadog) | 5-15 |
| Other (KMS, Lambda, Route53, ...) | 5-10 |

> **Sürpriz**: Çoğu org **observability'i** sunucu maliyetinden fazla harcadığını fark ediyor.

### "Hidden" cost'lar

- 🚨 NAT Gateway data processing ($0.045/GB).
- 🚨 Cross-AZ traffic ($0.01/GB her yön).
- 🚨 KMS encrypt/decrypt API ($0.03 / 10K).
- 🚨 CloudWatch Logs ingestion ($0.50/GB).
- 🚨 S3 GET/PUT request count.
- 🚨 ElastiCache snapshot.

### Reserved / Savings Plan

| | Term | Indirim |
|---|---|---|
| **AWS Reserved Instance** | 1 / 3 yıl | 30-72% |
| **AWS Savings Plan (Compute)** | 1 / 3 yıl | 27-66% |
| **GCP CUD** (Committed Use Discount) | 1 / 3 yıl | 25-57% |
| **Azure Reserved VM** | 1 / 3 yıl | 30-72% |

> Steady-state baseline kapasiteyi reserve et. Spike capacity on-demand. **80/20 kural**: Workload'ın %80'i reserve, %20 on-demand/spot.

### Spot / Preemptible

| | Discount | Risk |
|---|---|---|
| AWS Spot | 60-90% | 2 dakika önceden notification |
| GCP Preemptible | 60-91% | 24 saat max lifetime |
| Azure Spot | 60-90% | Eviction notification |

✅ Stateless batch, ML training, CI runner.
❌ Stateful production-critical (DB, customer-facing API tek).

---

## 5. Compute Optimizasyonu

### Right-sizing

> CPU < %20, memory < %40 ise → smaller instance.

Tools: AWS Compute Optimizer, GCP Recommender, Azure Advisor, Densify.

### Auto-scaling

- HPA (Horizontal Pod Autoscaler) — CPU, memory, custom.
- Cluster Autoscaler — node count.
- Karpenter — bin-packing aware (AWS).
- Scale to **zero** weekend / off-hours dev env.

### Container density

```
Bigger instance, multiple workload → 2-3x density.
Bin-packing efficient (Kubernetes scheduler, Karpenter).
```

### Architecture choices

| Architecture | Cost crossover (örnek) |
|---|---|
| Lambda | < 5M req/ay ucuz |
| Container | 5M-100M req/ay |
| Reserved EC2 | 100M+ req/ay sustained |

> Detay: [karar-cercevesi-matrisleri.md](karar-cercevesi-matrisleri.md) (compute karar matrisi).

### ARM (Graviton, Ampere)

> 20-40% daha ucuz, **çoğu workload** için aynı performans (CPU-bound, JIT'li runtime).

Migration cost: container rebuild (multi-arch).

### CPU pinning, NUMA awareness

Yüksek-perf workload için kernel-level tuning. Marjin var ama complex.

---

## 6. Storage Optimizasyonu

### Tier'lar (S3 örneği)

| Tier | Cost / GB / mo | Retrieval |
|---|---|---|
| Standard | $0.023 | Anlık |
| Standard-IA | $0.0125 | Anlık (retrieval fee) |
| One Zone-IA | $0.01 | Anlık (single AZ) |
| Glacier Instant | $0.004 | Anlık |
| Glacier Flexible | $0.0036 | Dakikalar-saatler |
| Glacier Deep Archive | $0.00099 | 12 saat |

### Lifecycle policy

```yaml
- 30 gün sonra → Standard-IA
- 90 gün sonra → Glacier
- 365 gün sonra → Deep Archive
- 7 yıl sonra → delete
```

> 30 günde nadir erişilen dosya → IA tier'a kaydır → **%50** tasarruf.

### Intelligent-Tiering

> S3 Intelligent-Tiering: Erişim deseni gözlemler, otomatik tier'lar. Monitoring fee var ama kuralları manage etme yükü ortadan kalkar.

### Block storage (EBS)

- gp2 → gp3 migration (daha hızlı + %20 daha ucuz).
- Snapshot lifecycle (eski snapshot delete).
- Unattached volume cleanup.

### Database storage

- Postgres bloat (vacuum + pg_repack).
- Old replica cleanup.
- Backup retention policy.

---

## 7. Network / Egress Tuzakları

### Cross-AZ traffic

```
AZ-a → AZ-b: $0.01/GB IN + $0.01/GB OUT = $0.02/GB
1 PB cross-AZ aylık = $20,000
```

### Internet egress

| Provider | Egress (US) |
|---|---|
| AWS | $0.09/GB (first 10TB) |
| GCP | $0.12/GB |
| Azure | $0.087/GB |
| Cloudflare R2 | $0 (zero egress!) |

> **Strateji**: CDN ile origin egress azalt. Multi-cloud için Cloudflare R2 yatırımları.

### NAT Gateway

```
$0.045 / hour + $0.045 / GB processed
1TB/gün → ~$1,400/month per NAT GW
```

> **Optimization**: VPC Endpoint (S3, DynamoDB) — NAT bypass, ücretsiz.

### Data transfer ücret modelleri

- Same AZ: free (genelde).
- Same region cross-AZ: $0.01/GB her yön.
- Same region same service (örn S3): free.
- Cross-region: $0.02/GB.
- Internet egress: $0.05-0.12/GB.
- VPN / Direct Connect: pricing different.

---

## 8. Veritabanı Maliyeti

### RDS / managed DB

- Reserved instance %50+ tasarruf.
- Storage auto-scaling (gerekenden fazla provision etme).
- Backup retention policy.
- Read replica only when needed (not "her zaman 3 replica").

### DynamoDB

| Mode | Use case |
|---|---|
| **Provisioned** | Predictable, sustained → reservation %50+ |
| **On-demand** | Variable, sporadic |

> On-demand'ı sürekli %50+ utilize ediyorsan provisioned'a geç → **5-10x** ucuzlama.

### Snowflake / BigQuery

- **Compute** (warehouse / slot) zaman bazlı.
- Auto-suspend kısa (60s).
- Multi-cluster only when needed.
- Result cache leverage.
- Materialized view for repeated query.

### Cache layer

- Redis/ElastiCache pahalı per-GB.
- Cache hit ratio ölç → düşük → cache yarar yok, kapat.
- TTL düşük tut (working set size).

---

## 9. Observability Maliyeti

### Datadog şok faturası

> Coinbase, Datadog'a aylık \$65M (2022) ödediğini açıkladı.
> "We pay more for observability than for compute" — yaygın org sorunu.

### Maliyet driverleri

- **Log volume**: Datadog \$0.10/GB ingest + retention.
- **Metric cardinality**: Per-host metric N hosts × M metrics × T intervals.
- **APM trace**: Per-trace pricing.
- **Custom metric**: Ekstra ücret.

### Optimization

- **Log sampling**: Debug %1, info %10, error %100.
- **Metric cardinality**: User-id label = explosion. Label disiplin.
- **Trace sampling**: Tail-based (errors %100, success %1-10).
- **Retention**: 30d hot + 90d cold + 1yr archive (S3 Glacier).
- **Self-host alternative**: Loki + Mimir + Tempo + Grafana — operational overhead, ama %90 cheaper.

### Logging anti-pattern

```python
logger.info(json.dumps(massive_object))  # 50KB log line
# 1M req/day × 50KB = 50GB/day = 1.5TB/month = $150/month sadece bu satır
```

**Çözüm:** Structured + selective + sampled.

---

## 10. Showback vs Chargeback

### Showback

> Her ekip kendi maliyetini **görür**, fatura yapılmaz. "Awareness".

### Chargeback

> Her ekip kendi maliyetini **öder** (internal billing). "Accountability".

| | Showback | Chargeback |
|---|---|---|
| Implementation | Tagging + dashboard | Tagging + budget + finance |
| Behavior change | Orta | Güçlü |
| Org maturity | Erken | İleri |
| Side effect | "İlginç ama benim sorunum değil" | Optimize zorla, ama gaming riski |

### Tagging strategy

```yaml
required-tags:
  - team: payments
  - environment: prod | staging | dev
  - service: order-service
  - cost-center: 1234
  - owner: ayse@example.com
```

Untagged resource → policy deny veya auto-tag.

---

## 11. Anti-Pattern'ler

### 1. "Cloud auto-scales, we don't worry"

Auto-scale ↑ trafiği takip eder, ama **alt sınır** yoksa idle resource maliyeti devam.

**Çözüm:** Auto-scale + scheduled scaling (off-hours).

### 2. "Reserved instance commit'imiz var, kullanmasak ne olur?"

Reserved instance commit edildi → kullansan da kullanmasan da öderiz. **Underutilization yıllık \$10K-100K kayıp**.

**Çözüm:** Convertible RI, Savings Plan (esnek). Ya da AWS RI marketplace'ten sat.

### 3. "Test ortamı 7/24 çalışır"

Dev/staging cluster cuma 18:00 - pazartesi 09:00 arası bekleme = 63 saat boş × 168 saat / hafta = **%37.5 idle**.

**Çözüm:** Off-hours auto-stop. KEDA + scheduler.

### 4. NAT Gateway her şey için

AWS örneği: VPC Endpoint S3 free. Aynı trafiği NAT GW'tan göndermek ücretli.

**Çözüm:** Common services için VPC Endpoint.

### 5. Logging = "everything"

"Belki gelecekte gerekir" → log volume 10x, fatura 10x.

**Çözüm:** Sampled logging, retention policy, cold tier archive.

### 6. Backup strategy yanlış

`pg_dump` her gece full → her gün artıyor. 1 yıl sonra dev env Postgres > prod.

**Çözüm:** Incremental, snapshot dedup, retention policy.

### 7. Kafka cluster oversized

3 broker, 10 partition, 1GB throughput → ama 100MB kullanılıyor.

**Çözüm:** Right-size, MSK Serverless evaluate.

### 8. CloudWatch Logs all the things

> CloudWatch Logs ingestion \$0.50/GB. 100GB/gün = \$15K/ay.

**Çözüm:** Critical only CloudWatch'a, geri kalanı S3 + Athena.

### 9. Cost gate yok

PR review'da "bu özellik aylık \$5K maliyet" tartışması yapılmıyor.

**Çözüm:** Design doc'ta "Cost analysis" zorunlu bölüm. ([rfc-design-doc-sablon.md](../templates/rfc-design-doc-sablon.md))

### 10. "Engineer time'ım pahalı, infra'ya bakmaya değmez"

> Senior \$200/saat. \$10K/ay tasarruf 50 saatlik iş ödüyor. ROI 12x ilk yıl.

**Çözüm:** FinOps **engineering** problemidir, sürekli yatırım.

---

## 🎯 Staff+ FinOps Kontrol Listesi

### Servis tasarımı

- [ ] Cost analysis design doc'ta var mı?
- [ ] Unit economics (cost per request/user) hesaplandı mı?
- [ ] Right-sized instance / pod resource?
- [ ] Auto-scale + min/max tanımlı?
- [ ] Reserved/savings plan değerlendirildi mi (steady state)?
- [ ] Storage tiering policy?
- [ ] Backup retention?
- [ ] Log sampling strategy?
- [ ] Tag'ler set (team, env, service)?

### Operasyon

- [ ] Daily cost report ekipte?
- [ ] Anomaly alert (sudden spike)?
- [ ] Budget threshold (80%, 100%)?
- [ ] Quarterly right-sizing review?
- [ ] Idle resource cleanup automation?
- [ ] FinOps champion ekipte?

---

## 📚 İleri Okuma

- *Cloud FinOps* — J.R. Storment & Mike Fuller (FinOps Foundation co-founders, 2nd ed. 2023)
- FinOps Foundation framework (finops.org)
- AWS / GCP / Azure Well-Architected Framework — Cost Optimization pillar
- Corey Quinn — *Last Week in AWS* newsletter, blog
- *Designing Distributed Systems* — Brendan Burns (cost considerations)
- Vantage, CloudHealth, Spot.io blogs

> [⬅️ Pratik klasörü](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
