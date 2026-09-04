# 🚦 SRE Pratiği

> **"Hope is not a strategy."** — Google SRE Book

Bu doküman SRE'nin (Site Reliability Engineering) **işlevsel disiplinini** kapsar: SLO tanımı, error budget yönetimi, toil ölçümü, on-call kültürü, incident management.

---

## 📑 İçindekiler

1. [SRE Felsefesi](#1-sre-felsefesi)
2. [SLI, SLO, SLA Üçgeni](#2-sli-slo-sla-üçgeni)
3. [Error Budget](#3-error-budget)
4. [Toil Ölçümü ve Azaltma](#4-toil-ölçümü-ve-azaltma)
5. [On-Call Kültürü](#5-on-call-kültürü)
6. [Incident Management](#6-incident-management)
7. [Capacity Planning](#7-capacity-planning)
8. [Chaos Engineering](#8-chaos-engineering)
9. [Observability — 3 Pillar + 1](#9-observability--3-pillar--1)
10. [Reliability Anti-Pattern'leri](#10-reliability-anti-patternleri)

---

## 1. SRE Felsefesi

### Temel ilke

> **"SRE = Software Engineering for Operations"**
> — Google'ın 2003'te Ben Treynor Sloss tarafından kurulmuş ekip felsefesi.

### Klasik Ops vs SRE

| Klasik Ops | SRE |
|---|---|
| Ticket-driven | Engineering-driven |
| Manuel iş normalleşmiş | Manuel iş **kabul edilmez** (toil < %50) |
| %100 uptime ideal | %100 yanlış hedef, error budget |
| "Daha çok çalışan" çözüm | "Daha çok automation" çözüm |
| Dev ↔ Ops siloları | Shared on-call, shared incentives |
| Reactive | Proactive (SLO, capacity, chaos) |

### Temel SRE prensipleri

1. **Embrace risk** — %100 yanlış hedef.
2. **SLO'lar kararı yönlendirir** — fikir değil, sayı.
3. **Toil'u azalt** — engineering investment.
4. **Monitoring** — symptom, cause değil.
5. **Automation** — eventually consistent automation.
6. **Release engineering** — gradual, reversible.
7. **Simplicity** — boring teknoloji.
8. **Postmortem culture** — blameless.

---

## 2. SLI, SLO, SLA Üçgeni

### Tanımlar

| | Anlam | Kim için? |
|---|---|---|
| **SLI** (Indicator) | Ölçülen şey | Internal |
| **SLO** (Objective) | Hedef | Internal — ekipler arası |
| **SLA** (Agreement) | Sözleşmede vaad | External — müşteri |

> **Pratik kuralı:** SLA < SLO < gerçek performans.
> Örnek: Gerçek %99.95 → SLO %99.9 → SLA %99.5.

### İyi bir SLI

- ✅ **Kullanıcının** etkilendiği bir şey ölçer.
- ✅ Sayısal, ölçülebilir.
- ✅ "Good event / total event" oranı.
- ❌ Sistem-iç metric (CPU, memory) **SLI değil**.

### Yaygın SLI tipleri

| Tip | Örnek |
|---|---|
| **Availability** | Successful requests / total requests |
| **Latency** | Requests faster than X / total |
| **Throughput** | Requests handled / requests offered |
| **Quality** | Full quality response / total |
| **Freshness** | Data within freshness target / total |
| **Correctness** | Successful tx / attempted tx |

### SLO örneği

```
SLO: Checkout API
  - Availability: 99.95% over rolling 28 days
    SLI = (2xx + 3xx + 4xx) / total
    (5xx hata sayılır, 4xx user hatası sayılmaz)

  - Latency: 99% of requests < 500ms over rolling 28 days
    SLI = count(latency < 500ms) / count(total)
```

### Multiwindow / Multiburn alerting

> Klasik "5 dakikadır error rate > %1" alertı **gecikir** veya **flapping**.

**Modern:** Multi-window burn rate (Google SRE Workbook 2018):

```
Page if:
  (1h burn rate > 14.4 AND 5m burn rate > 14.4)
  OR (6h burn rate > 6 AND 30m burn rate > 6)
```

- Hızlı tüketimde hızlı uyarı.
- Yavaş tüketimde yavaş uyarı.
- False positive azalır.

---

## 3. Error Budget

> **Error budget = (1 - SLO) × time window.**

```
SLO 99.9% / 28 gün
   = 0.001 × 28 × 24 × 60 = 40.32 dakika downtime izni
```

### Niye budget?

> Reliability ↔ velocity arasında **bilinçli trade-off**.

- Budget kalmışsa → yeni feature ship et, risk al.
- Budget tükendiyse → freeze, reliability'e yatırım.

### Error budget policy

```yaml
# Örnek policy
when_budget_remaining > 50%:
  - normal feature velocity
  - canary 1% → 10% → 50% → 100%

when_budget_remaining 10-50%:
  - feature freeze değil, ama reliability work önceliği
  - canary daha yavaş

when_budget_remaining < 10%:
  - feature freeze (sadece reliability fix)
  - all hands postmortem review
  - SLO target review
```

### Error budget burn rate

```
Burn rate = budget consumed / budget total × time fraction
   1.0  = on track to exhaust at end of window
   2.0  = 2x faster, will exhaust in half time
  14.4  = will exhaust 1h budget in (60/14.4) = 4.2 minutes
```

### "Borrowing" budget

- Major release sonrası kısa süreli artış kabul edilebilir.
- Ama uzun vadede (90 gün) ortalama SLO'ya dön.

---

## 4. Toil Ölçümü ve Azaltma

### Toil tanımı (Google)

> Manuel, repetetif, otomatize edilebilir, taktik (stratejik değil), ölçek dışı, **scale ile lineer büyüyen** iş.

### Toil örnekleri

- Manuel deployment.
- Manuel cluster yeniden boyutlandırma.
- Belirli bir metrik aşıldığında manuel restart.
- Aynı pattern'de ticket cevaplama.
- Periodic certificate renewal.

### NOT toil

- Engineering: yeni framework, automation, tooling.
- Project work.
- Postmortem yazımı (one-off).
- Documentation.
- On-call (managed scope).

### Toil ölçümü

```
Toil hours / total hours per quarter
   Hedef: < %50 (Google SRE)
   > %50 → ekip mühendis değil, operatör
```

### Toil reduction stratejileri

1. **Eliminate**: Sebebi ortadan kaldır.
2. **Automate**: Script + scheduler.
3. **Self-service**: Kullanıcı kendi yapsın (runbook, UI).
4. **Source of truth fix**: Manuel update gerektiren alan = kötü tasarım.

### "Engineering Time" budget

> Quarterly:
> - Project work: %50
> - On-call: %25
> - Toil: %25 (tolerated)

> Toil > %50 olursa **stop the line** — yeni iş alma, automation'a yatırım.

---

## 5. On-Call Kültürü

### On-call'un anlamı

- 🚨 Production incident'lara cevap.
- 📞 Çağrıya **15 dakikada** cevap (genelde).
- 🛡️ "Last line of defense."

### Sürdürülebilir on-call

- ✅ **Rotasyon**: 6+ kişilik havuz.
- ✅ **Vardiya**: Haftalık veya 2-haftalık.
- ✅ **Follow-the-sun**: Globally distributed (US/EU/APAC).
- ✅ **Compensation**: Salary, time off, premium.
- ✅ **Page volume cap**: Vardiya başına < 2 page (kabul). > 5 = bug.

### On-call ≠ "Tüm ticket'lara bak"

- 🚨 Page = aksiyon gereken, gerçek olay.
- ✉️ Ticket = office hours.
- 💬 Slack mesaj = best effort.

### Run-book ne zaman?

> Her **page** için run-book:
> 1. Bu alert ne anlama geliyor?
> 2. İlk yapılacak: dashboard X bak.
> 3. Şu komutla kontrol et: `kubectl ...`.
> 4. Eğer Y'yse → mitigate (rollback, scale, restart).
> 5. Yardım: kim arar (escalation).

### Handoff

- Vardiya sonu meeting (15-30 dk).
- Aktif incident'lar.
- Ongoing investigation.
- Risk göstergeleri.
- Slack #ops-handoff dokümante.

---

## 6. Incident Management

### Severity sınıflandırma

| | Tanım | Response |
|---|---|---|
| **SEV-1** | Major user impact (50%+) | Tüm ekip, exec aware |
| **SEV-2** | Significant impact (degraded) | On-call + senior |
| **SEV-3** | Minor impact, workaround var | On-call |
| **SEV-4** | No user impact, internal | Office hours |

### Incident roller

| Rol | Sorumluluk |
|---|---|
| **IC** (Incident Commander) | Koordinasyon, kararlar |
| **Communications Lead** | Status page, internal comms |
| **Operations Lead** | Mitigation actions |
| **Subject Matter Experts** | Spesifik domain |
| **Scribe** | Timeline keep |

> **Tek kişi her şeyi yapamaz.** SEV-1'de role split zorunlu.

### Incident response timeline

```
T+0       Alert fires
T+1m      On-call ack
T+5m      First mitigation attempt
T+10m     Determine: rollback vs forward fix
T+15m    Status page update
T+30m    Stable → declare resolved
T+1h      Initial postmortem outline
T+72h     Full blameless postmortem published
T+1 week  Action items being tracked
```

### "Mitigate first, debug later"

> Hata ayıklamak için **production'ı çalışır halde** tutmaya öncelik ver.
> Rollback ucuzsa **rollback**. Sonra debug.

### Status page disiplini

- Müşteri-yönelik durum sayfası (statuspage.io, Atlassian Statuspage).
- Update sıklığı: incident süresince **30 dk içinde**.
- Tone: net, az teknik, "we're aware, investigating, mitigating, resolved".
- Postmortem link'i public (şeffaflık trust kurar).

### Postmortem disiplin

> Detaylar: [templates/postmortem-sablon.md](../templates/postmortem-sablon.md), [postmortem-arsivi.md](postmortem-arsivi.md).

- Blameless.
- Timeline, root cause, contributing factors.
- Action items (sahibi + tarihi).
- 72h içinde draft, 1 hafta içinde final.

---

## 7. Capacity Planning

### Niye?

- Yeterli kaynak: SLO sağlanır.
- Çok kaynak: para ziyan.
- Az kaynak: incident.

### Forecasting

```
Önümüzdeki 6 ay yük tahmini:
   Mevcut traffic × büyüme oranı × seasonality × campaign uplift
```

- Linear extrapolation (basit).
- Exponential fit (büyüme aşaması).
- ARIMA, Prophet (daha sofistike).

### Headroom

> **Steady state**: %50-70 utilization. SLO koruyabilmek için headroom (40-50%) gerekli.

```
Capacity needed = peak load / target utilization
   peak = 8K req/s, target = 0.7 → capacity = 11.5K
```

### Vertical vs horizontal

- **Vertical**: Daha güçlü makine (limit var).
- **Horizontal**: Daha çok makine (state'siz servis için).

### Auto-scaling

- HPA (Horizontal Pod Autoscaler) — CPU, memory, custom metric.
- Cluster Autoscaler — node count.
- KEDA (event-driven) — Kafka lag, queue depth.
- ⚠️ Cold start latency — pre-warming.
- ⚠️ Cooldown period — flapping önleme.

### Capacity test (load test)

- Periyodik (ayda bir) production'a gerçek-yük testi.
- "Game day" — hedeflenen pik load.
- Netflix Chaos Monkey + Performance Test.

---

## 8. Chaos Engineering

> **"Hypothesis-driven experimentation in production."** — Netflix Principles of Chaos

### Niye?

- Failure'lara hazır olmak için **failure simüle et**.
- Sistemin gerçek davranışını **test ortamında simulasyondan** öğrenemezsin.
- Confidence ölçeklendirilebilir hale getirir.

### Chaos hierarchy

```
1. Tek instance kill (basic)
2. AZ kayıp
3. Region kayıp
4. Network partition
5. Latency injection
6. Resource exhaustion (CPU, memory, disk)
7. Dependency failure (DB slow, cache down)
8. Clock skew
9. Combined failures
10. Chaos in production (advanced)
```

### Tools

- **Chaos Monkey** (Netflix) — random instance kill.
- **Gremlin** — managed chaos service.
- **Litmus / Chaos Mesh** — Kubernetes chaos.
- **Toxiproxy** — network failure.
- **stress-ng** — resource saturation.

### Game day

> Önceden planlı, ekipçe yapılan chaos egzersizi:
> 1. Hipotez yaz.
> 2. Senaryo seç.
> 3. Çalıştır.
> 4. Gözlemle (alert? recovery? user impact?).
> 5. Postmortem-style learning.

### Pre-conditions

- ✅ Observability iyi (alert, dashboard).
- ✅ Rollback / mitigation hazır.
- ✅ Blast radius sınırlı.
- ✅ Customer impact değerlendirildi.
- ❌ Production'da kaos için **olgunluk** gerekir; staging'de başla.

---

## 9. Observability — 3 Pillar + 1

### Klasik 3 pillar

| | Anlam |
|---|---|
| **Logs** | Discrete event records (timestamps, structured) |
| **Metrics** | Aggregated numerical (counters, gauges, histograms) |
| **Traces** | Request flow across services (spans, parent/child) |

### 4. pillar: Profiles

> Continuous profiling — production'da CPU/memory/lock profile. Pyroscope, Parca, Datadog.

### Charity Majors'ın rüyası

> *"3 pillar yanlış metafor. Observability arbitrary cardinality + arbitrary dimensions ile sorgulanabilir bilgidir."*

→ **Wide events** (high-cardinality structured logs) + arbitrary query → her debug session farklı boyut.

### Cardinality dikkat

- Metrics low cardinality (10K-100K series limit).
- Logs/traces high cardinality.
- "Per-user metric" → metric explosion → traces tercih.

### Best practices

- **Structured logging** (JSON), not plain text.
- **Trace context** (W3C `traceparent`) tüm zincirde.
- **Correlation IDs**: trace_id, request_id, user_id (logs ↔ traces ↔ metrics).
- **RED/USE** dashboard hierarchy.
- **SLO dashboard** (top of stack).

### OpenTelemetry standardı

- Vendor-neutral SDK + protocol.
- Backend: Jaeger, Tempo, Datadog, New Relic, Honeycomb.
- 2024+ baskın standart.

---

## 10. Reliability Anti-Pattern'leri

### 1. %100 SLO

```
Mühendis: "Sistemimiz %100 uptime hedefliyor."
SRE: "Bu hedef yanlış. Maliyet vs marjin sınırsız değil."
```

**Çözüm:** Realistic SLO (99.9-99.99 most services).

### 2. Cause-based alerting

> "CPU > %80 alert".
> Kim umursar? CPU yüksek olabilir; user etkilenmediyse sorun yok.

**Çözüm:** Symptom-based — "p99 latency > 500ms".

### 3. Runbook olmayan alert

> Page geldi → eldim eldim ne yapacağız? → Google → ...

**Çözüm:** Her alert + runbook. Runbook'suz alert silinir.

### 4. Hero firefighter

> Bir kişi her incident'i kendisi çözüyor.
> Bu kişi tatildeyse sistem çöker.

**Çözüm:** Knowledge sharing (postmortem, runbook), shared on-call.

### 5. "Just restart it"

> Memory leak → restart cron. **Bug fix değil.**

**Çözüm:** Root cause + fix. Restart tek tek workaround.

### 6. Untested DR plan

> Disaster Recovery plan var, ama test edilmiyor.

**Çözüm:** Yıllık DR drill (tabletop + actual failover).

### 7. SLO yok, ama "gözüm üstünde"

Subjektif. Tartışmalı. Kararsız.

**Çözüm:** Yazılı SLO + dashboard. Karar SLO'ya göre.

### 8. Postmortem yazılır, aksiyon takipsiz

Aksiyon listesi 6 ay sonra hâlâ açık → öğrenme yok.

**Çözüm:** Aksiyon JIRA/Linear'da, sahibi var, tarihi var, weekly review.

### 9. Alert fatigue

> 50 alert/gün, kimse okumuyor.

**Çözüm:** Alert review (haftalık), agresif silme. P0/P1 ayrımı.

### 10. "Test ortamında çalışıyor"

> Staging ≠ production. Yük, data volume, traffic pattern, dependency hep farklı.

**Çözüm:** Production-like test (gameday), canary, feature flag, gradual rollout.

---

## 🎯 Staff+ SRE Kontrol Listesi

### Servis launch öncesi

- [ ] SLI tanımlı (kullanıcı-yönelik)?
- [ ] SLO yazılı + dashboard?
- [ ] Error budget policy ekipte mutabık?
- [ ] Runbook her alert için var mı?
- [ ] On-call rotation kurulu, eğitim verildi mi?
- [ ] Postmortem template + takip mekanizması?
- [ ] Capacity headroom hesaplandı mı?
- [ ] Chaos test (en azından "instance kill") yapıldı mı?
- [ ] Rollback prosedürü test edildi mi?
- [ ] Monitoring 4 golden signal kapsıyor mu?
- [ ] Disaster Recovery plan + RTO/RPO?

### Quarterly review

- [ ] SLO compliance (geçen quarter)?
- [ ] Error budget kullanımı?
- [ ] Toil saatleri?
- [ ] Postmortem aksiyonları kapanma oranı?
- [ ] Page volume + on-call yükü?
- [ ] Chaos test sonuçları?

---

## 📚 İleri Okuma

### Birincil

- *Site Reliability Engineering* — Beyer, Jones, Petoff, Murphy (Google, 2016)
- *The Site Reliability Workbook* — Beyer et al. (2018)
- *Building Secure & Reliable Systems* — Adkins et al. (2020)
- *Seeking SRE* — David Blank-Edelman (2018)

### Modern

- *Implementing Service Level Objectives* — Alex Hidalgo
- *Observability Engineering* — Charity Majors, Liz Fong-Jones, George Miranda
- *Database Reliability Engineering* — Campbell & Majors

### Bloglar

- Google SRE blog
- Netflix Tech Blog
- Charity Majors (honeycomb.io)
- Brendan Gregg
- Increment magazine — on-call & SRE issues

> [⬅️ Pratik klasörü](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
