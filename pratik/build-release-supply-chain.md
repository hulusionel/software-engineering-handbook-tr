# 🏗️ Build, Release ve Supply Chain

> **"You don't have a CI/CD pipeline. You have a build system that you trust to varying degrees."**

Bu doküman modern build/release pipeline'ının disiplinini, supply chain güvenliğini, deployment stratejilerini kapsar.

---

## 📑 İçindekiler

1. [CI vs CD vs Continuous Deployment](#1-ci-vs-cd-vs-continuous-deployment)
2. [Build Determinism ve Reproducibility](#2-build-determinism-ve-reproducibility)
3. [Pipeline Tasarımı](#3-pipeline-tasarımı)
4. [Test Pyramid in Pipeline](#4-test-pyramid-in-pipeline)
5. [Artifact Management](#5-artifact-management)
6. [Container Image Hardening](#6-container-image-hardening)
7. [SLSA, SBOM, Sigstore](#7-slsa-sbom-sigstore)
8. [Deployment Stratejileri](#8-deployment-stratejileri)
9. [Feature Flag](#9-feature-flag)
10. [Database Migration in CI/CD](#10-database-migration-in-cicd)
11. [Anti-Pattern'ler](#11-anti-patternler)

---

## 1. CI vs CD vs Continuous Deployment

| | Tanım |
|---|---|
| **CI** (Continuous Integration) | Her commit'te merge + build + test |
| **CD** (Continuous Delivery) | Her başarılı build prod'a **gitmeye hazır** |
| **CD** (Continuous Deployment) | Her başarılı build prod'a **otomatik gider** |

> Çoğu org "CI/CD" derken Continuous Delivery'yi kasteder. Continuous Deployment cesaret + olgunluk gerektirir.

### Trunk-based development

- Tek `main` branch.
- Kısa ömürlü feature branch (saat-gün).
- Daily merge zorunlu.
- Feature flag ile incomplete feature ship.

> **Karşıt:** GitFlow (release/develop/feature/hotfix branch'leri) — çoğu modern org için **fazla karmaşık**.

### DORA Metrics (Google DevOps Research)

| | Elite | High | Medium | Low |
|---|---|---|---|---|
| **Deployment frequency** | On-demand | Daily-weekly | Weekly-monthly | Monthly+ |
| **Lead time** | < 1 hour | < 1 day | 1-7 days | 1-6 months |
| **Change failure rate** | 0-15% | 16-30% | 16-45% | 46-60% |
| **MTTR** | < 1 hour | < 1 day | < 1 week | 1+ week |

> Hedef: Elite'a doğru. Otomasyon + small batches.

---

## 2. Build Determinism ve Reproducibility

### Niye?

- Aynı kaynak + aynı toolchain → **bit-by-bit aynı** binary.
- Audit edilebilir.
- Tampering tespiti.
- Cache effective.

### Threats to determinism

- **Timestamp** binary'de.
- **Path embedding** (build path).
- **Random seed**.
- **Parallel order** (linker order).
- **Environment vars**.
- **Network access** (download during build).

### Hermetic builds

> Build sadece **ön-tanımlı inputs** kullanır. Network erişimi yok (dependencies pre-fetched).

- **Bazel** (Google) — hermetic by design.
- **Nix / Guix** — content-addressed pure builds.
- **Buck2** (Meta) — Rust-based, hermetic.

### Reproducible builds örneği

```bash
SOURCE_DATE_EPOCH=$(git log -1 --format=%ct) \
  go build -trimpath -ldflags="-buildid="
```

`SOURCE_DATE_EPOCH` env var → timestamp deterministic.

---

## 3. Pipeline Tasarımı

### Stage hierarchy

```
1. Lint + format        (saniyeler, fail fast)
2. Unit test            (dakikalar)
3. Build artifact       (dakikalar)
4. Integration test     (orta)
5. Security scan        (paralel)
6. SBOM + sign          (saniyeler)
7. Deploy to staging    (dakika)
8. Smoke + E2E test     (dakikalar)
9. Canary deploy        (dakikalar)
10. Rollout to prod     (dakikalar - saatler)
```

### Fail fast principle

- Hızlı + ucuz testler önce.
- Yavaş + pahalı testler sonra.
- Erken fail → developer feedback hızlı.

### Pipeline as code

```yaml
# .github/workflows/ci.yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm test
      - run: npm run build
```

> CI config kod ile yönetilir, review edilir.

### Parallel jobs

- Test parçalama (Jest workers, pytest-xdist, Go test parallel).
- Matrix build (multiple OS, language versions).
- Independent stages.

### Caching

- Dependency cache (`node_modules`, `~/.m2`, `~/.cargo`).
- Docker layer cache.
- Build artifact cache (Bazel, Buck).
- 5-30x speedup.

---

## 4. Test Pyramid in Pipeline

```
       ▲    E2E (1-10)         ← prod-like, pahalı
      ▲▲    Integration (10-100)
    ▲▲▲▲    Unit (100-10000)   ← hızlı, ucuz, çok
```

### Hangi stage'de hangisi?

| Test tipi | Pipeline stage |
|---|---|
| Unit | Pre-merge |
| Lint, format, type check | Pre-merge |
| Static analysis | Pre-merge |
| Integration (component) | Pre-merge |
| API contract | Pre-merge |
| Security scan (SAST) | Pre-merge |
| Dependency scan | Pre-merge |
| Container scan | Post-build |
| End-to-end | Pre-deploy staging |
| Smoke test | Post-deploy |
| Performance test | Periodic |
| Penetration test (DAST) | Periodic |
| Chaos test | Periodic |

### Mutation testing

> **Stryker, Pitest** — kodda mutasyon yapar, test fail etmezse → testler **etkisiz**.

Real coverage > line coverage.

### Contract testing

> Pact, Spring Cloud Contract — provider/consumer kontratı sürekli doğrulanır.
> E2E'nin %80'ini ortadan kaldırır.

---

## 5. Artifact Management

### Niye registry?

- Versiyonlu storage.
- Permission, audit.
- Vulnerability scan.
- Cleanup policy.

### Yaygın tools

| Tip | Tool |
|---|---|
| **Docker images** | Docker Hub, Harbor, ECR, GCR, ACR, Quay |
| **Maven/Gradle** | Maven Central, JFrog Artifactory, Nexus |
| **npm** | npm registry, Verdaccio |
| **PyPI** | PyPI, devpi |
| **Universal** | JFrog Artifactory, Sonatype Nexus |
| **Generic blob** | S3 + index |

### Versioning

- **Semantic Versioning** (MAJOR.MINOR.PATCH).
- **Calendar Versioning** (2024.10.15) — release-driven products.
- **Git SHA** + tag — immutable build reference.

### Immutability

- ✅ Tag'i **asla** üzerine yazma.
- ✅ "latest" tag dev için, prod'a `v1.2.3-abc1234`.
- ✅ Pull-by-digest (`sha256:...`) en güvenli.

### Retention

- Latest 10-30 build keep.
- Tagged release sonsuz.
- Periodic cleanup (cost).

---

## 6. Container Image Hardening

### Minimal base

| Base | Boyut | Trade-off |
|---|---|---|
| `ubuntu:22.04` | ~78 MB | Geniş tooling, fazla attack surface |
| `debian:slim` | ~80 MB | Hafif |
| `alpine` | ~7 MB | Çok küçük, musl libc (compat issues) |
| `distroless` | ~20 MB | No shell, no package manager |
| `scratch` | 0 MB | Static binary only |

> **Production tavsiye:** Distroless veya scratch (Go, Rust statik binary).

### Multi-stage build

```dockerfile
# Stage 1: build
FROM golang:1.22 AS builder
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o app

# Stage 2: minimal runtime
FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=builder /src/app /app
USER nonroot:nonroot
ENTRYPOINT ["/app"]
```

### Best practices

- ✅ Pin base image digest (`@sha256:...`).
- ✅ Non-root user.
- ✅ Read-only root filesystem.
- ✅ Drop all capabilities (K8s `securityContext`).
- ✅ No secret in layer.
- ✅ `.dockerignore` for sensitive files.
- ✅ Image scanning (Trivy, Grype, Snyk) CI'da.

### Layer caching

```dockerfile
# ✅ Dependencies first (rarely change)
COPY package*.json ./
RUN npm ci

# Source code last (often change)
COPY . .
RUN npm run build
```

---

## 7. SLSA, SBOM, Sigstore

### SLSA (Supply-chain Levels for Software Artifacts)

| Seviye | Garanti |
|---|---|
| L1 | Build script var, provenance var |
| L2 | Hosted build, signed provenance |
| L3 | Hardened build (isolated, hermetic), tamper-evident |
| L4 | Two-party review, hermetic build, reproducibility |

### SBOM (Software Bill of Materials)

> Yazılımdaki **tüm** dependency'lerin listesi.

Formatlar:
- **SPDX** (Linux Foundation).
- **CycloneDX** (OWASP).

```bash
syft myimage:v1 -o spdx-json > sbom.json
syft myimage:v1 -o cyclonedx-json
```

> US Executive Order 14028 (2021) — federal kontrat için SBOM zorunlu.

### Sigstore / cosign

> Keyless signing using OIDC identity.

```bash
# Sign
cosign sign --yes ghcr.io/myorg/app@sha256:abc...

# Verify
cosign verify --certificate-identity ... \
  --certificate-oidc-issuer https://accounts.google.com \
  ghcr.io/myorg/app:v1
```

Components:
- **Fulcio**: Ephemeral cert from OIDC identity.
- **Rekor**: Transparency log (append-only, signed).
- **Cosign**: Sign/verify CLI.

### Supply chain saldırı örnekleri

- **SolarWinds 2020** — build pipeline injection.
- **event-stream 2018** — npm maintainer takeover.
- **ua-parser-js 2021** — npm account takeover.
- **3CX 2023** — supply chain double-compromise.
- **xz utils 2024** — multi-year insider attack.

---

## 8. Deployment Stratejileri

### Karşılaştırma

| Strateji | Risk | Cost | Rollback |
|---|---|---|---|
| **Big Bang** | Yüksek | Düşük | Yavaş |
| **Rolling** | Orta | Düşük | Yavaş |
| **Blue-Green** | Düşük | 2x infra | Anında |
| **Canary** | Düşük | Orta | Hızlı |
| **Shadow** | Çok düşük | 2x infra | N/A (test) |

### Rolling deployment

- N pod sırayla yeni version'a geçer.
- K8s default `RollingUpdate`.
- `maxSurge=1, maxUnavailable=0`.
- Slow but safe.

### Blue-Green

```
Blue (current prod) ── traffic
Green (new version) ── idle, health check

Switch: traffic → Green
Rollback: traffic → Blue (saniyeler içinde)
```

✅ Anında rollback.
❌ 2x infra ücreti.
❌ DB migration zorlu (schema sync).

### Canary

```
v1 (95%) ── prod
v2 (5%) ── small subset

Monitor: error rate, latency, business metric.
If healthy: 5% → 25% → 50% → 100%
If bad: rollback to 0%.
```

> **Otomatik canary**: Metric-based promotion (Argo Rollouts, Flagger, Spinnaker).

### Shadow / Dark Launch

> Yeni version eski ile **paralel** çalışır, kullanıcıya sadece eski cevap verir. Yeni'nin output'u logged + compare.

Use case: yüksek-risk migration, ML model A/B.

### Progressive delivery

> Canary + feature flag + observability + auto-rollback. Modern term.

---

## 9. Feature Flag

### Niye?

- Deployment ↔ Release decouple.
- Trunk-based development enabler.
- A/B test.
- Kill switch.
- Gradual rollout.

### Tools

- **LaunchDarkly** — premier SaaS.
- **Unleash** — open-source.
- **Flagsmith** — open-source.
- **Split** — experimentation focus.
- **ConfigCat** — basit.
- **GrowthBook** — open-source experimentation.

### Flag tipleri

| Tip | Lifetime | Örnek |
|---|---|---|
| **Release** | Kısa (gün-hafta) | New feature gradual rollout |
| **Experiment** | Orta (haftalar) | A/B test |
| **Ops** | Sonsuz | Kill switch, throttle |
| **Permission** | Sonsuz | Beta access |

### Best practices

- ✅ Flag **kısa ömürlü** (release tipi). 30-90 gün sonra sil.
- ✅ Flag debt kontrolü (eski flag'ler temizlik).
- ✅ Default value = current behavior.
- ✅ Flag config audit + change log.
- ✅ Feature flag test'leri (on + off path).

### Anti-pattern: flag hell

```
if (flagA && flagB && !flagC) { ... }
else if (flagA && !flagB) { ... }
else if (!flagA && flagD) { ... }
```

→ Cyclomatic complexity patlar. Aggressive cleanup zorunlu.

---

## 10. Database Migration in CI/CD

### Expand-Contract Pattern

> Schema değişikliğini **2 deploy** ile yap:

```
Deploy 1 (Expand):
  - Yeni kolon ekle (nullable)
  - Eski + yeni kolonu yaz (dual-write)
  - Backfill historical

Deploy 2 (Contract):
  - Yeni kolonu okumaya geç
  - Dual-write durdur
  - Eski kolonu sil
```

> **Migrations always backward-compatible** (in-flight request'ler eski schema bilebilir).

### Online schema change

- **gh-ost** (GitHub) — MySQL.
- **pt-online-schema-change** (Percona) — MySQL.
- **pgroll** (Xata) — Postgres expand-contract.

> Lock-free large table migration. Saatler süren ALTER TABLE'ı online yap.

### CI'da migration test

- Test DB'de migration apply.
- Rollback test.
- Backward compat smoke test (eski version'la).

### Anti-pattern: irreversible migration

```sql
-- ❌ Bir defa silersen geri alamazsın
DROP COLUMN sensitive_data;
```

→ Önce nullable yap, deploy, monitor, sonra drop (next sprint).

---

## 11. Anti-Pattern'ler

### 1. Pipeline yok, "git pull && restart"

Production'a manuel deploy. **Tutarsız, izlenmez, geri alınamaz.**

**Çözüm:** Standart CI/CD.

### 2. Long-lived feature branches

3 ay yaşayan branch → merge cehennemi.

**Çözüm:** Trunk-based + feature flag.

### 3. Pre-prod ≠ prod

Prod RDS, pre-prod local SQLite. **Test sonuçları değersiz.**

**Çözüm:** Production-parity (managed DB, real services).

### 4. Manual approval everywhere

Her deploy 5 onay → DORA metrics çöker.

**Çözüm:** Otomasyon + canary + auto-rollback. Onay sadece prod sensitive change'lere.

### 5. Test on prod via "soft launch"

Diğer adıyla "kullanıcı test eder."

**Çözüm:** Pre-prod test rigor + production observability.

### 6. Cron'la deploy

`0 2 * * * deploy.sh` — gece kimse görmüyor → bug görünmez.

**Çözüm:** Business hours deploy (canary güvenli kıldıkça). Cuma deploy yasağı **fear smell** — confidence düşük.

### 7. "Build artifact'i biz mi yoksa CI mi?"

Local build + manual upload → "works on my machine".

**Çözüm:** Single source of truth: CI build = release.

### 8. Secret in pipeline log

```
echo $DB_PASSWORD  # CI log'una sızar
```

**Çözüm:** Masked secret, secret manager integration.

### 9. CI/CD as auth bypass

> Engineer prod'a SSH yapamıyor ama CI deploy edebiliyor → kişi pipeline'a kötü PR yazar → prod'a dolaylı erişim.

**Çözüm:** PR review zorunlu, branch protection, CODEOWNERS.

### 10. No deployment metadata

> Hangi commit prod'da? Bilinmiyor.

**Çözüm:** Deploy event → metric + log. `/version` endpoint git SHA döndürür.

---

## 🎯 Staff+ Deployment Kontrol Listesi

### Servis için

- [ ] CI pipeline kod olarak versionlu mu?
- [ ] Trunk-based + feature flag pattern?
- [ ] Pre-merge: lint + unit + integration test?
- [ ] Build deterministic + reproducible?
- [ ] Container hardened (non-root, distroless, scan)?
- [ ] SBOM + signing?
- [ ] Canary / blue-green strategy yazılı?
- [ ] Auto-rollback metric'lere bağlı?
- [ ] DB migration expand-contract pattern?
- [ ] Production observability (deploy event tracking)?
- [ ] DORA metrics ölçülüyor mu?

### Org için

- [ ] Trunk-based standardı?
- [ ] Branch protection (CODEOWNERS, required checks)?
- [ ] Secret manager (no hardcode)?
- [ ] Vulnerability scanning policy?
- [ ] Pipeline access control (kim deploy edebilir)?
- [ ] Audit log (deploy events)?

---

## 📚 İleri Okuma

- *Continuous Delivery* — Humble & Farley (klasik)
- *Accelerate* — Forsgren, Humble, Kim (DORA research)
- *Software Engineering at Google* — Winters, Manshreck, Wright
- *DevOps Handbook* — Kim, Humble, Debois, Willis
- SLSA framework (slsa.dev)
- *Securing the Software Supply Chain* — NIST SP 800-218
- Sigstore docs

> [⬅️ Pratik klasörü](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
