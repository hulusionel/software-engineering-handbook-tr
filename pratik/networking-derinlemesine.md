# 🌐 Networking Derinlemesine

> **"Network güvenilir değildir. Network güvenli değildir. Topology değişir."** — Fallacies of Distributed Computing

Bu doküman OSI'den HTTP/3'e, TLS'ten gRPC'ye kadar **modern uygulama mühendisinin bilmesi gereken** network bilgisini kapsar.

---

## 📑 İçindekiler

1. [Katman Modeli — Niye Hâlâ Önemli?](#1-katman-modeli--niye-hâlâ-önemli)
2. [TCP'nin İç Yapısı](#2-tcpnin-iç-yapısı)
3. [TLS/SSL](#3-tlsssl)
4. [HTTP/1.1, HTTP/2, HTTP/3](#4-http11-http2-http3)
5. [DNS](#5-dns)
6. [Load Balancing](#6-load-balancing)
7. [gRPC, WebSocket, SSE](#7-grpc-websocket-sse)
8. [CDN ve Edge](#8-cdn-ve-edge)
9. [Network Observability](#9-network-observability)
10. [Network Security](#10-network-security)
11. [Tuzaklar](#11-tuzaklar)

---

## 1. Katman Modeli — Niye Hâlâ Önemli?

```
┌─────────────────────────────────┐
│ L7 Application: HTTP, gRPC, DNS │
│ L6 Presentation: TLS, JSON      │
│ L5 Session: SSL handshake       │
│ L4 Transport: TCP, UDP, QUIC    │
│ L3 Network: IP, ICMP, BGP       │
│ L2 Data Link: Ethernet, ARP     │
│ L1 Physical: copper, fiber      │
└─────────────────────────────────┘
```

> **Pratik:** Çoğunlukla L4-L7 ile uğraşırsın. Ama **L3 BGP routing leak** Cloudflare 2019, **L7 service mesh** Istio konuları staff IC için bilinmesi gerekir.

---

## 2. TCP'nin İç Yapısı

### 3-way handshake

```
Client → SYN → Server
Client ← SYN-ACK ← Server
Client → ACK → Server
```

→ 1 RTT + ilk veri = **2 RTT** ilk byte için.

### TCP Fast Open (TFO)

İlk SYN'de **veri gönder** — TFO cookie ile. 1 RTT'ye düşer. (Linux 3.7+)

### Slow start + congestion control

```
cwnd (congestion window) = 1 segment
Her ACK ile cwnd *= 2 (exponential)
Loss tespit → cwnd /= 2 (multiplicative decrease)
```

**Sonuç:** İlk birkaç saniye throughput **giderek artar**. Kısa connection'lar gerçek bandwidth'e ulaşamaz.

### Congestion control algorithms

| Algoritma | Davranış | Kullanım |
|---|---|---|
| **Reno** | Loss-based, klasik | Eski default |
| **CUBIC** | Loss-based, daha agresif | Linux default |
| **BBR** (Google) | Bandwidth-based, RTT-aware | Yüksek-throughput, packet-loss tolerant |
| **BBRv2/v3** | Daha fair | Modern |

```bash
sysctl -w net.ipv4.tcp_congestion_control=bbr
```

> Bandcamp/Spotify gibi global servisler BBR ile latency düşürdü, throughput arttırdı.

### Nagle ve Delayed ACK

- **Nagle**: Küçük paketleri buffer'la, birleştir. Bandwidth dostu, latency kötü.
- **Delayed ACK**: ACK'leri toplu yolla.
- İkisi birlikte → **200ms gecikme!**
- Çözüm: `TCP_NODELAY` + `TCP_QUICKACK`.

### Buffer sizes

```
BDP = Bandwidth × RTT
   100 Mbps, 100ms RTT → 1.25 MB BDP
   send_buf < BDP → throughput sınırlanır
```

```bash
sysctl -w net.core.rmem_max=16777216
sysctl -w net.core.wmem_max=16777216
sysctl -w net.ipv4.tcp_rmem='4096 87380 16777216'
```

### TCP Keepalive

- Default: 2 saat, 75s × 9 retry → 2 saat 11 dk sonra dead.
- Çoğu uygulama için **app-level heartbeat** daha iyi.

```bash
sysctl -w net.ipv4.tcp_keepalive_time=600
sysctl -w net.ipv4.tcp_keepalive_intvl=60
sysctl -w net.ipv4.tcp_keepalive_probes=3
```

### TIME_WAIT

Connection kapandıktan sonra 60-120s TIME_WAIT. Yüksek-rate servis → port exhaustion.
**Çözüm:** Connection reuse (keep-alive), `tcp_tw_reuse`, **bağlantı tarafı (client) seç dikkatli**.

### io_uring — Modern Async I/O

Linux 5.1+ ile gelen `io_uring`, geleneksel `epoll` + `read`/`write` syscall modelini kökten değiştirir. İki ring buffer (submission queue + completion queue) üzerinden kernel ile **syscall'sız** iletişim sağlar:

- **Syscall azaltma:** Geleneksel modelde her I/O için en az 1 syscall gerekir. io_uring'de yüzlerce I/O operasyonu tek `io_uring_enter()` ile submit edilir; hatta `SQPOLL` modunda kernel thread polling yapar → **sıfır syscall**.
- **Zero-copy:** `IORING_OP_SEND_ZC` ile userspace buffer'dan doğrudan NIC'e gönderim; memcpy overhead'i sıfırlanır.
- **Batching & pipelining:** Submission queue'ya birden fazla request eklenip tek seferde submit edilir; completion'lar asenkron olarak completion queue'dan okunur.

**Performans etkisi:** Facebook (Meta) Thrift'i io_uring'e taşıdığında %5-10 latency düşüşü ve %10+ CPU tasarrufu gördü. High-frequency trading, proxy (Envoy io_uring desteği deneysel), veritabanı engine'leri (RocksDB, ScyllaDB) en çok fayda gören alanlar.

**Dikkat:** io_uring güvenlik yüzeyini genişletir (CVE-2022-29582 vb.); container ortamda seccomp ile kısıtlanması önerilir. macOS/Windows'ta karşılığı yoktur (kqueue/IOCP farklı model).

---

## 3. TLS/SSL

### Handshake

#### TLS 1.2 (eski) — 2 RTT

```
Client → ClientHello (versions, ciphers, random)
Client ← ServerHello + Certificate + ServerKeyExchange + ServerHelloDone
Client → ClientKeyExchange + ChangeCipherSpec + Finished
Client ← ChangeCipherSpec + Finished
```

#### TLS 1.3 (modern) — 1 RTT

```
Client → ClientHello (versions, ciphers, key_share)
Client ← ServerHello + Certificate + Finished
Client → Finished + APPLICATION DATA
```

#### 0-RTT (TLS 1.3 resumption)

PSK ticket ile **ilk RTT'de application data**. Replay attack riski → idempotent ops için.

### Certificate chain

```
Root CA → Intermediate CA → Leaf certificate
```

- Browser'da **Root CA store** (Mozilla, Apple, Microsoft).
- Server **Leaf + Intermediate** sunar.
- Browser zinciri Root'a kadar doğrular.

### Cipher suite örneği

```
TLS_AES_256_GCM_SHA384
   key exchange: ECDHE
   auth: signature in cert (RSA / ECDSA)
   bulk cipher: AES-256-GCM
   MAC: integrated (GCM)
   PRF: SHA-384
```

### Forward Secrecy

ECDHE (ephemeral) → her connection için yeni session key. Server private key sızdığında **eski trafik açılamaz**.

### Üretim ipuçları

- ✅ TLS 1.2 + 1.3 enabled, eskiler disabled.
- ✅ Modern cipher list (Mozilla SSL config generator).
- ✅ HSTS (`Strict-Transport-Security: max-age=31536000`).
- ✅ OCSP stapling (revocation check'i hızlandırır).
- ✅ Cert renewal otomatik (Let's Encrypt + cert-manager).
- ✅ mTLS internal traffic (zero-trust).

### mTLS

İki taraf da cert sunar → karşılıklı doğrulama. Service mesh (Istio, Linkerd) varsayılan.

---

## 4. HTTP/1.1, HTTP/2, HTTP/3

### HTTP/1.1

- Text-based.
- Connection başına bir istek (paralelizm için **6 connection** browser limit).
- Keep-alive: connection reuse.
- Head-of-line blocking: yavaş response sonrakileri bloklar.

### HTTP/2

- **Binary** framing.
- **Multiplex**: tek connection üzerinde N stream.
- **Header compression** (HPACK).
- **Server push** (deprecated 2022).
- **TLS** zorunlu pratikte.

**Sorun:** TCP'nin head-of-line blocking'i hâlâ var (paket kayıbı tüm stream'leri bekletir).

### HTTP/3 (QUIC üzerinde)

- **UDP** üzerinde QUIC (Google 2012, IETF RFC 9000).
- **No HoL blocking**: stream'ler bağımsız (kayıp tek stream'i etkiler).
- **0-RTT resumption** built-in.
- **Connection migration**: IP değişse de bağlantı sürer (mobile-friendly).
- TLS 1.3 entegre.

### Hangisi ne zaman?

| Durum | Tercih |
|---|---|
| Internal service-to-service | gRPC (HTTP/2) |
| Browser facing | HTTP/2 yaygın, HTTP/3 artıyor |
| Mobile (lossy network) | HTTP/3 (BBR + QUIC) |
| Legacy proxy chain | HTTP/1.1 fallback |

### Header semantics

- **Idempotent**: GET, PUT, DELETE, HEAD, OPTIONS.
- **Safe**: GET, HEAD, OPTIONS.
- **Cacheable**: GET, HEAD, opsiyonel POST (cache-control ile).

### Caching headers

```
Cache-Control: max-age=3600, public
ETag: "abc123"
Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT
```

Conditional request:
```
If-None-Match: "abc123"
→ 304 Not Modified (no body)
```

---

## 5. DNS

### Hierarchy

```
Root → TLD (.com) → Authoritative (example.com) → Subdomains
```

### Resolver path

```
App → Stub resolver → Recursive resolver (ISP/8.8.8.8) → Auth servers
```

### Record types

| Tip | Anlam |
|---|---|
| A | IPv4 |
| AAAA | IPv6 |
| CNAME | Alias |
| MX | Mail exchanger |
| TXT | Free text (SPF, DKIM, verification) |
| SRV | Service location |
| NS | Name server |
| SOA | Authority |
| CAA | Cert issuance auth |

### TTL & cache

- TTL düşük → değişiklik hızlı, query yük yüksek.
- TTL yüksek → değişiklik yavaş yayılır.
- Failover için 60s veya altı, normal için 300-3600s.

### DNS-based service discovery

- Consul, K8s CoreDNS, Eureka.
- TTL'i kısa (5-30s) tut.
- Round-robin DNS basit ama health-aware değil.

### Anti-pattern: client cache

> Java JVM **default forever DNS cache**. ⚠️
> `networkaddress.cache.ttl=60` mutlaka set et.

> Facebook 2021 outage (postmortem-arsivi #12): BGP withdrawal → DNS unreachable → tüm sistem.

### DNSSEC, DoH, DoT

- **DNSSEC**: Authentic responses (signed).
- **DoH** (DNS over HTTPS): Privacy.
- **DoT** (DNS over TLS): Privacy + integrity.

---

## 6. Load Balancing

### L4 vs L7

| | L4 | L7 |
|---|---|---|
| Layer | TCP/UDP | HTTP |
| Speed | Çok hızlı | Daha yavaş |
| Inspection | IP/port | Full HTTP |
| Stickiness | Source IP | Cookie, header |
| Examples | LVS, AWS NLB | nginx, HAProxy, AWS ALB, Envoy |

### Algoritmalar

- **Round-robin**: Sırayla.
- **Least connections**: En az aktif bağlantı.
- **Least response time**: En hızlı.
- **Consistent hashing**: Same key → same server (cache friendly).
- **Power of 2 choices**: 2 random server'ın arasında least-loaded — neredeyse optimal.

### Tutarlı Hashleme Varyantları

Consistent hashing, node eklenip çıkarıldığında minimum key redistribution sağlar. Farklı varyantlar farklı trade-off'lar sunar:

| Varyant | Nasıl Çalışır | Artı | Eksi | Kullanım |
|---|---|---|---|---|
| **Ring (Karger 1997)** | Hash ring üzerinde node'lar sanal düğümlerle dağıtılır; key saat yönünde en yakın node'a gider | Basit, anlaşılır | Sanal düğüm sayısı dengeyi belirler; metadata büyük olabilir | Memcached, DynamoDB |
| **Jump (Lamping & Veach 2014)** | O(ln n) zaman, sıfır memory; hash fonksiyonu ile bucket belirlenir | Bellek yok, çok hızlı, mükemmel denge | Sadece **append-only** — ortadan node çıkarma yok | Stateless sharding, Google internal |
| **Maglev (Eisenbud et al. 2016)** | Permutation tabanlı lookup table; her node sabit boyutlu tabloda eşit slot alır | Çok düşük lookup (O(1)), minimal disruption | Tablo yeniden hesaplaması O(M×N); bellek M×N | Google Maglev LB, Envoy |
| **Rendezvous / HRW (Thaler & Ravishankar 1998)** | Her key için tüm node'lara hash hesaplanır, en yüksek kazanır | Node ekleme/çıkarma'da minimal redistribution; basit implementasyon | O(N) per-lookup — node sayısı arttıkça yavaşlar | DNS, CDN, distributed cache |

**Seçim kuralı:** Node sayısı az ve dinamikse → Ring. Append-only ve hız kritikse → Jump. L4/L7 LB ve düşük latency → Maglev. Basitlik ve doğruluk → Rendezvous.

### Health check

- Active: periyodik HTTP/TCP probe.
- Passive: response error tracker.
- **Aggressive timeout** = false positive cascading failures.
- **Lazy timeout** = dead server'a istek yollar.

### Sticky session

- Cookie-based (HTTP).
- Source IP hash (L4).
- ⚠️ Stateful → scale zorlu, prefer stateless + external session store.

### Service mesh (Envoy + Istio/Linkerd)

- mTLS, retry, circuit breaker, distributed tracing — sidecar pattern.
- Yüksek yatırım — küçük ekipte aşırı.

---

## 7. gRPC, WebSocket, SSE

### gRPC

- HTTP/2 + Protobuf.
- Strong typing, schema-driven.
- Streams: unary, server-stream, client-stream, bi-direction.
- 8+ dilde stub generation.
- Browser'dan **doğrudan** kullanılamaz → grpc-web + proxy.

### WebSocket

- Persistent bi-directional channel.
- HTTP upgrade ile başlar, sonra raw TCP.
- Real-time push (chat, oyun, dashboard).
- ⚠️ Stateful — connection routing zorluğu.

### SSE (Server-Sent Events)

- HTTP üzerinde tek-yön server → client streaming.
- Auto-reconnect built-in.
- Text-based, debug kolay.
- Bi-direction yoksa **WebSocket'ten basit**.

### Hangisi?

| Senaryo | Tercih |
|---|---|
| Internal RPC | gRPC |
| Browser ↔ server (real-time) | WebSocket |
| Server → client only stream | SSE |
| Public API | REST |
| Mobile, polling kabul | REST + long polling |

---

## 8. CDN ve Edge

### CDN nasıl çalışır?

```
User → DNS resolves to nearest PoP
PoP cache hit → serve directly (10-30ms)
PoP cache miss → origin pull → cache → serve
```

### Cache key

URL + query string + Vary headers.
Misconfig → **cache poisoning** (auth header'ı cache key'e karışırsa cross-user leak).

### Edge compute

- Cloudflare Workers (V8 isolate).
- AWS Lambda@Edge.
- Fastly Compute@Edge (WASM).
- Vercel Edge Functions.

**Use case:** A/B testing, auth, request rewriting, image optimization.

### CDN anti-pattern'leri

- 🚫 Auth-required content cache'lenir (private cache eksik).
- 🚫 `Cache-Control: no-cache` yanlış kullanım (cache OK ama revalidate).
- 🚫 Vary header eksik → wrong variant döner.
- 🚫 Origin shield yok → cache miss flood orijini düşürür.

---

## 9. Network Observability

### Layered metrics

| Katman | Araç |
|---|---|
| **Packet** | Wireshark, tcpdump |
| **Flow** | NetFlow, sFlow |
| **TCP state** | `ss`, `netstat` |
| **HTTP** | nginx access log, ALB log |
| **App-level** | OpenTelemetry, Jaeger |
| **Mesh** | Envoy stats, Hubble |

### Distributed tracing

- W3C Trace Context (`traceparent` header).
- OpenTelemetry collector → Jaeger / Tempo / Datadog.
- Each span: start, end, attributes, parent.
- Sampling: head-based (1%) veya tail-based (errors %100).

### eBPF observability

- **Cilium Hubble**: K8s flow visibility.
- **Pixie**: zero-instrumentation profiling.
- **bpftrace**: ad-hoc one-liner.

### "Network slow" diagnosis

```
1. ping  → round-trip baseline
2. mtr   → hop-by-hop, packet loss
3. tcpdump → packet level
4. ss -tin → TCP socket detail (RTT, retransmit)
5. iperf3 → bandwidth raw
```

---

## 10. Network Security

### Defense in depth

```
[Internet]
   ↓ WAF (L7 attacks: SQLi, XSS)
   ↓ DDoS protection (CloudFlare, AWS Shield)
   ↓ Load balancer (TLS termination)
   ↓ API gateway (rate limit, auth)
   ↓ Service mesh (mTLS)
   ↓ Application (authz, input validation)
```

### Common attacks

| Saldırı | Savunma |
|---|---|
| **DDoS (volumetric)** | CDN, scrubbing, anycast |
| **DDoS (L7)** | Rate limit, CAPTCHA, JS challenge |
| **DNS amplification** | UDP rate limit, ACL |
| **TLS downgrade** | HSTS, modern cipher only |
| **MitM** | Cert pinning, mTLS |
| **BGP hijack** | RPKI, monitoring |
| **DNS poisoning** | DNSSEC, DoH/DoT |
| **SYN flood** | SYN cookies, conntrack tuning |

### Zero-Trust Networking

> **"Network konumu güven göstergesi değildir."** Her istek **kimlik ve yetki ile** geçer.

- Service mesh + mTLS.
- Identity-aware proxy (Google BeyondCorp, Cloudflare Access, Tailscale).
- Workload identity (SPIFFE/SPIRE).
- Hiçbir VPN "içerideyim, güvendeyim" demez.

### Network policy (K8s)

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all-default
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]
```

> Default deny + allowlist. Cilium / Calico enforce.

---

## 11. Tuzaklar

### 1. JVM DNS cache forever

`networkaddress.cache.ttl=60` set et.

### 2. Connection pool exhaustion

```
maxConn = 10
incoming rate > processing rate → pool tükenir → 5xx
```

**Çözüm:** Pool size = (peak QPS × p99 latency) + buffer.

### 3. SO_REUSEADDR vs SO_REUSEPORT

- `SO_REUSEADDR`: TIME_WAIT'teki addr'i tekrar bind.
- `SO_REUSEPORT`: Aynı port'a multiple listener (kernel load balance).

### 4. MTU mismatch

- Default 1500 byte.
- VPN/tunnel → daha az (örn. 1400).
- Path MTU discovery fail → packet drop.
- ICMP filtreleme yapma.

### 5. Asymmetric routing

Outbound bir path, inbound başka — stateful firewall reset eder.

### 6. NAT timeout

Idle TCP connection NAT tablosundan düşer (genelde 5 dk).
**Çözüm:** Application keepalive < NAT timeout.

### 7. Cross-AZ traffic ücreti

AWS \$0.01/GB cross-AZ. Aşırıya kaçarsa **fatura katlanır**.
**Çözüm:** Topology-aware routing (Istio locality LB).

### 8. DNS round-robin ≠ load balance

Client cache + uneven distribution. Sadece basit fallback olarak.

### 9. Idempotent retry hatası

POST'u retry ediyor → çift kayıt. Idempotency-key zorunlu.

### 10. HTTPS sertifika expiry

> **Üretimde kalan en eski outage tipi.** Cert renewal otomatik + 30/14/7 gün öncesi alert.

---

## 🎯 Staff+ Networking Kontrol Listesi

### Yeni servis / platform değerlendirme

- [ ] Servisler arası iletişim protokolü seçildi mi? (REST vs gRPC vs async messaging — trade-off ADR'de)
- [ ] TLS 1.2+ zorunlu mu? Sertifika otomasyonu (cert-manager, ACME) kurulu mu?
- [ ] DNS TTL stratejisi belirlenmiş mi? (Failover hızı vs cache verimliliği)
- [ ] Cross-AZ / cross-region trafik maliyeti hesaplanmış mı?
- [ ] mTLS veya service mesh gerekli mi? (Zero-trust network policy)

### Operasyonel kontrol

- [ ] TCP keepalive < NAT timeout mu? (Cloud ortamda genelde 350s)
- [ ] Connection pooling doğru yapılandırılmış mı? (Max connections, idle timeout)
- [ ] Rate limiting katmanı (API gateway / envoy) tanımlı mı?
- [ ] Circuit breaker timeout'ları SLO ile uyumlu mu?
- [ ] Network observability: packet loss, retransmission, latency per-hop izleniyor mu?

### Incident readiness

- [ ] BGP hijack / route leak detection var mı? (RPKI, monitoring)
- [ ] DNS failover test edilmiş mi? (Primary → secondary geçiş süresi)
- [ ] DDoS mitigation planı (Cloudflare, AWS Shield) aktif mi?

---

## 📚 İleri Okuma

- *TCP/IP Illustrated* — W. Richard Stevens (klasik)
- *High Performance Browser Networking* — Ilya Grigorik (online ücretsiz)
- *Computer Networks: A Systems Approach* — Peterson & Davie
- RFC 9000 — QUIC
- RFC 9110-9114 — modern HTTP semantics
- RFC 8446 — TLS 1.3
- Cloudflare blog (BGP, DNS, TLS deep dives)
- Mozilla SSL Configuration Generator

> [⬅️ Pratik klasörü](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
