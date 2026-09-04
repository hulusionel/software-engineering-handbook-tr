# 🛰️ Modern Teknoloji Radarı

> **"Yeni" ile "olgun" arasındaki farkı bilmeyen mühendis, takıma teknik borç bırakır."**

Bu doküman 2024-2026 dönemini şekillendiren teknolojileri ThoughtWorks Tech Radar formatında sınıflandırır: **Adopt, Trial, Assess, Hold**.

---

## 📑 İçindekiler

1. [Tech Radar Disiplini](#1-tech-radar-disiplini)
2. [Programlama Dilleri](#2-programlama-dilleri)
3. [Sistem Yazılımı (eBPF, WASM)](#3-sistem-yazılımı-ebpf-wasm)
4. [Container, Orchestration, Service Mesh](#4-container-orchestration-service-mesh)
5. [Edge Computing](#5-edge-computing)
6. [Veri & ML Altyapısı](#6-veri--ml-altyapısı)
7. [LLM & GenAI Stack](#7-llm--genai-stack)
8. [DevEx & Productivity](#8-devex--productivity)
9. [Frontend Trendleri](#9-frontend-trendleri)
10. [Hold — Uzak Durulacaklar](#10-hold--uzak-durulacaklar)

---

## 1. Tech Radar Disiplini

### 4 ring

| Ring | Anlam |
|---|---|
| **Adopt** | Üretimde güvenle kullan |
| **Trial** | Düşük-risk projede dene |
| **Assess** | Takip et, anla |
| **Hold** | Yeni proje başlatma |

### 4 quadrant (ThoughtWorks)

- Languages & Frameworks.
- Tools.
- Platforms.
- Techniques.

### Org radar oluştur

- Ekipler kendi radar'ını yayınlar (yarım yıllık).
- "Trial" hedefi: %20 yeni şey denemek.
- "Hold" disiplinli — yenisi için eskiyi bırakma kabul edilmeli.

---

## 2. Programlama Dilleri

### Adopt

- **Rust**: Sistem yazılımı, performance-critical, güvenlik. Linux kernel desteği (2022+). Cloudflare, Discord, Microsoft, Meta üretimde.
- **Go**: Cloud-native standardı. Kubernetes, Docker, Terraform, etcd, CockroachDB, Hashicorp tüm stack.
- **TypeScript**: JS yerine **default seçim**. Frontend + Node backend.
- **Python 3.12+**: Veri, ML, scripting. PEP 703 (no-GIL) deneysel ama umut verici.
- **Java 21 LTS**: Virtual threads (Project Loom), pattern matching, records. Modern Java **çok farklı** eski Java'dan.
- **Kotlin**: JVM ekosistemi modernize. Android default.

### Trial

- **Zig**: C alternatif, comptime, no hidden control flow. Bun (Node alternatif) Zig ile yazıldı.
- **Mojo**: Python superset, AI/ML için optimize. 2023 lansmanı, Modular firma.
- **Gleam**: BEAM (Erlang VM) üstünde modern, type-safe.
- **Roc**: Functional, performance-focused. Henüz stable yok.

### Assess

- **Crystal**: Ruby-like syntax, compile-to-native.
- **Nim**: Python-like, performant.

### Hold

- **CoffeeScript** (TypeScript yendi).
- **Perl new project** (legacy maintenance OK).
- **JavaScript** for non-trivial new project (TypeScript kullan).

---

## 3. Sistem Yazılımı (eBPF, WASM)

### eBPF — Adopt

> **Extended Berkeley Packet Filter**. Kernel'da güvenli, sandboxed program çalıştırma.

**Use case:**
- Network observability (Cilium Hubble, Pixie).
- Security policy (Tetragon, Falco).
- Performance profiling (Pyroscope, Parca).
- Service mesh sidecar-less (Cilium Service Mesh).

**Niye trend?** Kernel modüle yazma riski olmadan kernel-level functionality.

### WebAssembly (WASM) — Adopt (browser), Trial (server)

> Browser'da binary format. WASI ile server-side de.

**Browser:** Adopt (Photoshop on web, Figma).

**Server-side / edge:**
- **Cloudflare Workers** (V8 isolates, native WASM).
- **Fastly Compute@Edge** (WASM native).
- **wasmCloud, Spin** — WASM-based microservice runtime.
- **Docker Desktop** WASM container support.

**Avantaj:** mikrosaniye cold start, dil bağımsız, sandbox.

### Unikernel — Assess

- **Unikraft** — modular unikernel framework.
- Use case: workload-specific minimal OS.
- Henüz mainstream değil.

---

## 4. Container, Orchestration, Service Mesh

### Adopt

- **Kubernetes**: De-facto orchestrator. EKS, GKE, AKS managed.
- **Helm** + **Kustomize** (combined).
- **Argo CD / Flux** — GitOps.
- **Cilium** — eBPF-based CNI, modern service mesh.
- **Karpenter** (AWS) — bin-packing aware autoscaler.
- **Tilt / Skaffold / Devspace** — local K8s dev loop.

### Trial

- **Crossplane** — Kubernetes API for cloud resources.
- **eBPF-based mesh** (Cilium without sidecar) — Istio/Linkerd alternative.
- **K8s Gateway API** (replaces Ingress).
- **Knative** — serverless on K8s.

### Assess

- **Wasm-based runtime** (Spin, wasmCloud) — K8s'siz container alternative.
- **Dapr** — microservice runtime sidecar abstraction.

### Hold

- **Helm v2** (deprecated long ago).
- **Custom K8s controller'ı framework olmadan** (operator-sdk, kubebuilder kullan).
- **Istio sidecar-based** new install (ambient mode evaluate).

---

## 5. Edge Computing

### Adopt

- **Cloudflare Workers** + R2 (zero egress) + D1 (SQLite).
- **Vercel Edge Functions** + KV.
- **Fastly Compute@Edge** (WASM).
- **AWS CloudFront Functions / Lambda@Edge**.

### Trial

- **DurableObjects** (Cloudflare) — global stateful objects.
- **Edge SQL** (Turso, Cloudflare D1) — SQLite at edge.
- **Region-less databases** (FaunaDB, PlanetScale, Neon).

### Use case eşlemesi

| Use case | Tool |
|---|---|
| A/B testing, geo routing | Workers, Lambda@Edge |
| Image transformation | Workers, ImageKit, Cloudinary |
| Auth at edge | Workers, OPA, Cloudflare Access |
| Real-time at edge | DurableObjects, PartyKit |
| Data at edge (read-heavy) | Edge SQL, R2 |

---

## 6. Veri & ML Altyapısı

### Adopt

- **Snowflake / BigQuery / Databricks** — cloud DW.
- **dbt** — SQL-first transformation.
- **Apache Iceberg** — open table format.
- **Apache Kafka** — event streaming default.
- **Apache Flink** — stream processing.
- **Postgres + extensions** (pgvector, TimescaleDB) — multi-purpose.
- **DuckDB** — local OLAP, lightweight.
- **ClickHouse** — column store, fast analytics.

### Trial

- **Apache Iceberg with Snowflake / Databricks** unified.
- **Materialize / RisingWave** — streaming SQL DB.
- **MotherDuck** — DuckDB hosted.
- **Tinybird** — analytics API.
- **Postgres-as-everything** (CDC, vector search, queue, full-text).

### Assess

- **Apache Hudi vs Iceberg vs Delta** — converging?
- **Lakehouse query engines** (Trino, Velox).
- **Streaming-first DB** (Materialize, RisingWave, EventQL).

### Hold

- **Hadoop ecosystem** (HDFS, MapReduce) for new build.
- **Cassandra new install** for OLTP (DynamoDB / CockroachDB / ScyllaDB değerlendir).
- **Couchbase, RethinkDB** new build.

---

## 7. LLM & GenAI Stack

### Adopt

- **OpenAI / Anthropic / Google API** — production LLM (with caveats).
- **Embeddings + vector DB** (pgvector, Pinecone, Weaviate, Qdrant).
- **LangChain, LlamaIndex** (with caution — abstraction debt).
- **Hugging Face transformers** — open model hosting.
- **OpenAI structured outputs / function calling** — JSON schema.

### Trial

- **Local LLM** (Llama 3.1, Mistral, Qwen) — vLLM, llama.cpp, Ollama.
- **DSPy** — programmatic prompt optimization.
- **Guardrails / NeMo Guardrails** — output safety.
- **Agent frameworks** (AutoGen, CrewAI) — multi-agent orchestration.
- **LiteLLM** — provider abstraction.
- **LangSmith / Langfuse** — LLM observability.

### Assess

- **Multimodal models** (vision, audio, video).
- **Function calling agents in production** — reliability, cost.
- **Local inference at scale** — TCO vs API.
- **Mixture of Experts** (MoE) — trade-off.
- **Long-context models** (1M+ tokens) — etkili kullanım.
- **Agentic browsers / OS** — early days.

### Hold

- **Black-box LLM in critical decision** (medical, legal, financial) without human review.
- **Eski LangChain monolithic chain** — modülerleş.
- **PII to public LLM** (privacy + compliance).
- **Hallucination as feature** — fact-grounded RAG zorunlu.

### LLMOps stack

| Layer | Tool |
|---|---|
| Vector DB | pgvector, Pinecone, Weaviate, Qdrant |
| Orchestration | LangChain, LlamaIndex, DSPy |
| Observability | LangSmith, Langfuse, Helicone |
| Eval | Promptfoo, Ragas, OpenAI Evals |
| Caching | GPTCache, Redis semantic |
| Routing | LiteLLM, OpenRouter |
| Safety | Guardrails, NeMo, Lakera |

---

## 8. DevEx & Productivity

### Adopt

- **GitHub Copilot / Cursor / Codeium** — AI pair programming.
- **Devcontainers** — reproducible dev env.
- **GitHub Actions / GitLab CI** — pipeline.
- **Renovate / Dependabot** — dependency update automation.
- **Snyk / Trivy** — vulnerability scan.
- **Conventional Commits + release-please** — auto-versioning.
- **OpenTelemetry** — vendor-neutral observability.

### Trial

- **Claude Code / Devin / OpenAI Operator** — AI agentic dev.
- **Coder / Gitpod / GitHub Codespaces** — cloud dev env.
- **Nx / Turborepo** — monorepo tooling.
- **Zed editor** — collaborative.
- **Bazel / Buck2 / Pants** — hermetic build (large monorepo).
- **Sigstore / cosign** — supply chain signing.

### Assess

- **AI-driven test generation**.
- **Automated postmortem** via LLM.
- **Code modification at scale** (codemods + LLM).

### Hold

- **Manuel deployment scripts** (CI/CD use et).
- **Vendor-locked observability** (OpenTelemetry kullan).
- **JIRA + 5 başka ticket system** — tek source of truth.

---

## 9. Frontend Trendleri

### Adopt

- **React 18+ (Server Components)** — RSC paradigma.
- **Next.js 14+ App Router** — full-stack React.
- **Vue 3 + Nuxt** — alternative.
- **Svelte 5 + SvelteKit** — runes ile reactive.
- **TanStack** ecosystem (Query, Router, Table) — framework-agnostic.
- **Tailwind CSS** — utility-first styling.
- **shadcn/ui** — component library copy-paste.
- **Vite** — Webpack yerine build tool.
- **Playwright** — E2E test.

### Trial

- **Astro** — content-heavy, islands architecture.
- **Qwik** — resumable, near-zero JS.
- **HTMX** — server-driven UI, SPA olmadan.
- **Solid / SolidStart** — fine-grained reactivity.

### Assess

- **Server-driven UI** patterns (Airbnb, Shopify Hydrogen).
- **Local-first** (Linear, Figma) + sync engine (Replicache, Yjs).
- **WebGPU** — graphics, ML in browser.

### Hold

- **Webpack new project** (Vite).
- **Create React App** (deprecated 2023).
- **Redux for everything** (TanStack Query + Zustand).
- **CSS-in-JS runtime** (compile-time alternative or Tailwind).

---

## 10. Hold — Uzak Durulacaklar

### Yeni proje için kaçın

- 🚫 **PHP for new product** (legacy maintenance OK; modern stack için diğer seçenekler).
- 🚫 **CoffeeScript**.
- 🚫 **Backbone.js, AngularJS (1.x)**.
- 🚫 **Hadoop ecosystem** (yeni install).
- 🚫 **Subversion, CVS, Mercurial new project** (Git).
- 🚫 **SOAP** (REST, gRPC, GraphQL).
- 🚫 **XML config** (YAML / TOML).
- 🚫 **Bash scripts > 100 satır** (Python / Go).
- 🚫 **Selenium yeni proje** (Playwright).
- 🚫 **Jenkins yeni proje** (GitHub Actions, GitLab CI).
- 🚫 **VirtualBox + Vagrant** (Devcontainers, Docker).
- 🚫 **JSON Schema yerine ad-hoc validation**.

### "Modaya kapılma" tehlikesi

> Yeni teknoloji evaluation cost'u **gizlidir**:
> - Eğitim süresi.
> - Operational tooling olgunlaşmamış.
> - Stack Overflow / forum desteği zayıf.
> - 2 yıl sonra terkedilebilir.

**Boring teknoloji dan ChooseBoringTechnology.com manifesto'su**: "Innovation tokens"ını **dikkatli** kullan. Tipik proje 3 token ile başlar; her yeni / olgunlaşmamış teknoloji 1 token tüketir.

---

## 🎯 Staff+ Yaklaşımı

### "Yeni" için kontrol listesi

- [ ] Production-ready mi (1.0+ değil yeterli; **işletme** olgunluğu)?
- [ ] Operational tooling (metric, log, debugger) var mı?
- [ ] Community + Stack Overflow > 1K post?
- [ ] Major şirket production'da kullanıyor mu?
- [ ] 3-5 yıl sonra hâlâ olur mu (vendor stability)?
- [ ] Migration story varsa (lock-in tolerable)?
- [ ] Eğitim + onboarding maliyeti?
- [ ] Replace ettiği eski tool için sweat equity var mı?

### Adoption stratejisi

```
1. Spike (1-2 sprint, throwaway).
2. Pilot servis (düşük-risk, internal tool).
3. POC production (canary, feature flag).
4. Selective rollout (yeni yazılımda).
5. Default (org-wide).
```

> Her adımda gating criteria + rollback plan. **Tüm büyük teknoloji geçişlerinin %50'si başarısız** ya da gecikmeli; risk planlaması zorunlu.

---

## ⚠️ Teknoloji Seçim Anti-Pattern'leri

| Anti-Pattern | Neden Tehlikeli | Doğru Yaklaşım |
|---|---|---|
| **Résumé-Driven Development** | Mühendis CV'sine yazmak için teknoloji seçer; proje ihtiyacı ikincil kalır | Karar ADR'ye yazılır; "bu teknolojiyi neden seçtik?" sorusu business impact ile cevaplanmalı |
| **Yeni = iyi varsayımı** | Her yeni framework/tool production-ready değil; community, tooling, debug desteği eksik | Innovation token modeli: proje başına 2-3 yeni teknoloji sınırı |
| **POC'suz adoption** | "Demo'da çalıştı" → production'da operasyonel sorunlar (monitoring, backup, upgrade) | Spike → Pilot (internal) → Canary (production) → Selective rollout |
| **Hype-Driven Architecture** | Konferans talk'larına bakarak mimari değiştirmek; context farkı görmezden gelinir | "Hangi problemi çözüyor?" — problem-first, technology-second |
| **Vendor lock-in körlüğü** | Managed servis konforunda abstraction yapılmaz; migration imkânsızlaşır | Thin wrapper / port-adapter; exit cost'u ADR'de dokümante et |
| **Big-bang migration** | Tüm sistemi aynı anda yeni stack'e taşıma → uzun süre, yüksek risk | Strangler fig pattern; incremental migration + feature flag |
| **"Herkes kullanıyor" argümanı** | Netflix'in çözdüğü problem ≠ senin problemin; scale farkı 1000× olabilir | Kendi traffic/team/budget profiliyle değerlendir |

---

## 📚 İleri Okuma

- ThoughtWorks Technology Radar (yıllık)
- *Software Architecture: The Hard Parts* — Ford, Richards, Sadalage, Dehghani
- *Building Evolutionary Architectures* — Ford, Parsons, Kua
- *Choose Boring Technology* — Dan McKinley
- LeadDev / The Pragmatic Engineer — modern stack analyses
- The New Stack, InfoQ — tech trend coverage

> [⬅️ Pratik klasörü](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
