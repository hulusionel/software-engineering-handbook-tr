# 🔌 API Tasarım Derinliği

> **"REST API tasarımı 100 mühendisten 95'inin yanlış yaptığı, ama hatalarının üretime düştüğü ana yer."**

Bu doküman senior+ mühendisin **anında** doğru kararı vermesi gereken API meselelerini detaylı işler: idempotency, pagination, error model, versioning, deprecation, ve standart RFC'ler.

---

## 📑 İçindekiler

1. [Idempotency — En Kritik Konu](#1--idempotency--en-kritik-konu)
2. [Pagination — Cursor vs Offset](#2--pagination--cursor-vs-offset)
3. [Error Model — RFC 7807 / RFC 9457](#3--error-model--rfc-7807--rfc-9457)
4. [Versioning Stratejisi](#4--versioning-stratejisi)
5. [Deprecation & Sunsetting](#5--deprecation--sunsetting)
6. [Rate Limiting & Throttling](#6--rate-limiting--throttling)
7. [Authentication & Authorization Header'ları](#7--authentication--authorization-headerları)
8. [Caching & Conditional Requests](#8--caching--conditional-requests)
9. [Long-Running Operations](#9--long-running-operations)
10. [Filtering, Sorting, Field Selection](#10--filtering-sorting-field-selection)
11. [Webhooks](#11--webhooks)
12. [API Tasarım Anti-Pattern'leri](#12--api-tasarım-anti-patternleri)

---

## 1. 🎯 Idempotency — En Kritik Konu

> **Tanım:** Aynı isteği N kez yapmak, 1 kez yapmakla aynı son durumu üretir.

### Hangi metodlar idempotent?

| Metod | Spec'e göre | Pratikte |
|---|---|---|
| GET | ✅ | ✅ |
| HEAD | ✅ | ✅ |
| OPTIONS | ✅ | ✅ |
| PUT | ✅ | Genelde ✅ (full replace) |
| DELETE | ✅ | ✅ (silinen tekrar silinemez = idempotent) |
| POST | ❌ | **Sen idempotent yapmazsan değil** |
| PATCH | ❌ | **Operasyona göre değişir** |

### Neden POST'u idempotent yapmak zorundayız?

**Senaryo:** Mobile app payment isteği gönderir. Network kesilir. Cevap dönmedi mi yoksa dönerken mi koptu? **Bilinmiyor.** Retry yapılırsa **çift ödeme** riski.

**Çözüm:** `Idempotency-Key` header'ı.

### Stripe modelinin uyarlaması

```http
POST /v1/charges
Idempotency-Key: a1b2c3d4-uniq-uuid-from-client
Content-Type: application/json

{ "amount": 5000, "currency": "TRY", "source": "card_xxx" }
```

**Server tarafı algoritma:**

```
1. (key, request_hash) tuple'ını DB'de ara.
2. Bulundu mu?
   - Aynı request_hash → cached response döndür (HTTP 200, X-Idempotent-Replayed: true).
   - Farklı request_hash → 422 (key reuse with different body).
   - Yoksa → işle, sonucu cache'e yaz (TTL 24-48 saat).
3. Race condition: aynı key paralel 2 istek
   → DB unique index + SELECT ... FOR UPDATE veya advisory lock.
```

### Idempotency-Key tasarım kuralları

- ✅ Client UUID üretmeli (server değil).
- ✅ Body hash'i ile birlikte sakla — aynı key, farklı body = hata.
- ✅ TTL 24-48 saat tipik. (Stripe: 24h)
- ✅ Header ismi: `Idempotency-Key` (RFC draft) veya `X-Idempotency-Key`.
- ❌ Auto-generate sunucu tarafında — retry'da yeni key olur, idempotency yıkılır.
- ❌ Sadece in-memory cache — pod restart ile kaybolur.

### IETF taslağı

> RFC olmaya çalışan: [draft-ietf-httpapi-idempotency-key-header](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/)

---

## 2. 📄 Pagination — Cursor vs Offset

### Offset pagination (kötü, yaygın)

```http
GET /items?page=42&size=20
GET /items?offset=820&limit=20
```

| Sorun | Neden |
|---|---|
| **Performans** | DB her sayfada 0..N+offset row tarar. Page 1000 = full scan |
| **Tutarlılık** | Sayfa 1 ile 2 arasında yeni item eklenirse: tekrar veya atlama |
| **Deep pagination** | Çoğu DB için page > 1000 yavaş |

### Cursor pagination (doğru)

```http
GET /items?cursor=eyJpZCI6MTIzfQ&limit=20

Yanıt:
{
  "data": [...],
  "next_cursor": "eyJpZCI6MTQzfQ",
  "has_more": true
}
```

**Tasarım kuralları:**

- ✅ Cursor **opaque** olmalı (base64 encode edilmiş JSON / token). Client içeriğine bakmasın.
- ✅ Cursor stable ID üzerinden (PK + sort key) olmalı.
- ✅ Sort field unique değilse (örn. `created_at`), **(sort_value, id)** tuple kullan.
- ✅ Cursor invalidation senaryosu: `400 Bad Cursor` yerine yumuşak fallback.

### Hibrit: Keyset pagination (cursor'un SQL hali)

```sql
-- İlk sayfa
SELECT * FROM items ORDER BY created_at DESC, id DESC LIMIT 20;

-- Sonraki sayfa
SELECT * FROM items
WHERE (created_at, id) < ('2024-11-01', 12345)
ORDER BY created_at DESC, id DESC
LIMIT 20;
```

İndex: `(created_at DESC, id DESC)`. Performans: O(log N + page_size) — sayfa 1 ile sayfa 1000 aynı.

### Total count?

```
❌ "Toplam 47.392 sonuç" — büyük tabloda COUNT(*) yavaş
✅ "Tahmini 47K+ sonuç" — pg_class.reltuples veya cache
✅ "has_more: true" — gerçek count gerekmiyorsa
```

### Anti-pattern

- ❌ **Cursor + offset karışımı** API'de iki pagination tipi sunmak (confusion).
- ❌ **Cursor'da SQL injection vector** — opaque tut, validate et.
- ❌ **Page size limitsiz** — `?limit=1000000` izin verme.

---

## 3. 🚨 Error Model — RFC 7807 / RFC 9457

### Yanlış (her API farklı format)

```json
{ "error": "Bad request" }
{ "code": 400, "message": "..." }
{ "errors": [{ "field": "email", "msg": "invalid" }] }
```

→ Client hiçbir API ile tutarlı hata handle edemez.

### Doğru: RFC 9457 — Problem Details for HTTP APIs

> RFC 7807'nin (2016) güncellenmiş hali RFC 9457 (2024).

```http
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/problem+json

{
  "type": "https://api.example.com/probs/validation-error",
  "title": "Your request parameters didn't validate.",
  "status": 422,
  "detail": "The 'email' field must be a valid email address.",
  "instance": "/orders/12345",
  "errors": [
    { "field": "email", "message": "must be valid email" },
    { "field": "amount", "message": "must be positive" }
  ],
  "trace_id": "abc-123-def"
}
```

| Alan | Zorunlu? | Açıklama |
|---|---|---|
| `type` | Önerilen | Hata tipinin URI'si (insanlar için doc, kod için switch key) |
| `title` | Önerilen | Kısa, sabit, lokalize edilmemiş başlık |
| `status` | Önerilen | HTTP status code (gövdede de) |
| `detail` | Opsiyonel | İnsan-okur açıklama, lokalize edilebilir |
| `instance` | Opsiyonel | Bu spesifik hatanın URI'si |
| **Genişletme alanları** | İsteğe bağlı | `errors[]`, `trace_id`, `retry_after` vb. |

### HTTP status code disiplini

| Code | Anlamı | Yanlış kullanım |
|---|---|---|
| **200** | OK | "İşlem başarılı ama gövdede `success: false`" 🚫 |
| **201** | Created | POST'tan sonra Location header şart |
| **202** | Accepted | Async işlem başlatıldı |
| **204** | No Content | DELETE / PUT idempotent |
| **301 / 308** | Moved Permanently | Permanent redirect (308 = method preserve) |
| **400** | Bad Request | Generic — daha spesifik kod varsa kullan |
| **401** | Unauthorized | Aslında "unauthenticated" |
| **403** | Forbidden | Yetkili değil |
| **404** | Not Found | Resource yok / yetki yok (info-leak için bazen 403 yerine) |
| **409** | Conflict | Versioning conflict, duplicate key |
| **410** | Gone | Resource kasıtlı silindi (404 değil) |
| **422** | Unprocessable Entity | Validation error (400'den daha spesifik) |
| **429** | Too Many Requests | Rate limit + `Retry-After` header |
| **500** | Internal Server Error | Bug — düzelt, tekrar etme |
| **502** | Bad Gateway | Upstream bozuk |
| **503** | Service Unavailable | Yük + `Retry-After` |
| **504** | Gateway Timeout | Upstream yavaş |

### Retry-After header

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 60

veya

Retry-After: Wed, 21 Oct 2026 07:28:00 GMT
```

→ Client retry mantığı için hayati. **Saniye veya HTTP-date.**

---

## 4. 🔢 Versioning Stratejisi

### Yöntemler

| Yöntem | Örnek | Artı | Eksi |
|---|---|---|---|
| **URL path** | `/v1/users` | Görünür, cache-friendly | URL "kirli" |
| **Header** | `Accept: application/vnd.api.v1+json` | URL temiz | Görünmez, tooling zor |
| **Query param** | `/users?version=1` | Görünür | Cache karışır |
| **Hostname** | `v1.api.example.com` | İzole edilebilir | DNS kompleks |
| **Date-based** | `Stripe-Version: 2024-04-10` | İnce taneli, "rolling" | Versioning matrix patlar |

### Endüstri pratiği

- **GitHub, AWS:** URL path (`/v1/`, `/v2/`)
- **Stripe:** Date-based (`Stripe-Version` header)
- **GCP:** Hibrit — major URL'de, minor header'da

### Major bump ne zaman?

- 🔴 **Breaking change** zorunlu (alan kaldır, tip değişti, semantik değişti)
- 🟢 **Backward-compatible**: yeni alan, yeni endpoint, yeni opsiyonel param → **bump etme**

### Schema evolution kuralları (backward-compatible)

- ✅ **Yeni opsiyonel alan eklemek** OK
- ✅ **Enum'a yeni değer eklemek** OK (client unknown'a tolerant olmalı)
- ✅ **Yeni endpoint** OK
- ❌ **Alan kaldırmak** breaking
- ❌ **Alan tipini değiştirmek** breaking
- ❌ **Required alan eklemek** breaking
- ❌ **Default değeri değiştirmek** breaking
- ❌ **Validation kuralını sıkılaştırmak** breaking

### "Tolerant Reader" prensibi

> Client bilmediği alanları **yoksay** (fail etmesin). Bu sayede sunucu **additive** değişiklik yapabilir.

```javascript
// ❌ Strict parsing
const { name, email } = strictSchema.parse(response);

// ✅ Tolerant
const { name, email, ...rest } = response;
```

---

## 5. 🌅 Deprecation & Sunsetting

### RFC 8594 — Sunset header

```http
HTTP/1.1 200 OK
Sunset: Wed, 11 Nov 2026 23:59:59 GMT
Deprecation: true
Link: <https://api.example.com/v2/users>; rel="successor-version"
Link: <https://api.example.com/docs/migration>; rel="deprecation"
```

### Deprecation timeline (önerilen)

```
Day 0    : Yeni versiyon yayınlanır, paralel çalışır
Day 30   : Doc'ta "deprecated" işareti, blog post
Day 60   : Sunset header eklenir (örn. 6 ay sonra)
Day 120  : Email + dashboard uyarı (kullanıcılar tespit)
Day 150  : Yumuşak rate limit (eski versiyon yavaşlar)
Day 180  : 410 Gone — eski versiyon kapanır
```

### Public API kuralı

> **Public** API: minimum **12 ay** deprecation süresi. Enterprise kontratlarda 24 ay yaygın.

> **Internal** API: 1-3 ay yeter, ama **kullananları izleyebilmek** şart (telemetry).

### Migration desteği

- ✅ **Side-by-side** çalıştır eski + yeni.
- ✅ **Migration guide** dokümantasyonu.
- ✅ **Sandbox** ile test ortamı.
- ✅ **Top kullanıcılara** bireysel iletişim.
- ❌ **"Pazartesi kapatıyoruz"** mailini Cuma atma.

---

## 6. 🚦 Rate Limiting & Throttling

### Algoritma seçimi

| Algoritma | Avantaj | Dezavantaj |
|---|---|---|
| **Fixed window** | Basit | Sınır çizgisinde 2× burst |
| **Sliding window log** | Doğru | Memory yoğun |
| **Sliding window counter** | Hibrit, doğru + memory verimli | Hafif yaklaşık |
| **Token bucket** | Burst destekli | Tuning karmaşık |
| **Leaky bucket** | Düz akış | Burst engelli |

> **Pratik:** Çoğu API gateway (Kong, Envoy, AWS WAF) **token bucket** kullanır.

### Header'lar — IETF taslağı

```http
RateLimit-Limit: 100
RateLimit-Remaining: 87
RateLimit-Reset: 60
RateLimit-Policy: 100;w=60
```

### Hangi limitler?

- 🔑 **Per API key** — premium tier yüksek
- 🌍 **Per IP** — abuse koruma
- 👤 **Per user** — fair use
- 🛣️ **Per endpoint** — pahalı endpoint düşük limit
- 🏢 **Global** — DDoS koruması

### 429 yanıtı

```http
HTTP/1.1 429 Too Many Requests
Content-Type: application/problem+json
Retry-After: 30
RateLimit-Reset: 30

{
  "type": "https://api.example.com/probs/rate-limit",
  "title": "Rate limit exceeded",
  "status": 429,
  "detail": "Limit 100 req/min. Try again in 30 seconds.",
  "trace_id": "abc"
}
```

### Anti-pattern

- ❌ **Limit'i 401/403 ile dön** — client retry mantığını bozar.
- ❌ **Retry-After yok** — client exponential backoff zorlanır.
- ❌ **Cluster-wide tek counter Redis** — Redis bottleneck.
- ❌ **Limit aşıldığında IP ban** — proxy'ler arkasında abuse.

---

## 7. 🛂 Authentication & Authorization Header'ları

### Standart

```http
Authorization: Bearer eyJhbGciOiJSUzI1NiIs...
```

| Şema | Kullanım |
|---|---|
| `Bearer` | OAuth2 / JWT |
| `Basic` | Eski sistemler, deprecated public API'lerde |
| `Digest` | Eski, kullanılmıyor |
| `Hawk / AWS-SigV4` | Request imzalama |

### API Key

> **`Authorization: Bearer api_key`** veya **`X-API-Key:`** custom header. Hangisini seçersen tutarlı kal.

### Multi-tenant header

```http
X-Tenant-ID: acme-corp
```

→ Authorization scope'ta yoksa eklenmeli; yoksa client başka tenant'ın verisini görür (IDOR).

### Anti-pattern

- ❌ **API key URL'de** (`?apikey=xxx`) — log'larda saklanır.
- ❌ **Long-lived token** + refresh yok — token leak felaketi.
- ❌ **JWT verify atlama** veya `alg: none` kabul.
- ❌ **`Authorization` header'ı yansıt** error log'larında.

---

## 8. 🗄️ Caching & Conditional Requests

### ETag + If-None-Match

```http
GET /users/123
→ 200 OK
  ETag: "v3-abc"
  ...

GET /users/123
If-None-Match: "v3-abc"
→ 304 Not Modified  (gövde yok!)
```

### Last-Modified + If-Modified-Since

```http
GET /users/123
If-Modified-Since: Wed, 21 Oct 2026 07:28:00 GMT
→ 304 Not Modified
```

### Optimistic concurrency control

```http
PUT /users/123
If-Match: "v3-abc"
→ 200 OK (güncel) veya 412 Precondition Failed (başkası güncellemiş)
```

### Cache-Control directive'leri

```http
Cache-Control: public, max-age=3600                  # 1 saat herkese cache
Cache-Control: private, max-age=300                  # sadece browser
Cache-Control: no-cache                              # her seferinde validate
Cache-Control: no-store                              # asla cache'leme (PII)
Cache-Control: stale-while-revalidate=86400          # bayatken serv et, arkada yenile
```

### Stale-while-revalidate (RFC 5861)

> Pratikte CDN'lerin (Cloudflare, Vercel) en güçlü silahı. Cache expired olduğunda **cevap kullanıcıya gönderilir** ve aynı anda CDN arka planda yeniler.

---

## 9. ⏳ Long-Running Operations

### Pattern: Async with status polling

```http
POST /export-jobs
→ 202 Accepted
  Location: /export-jobs/abc123
  Retry-After: 5

GET /export-jobs/abc123
→ 200 OK
  {
    "status": "running",      // pending|running|completed|failed
    "progress": 0.45,
    "started_at": "...",
    "estimated_completion": "..."
  }

GET /export-jobs/abc123  (after some time)
→ 200 OK
  {
    "status": "completed",
    "result_url": "https://s3.../export.csv"
  }
```

### Webhook alternatifi

```http
POST /export-jobs
{
  "callback_url": "https://customer.example.com/webhook",
  ...
}
→ 202 Accepted

# Server iş bitince:
POST https://customer.example.com/webhook
X-Signature: sha256=...
{ "job_id": "abc123", "status": "completed", "result_url": "..." }
```

### LRO best practices

- ✅ **Idempotency-Key** ile tetikleme (yinelemez başlatma).
- ✅ **Cancel** endpoint'i (`DELETE /jobs/abc`).
- ✅ **TTL** — completed job'lar 7-30 gün sonra silinir.
- ✅ **Retry-After** süresi server tahmini ile.

---

## 10. 🔍 Filtering, Sorting, Field Selection

### Filtreleme

```http
GET /users?status=active&country=TR&created_after=2024-01-01
GET /users?filter[status]=active&filter[country]=TR     # JSON:API stili
```

### Karmaşık filtre — RSQL / FIQL

```http
GET /users?filter=status==active;country==TR;created_after=gt=2024-01-01
```

→ Public API'de kullanma; internal'da sorgu DSL eklenmesi pratik.

### Sıralama

```http
GET /users?sort=created_at,desc
GET /users?sort=-created_at,name      # - prefix = desc
```

### Sparse fieldsets (over-fetch önleme)

```http
GET /users/123?fields=id,name,email
```

veya GraphQL ile çözülür.

### Anti-pattern

- ❌ **Tüm tabloyu free-form filter** açma — N+1 / full scan riski.
- ❌ **WHERE injection** — filter input'unu raw SQL'e koyma.
- ❌ **Sayısız filter param** kombinasyonunu indekslememe — slow query.

---

## 11. 🪝 Webhooks

### Tasarım kuralları

```http
POST https://customer.example.com/webhook
X-Webhook-Signature: t=1700000000,v1=hex_hmac_sha256
X-Webhook-Event-ID: evt_abc123
X-Webhook-Event-Type: order.created
X-Webhook-Delivery-Attempt: 1
Content-Type: application/json
```

### Webhook checklist

- ✅ **HMAC imza** (timestamp + body).
- ✅ **Event ID** (idempotency için).
- ✅ **Timestamp** (replay attack'a karşı, ±5 dakika tolerans).
- ✅ **Retry policy** (exponential backoff, max attempt, DLQ).
- ✅ **Delivery attempt** sayacı header'da.
- ✅ **2xx = ack**, başka her şey retry.
- ✅ **Webhook log** dashboard'u customer için.

### Webhook security pattern: "thin payload"

```json
{
  "event_id": "evt_abc",
  "type": "order.completed",
  "object_url": "https://api.example.com/orders/12345"
}
```

→ Webhook payload'ı küçük, **signed URL** ile gerçek veriyi al. Avantajları:
- Webhook intercept edilse bile saldırgan veriye ulaşamaz (auth gerekir).
- Replay zararı azalır.

---

## 12. 🚫 API Tasarım Anti-Pattern'leri

### Top 15 hata

1. ❌ **HTTP verb'leri ihmal**: `POST /api/getUser` (RPC over HTTP).
2. ❌ **Status code'u 200'de tut**: `200 OK { success: false }`.
3. ❌ **Bulk endpoint yok**: 1000 kayıt güncellemek için 1000 HTTP call.
4. ❌ **Pagination yok**: List endpoint tüm tabloyu döner.
5. ❌ **Idempotency-Key yok**: Payment retry → çift charge.
6. ❌ **Hata formatı tutarsız** (RFC 9457 yok).
7. ❌ **Versioning yok / her endpoint farklı**.
8. ❌ **Deprecation süresi yok**: "Bugün kapattık".
9. ❌ **Rate limit yok**: Tek müşteri tüm sistemi yer.
10. ❌ **Authentication header yansıma** error log'da.
11. ❌ **Cursor opaque değil** + içeriğine bağımlı client.
12. ❌ **Date format inconsistency**: ISO 8601 her yerde olmalı.
13. ❌ **Boolean status string**: `"active"` vs `"inactive"` yerine sayısal/sayısallaşan kod.
14. ❌ **Snake_case + camelCase karışımı** aynı API'de.
15. ❌ **Documentation yok / OpenAPI eksik**: Swagger varsa otomatik.

### "İyi API" 10 maddelik kontrol listesi

- [ ] OpenAPI / Protobuf schema mevcut, CI'de validate.
- [ ] Tüm POST/PUT/PATCH idempotent (key veya doğal).
- [ ] Cursor pagination kullanılıyor (büyük listelerde).
- [ ] RFC 9457 hata formatı.
- [ ] Tüm tarihler ISO 8601 UTC.
- [ ] Versioning + deprecation politikası tanımlı.
- [ ] Rate limit + `RateLimit-*` header'ları + 429 + Retry-After.
- [ ] ETag/Last-Modified caching destekli.
- [ ] Webhook'lar HMAC imzalı + retry'lı.
- [ ] Uygun trace_id her response'ta.

---

## 📚 İleri Okuma

- **RFC 9457** — Problem Details for HTTP APIs (2024)
- **RFC 7807** — Problem Details (eski)
- **RFC 8594** — Sunset HTTP Header
- **RFC 5861** — Stale-While-Revalidate
- **RFC 5988** — Web Linking (`Link` header)
- **RFC 7232** — Conditional Requests
- **draft-ietf-httpapi-idempotency-key-header** — Idempotency-Key
- **draft-ietf-httpapi-ratelimit-headers** — RateLimit-* headers
- **JSON:API** specification — jsonapi.org
- **Microsoft REST API Guidelines** — github.com/microsoft/api-guidelines
- **Google API Design Guide** — cloud.google.com/apis/design
- **Stripe API** — pratisyenin görmesi gereken referans
- *Designing Web APIs* — Brenda Jin (O'Reilly)

> [⬅️ Pratik klasörü](README.md) · [📐 ADR şablonu](../templates/adr-sablon.md)
