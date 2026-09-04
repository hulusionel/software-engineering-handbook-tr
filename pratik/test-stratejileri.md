# 🧪 Test Stratejileri

> **"Tests are the way you put your faith into your design."** — Kent Beck

Bu doküman modern test disiplinlerini kapsar: test pyramid'in ötesinde, property-based, mutation, contract, snapshot, fuzzing.

---

## 📑 İçindekiler

1. [Test Pyramid (ve Eleştirisi)](#1-test-pyramid-ve-eleştirisi)
2. [Unit Test Disiplini](#2-unit-test-disiplini)
3. [Integration Test](#3-integration-test)
4. [Contract Testing](#4-contract-testing)
5. [E2E ve Smoke Test](#5-e2e-ve-smoke-test)
6. [Property-Based Testing](#6-property-based-testing)
7. [Mutation Testing](#7-mutation-testing)
8. [Snapshot Testing](#8-snapshot-testing)
9. [Fuzzing](#9-fuzzing)
10. [Performance Test](#10-performance-test)
11. [Test Anti-Pattern'leri](#11-test-anti-patternleri)

---

## 1. Test Pyramid (ve Eleştirisi)

### Klasik (Mike Cohn 2009)

```
       ▲    E2E
      ▲▲    Service / Integration
    ▲▲▲▲    Unit
```

**Mantık:**
- Unit: çok, hızlı, ucuz, izole.
- E2E: az, yavaş, kırılgan, ama gerçek.

### "Trophy" (Kent C. Dodds, frontend)

```
        🏆     E2E
       🏆🏆    Integration  ← AĞIRLIK BURADA
      🏆🏆🏆   Unit
     🏆🏆🏆🏆  Static (linting, types)
```

**Mantık:** Modern app'te gerçek değer integration'da. Unit test çoğu zaman implementation detail test eder.

### Karşıt: Ice Cream Cone (anti-pattern)

```
    ▼     Manual
   ▼▼     E2E (çok)
  ▼▼▼     Integration
 ▼▼▼▼     Unit (az)
```

❌ Yavaş, kırılgan, maintenance kabusu.

### Pragmatik öneri

| Servis tipi | Pyramid |
|---|---|
| Pure logic library | Klasik (unit ağırlıklı) |
| API server | Trophy (integration ağırlıklı) |
| Frontend | Trophy |
| Distributed system | Trophy + chaos test |
| Embedded | Klasik + hardware-in-loop |

---

## 2. Unit Test Disiplini

### Tanım

- **Tek bir unit** test edilir (function, class).
- Diğer unit'ler **mock**'lanır veya gerçek kullanılır (granularity tartışma).
- **Hızlı** (< 100ms her test).
- **İzole** (sıralama bağımsız).

### Detroit (Classical) vs London (Mockist)

| | Detroit | London |
|---|---|---|
| Mock | Az kullan | Çok kullan |
| Test | State/output | Behavior/interaction |
| Fail | Implementation değişimine sağlam | Refactor hassas |
| Hız | Real DB ile yavaş | Çok hızlı |

> **Kent Beck (Detroit):** "Test the public interface, not implementation."
> **Steve Freeman (London):** "Test interaction patterns explicitly."

> Modern denge: Domain logic Detroit, infrastructure boundary London.

### AAA / Given-When-Then

```javascript
test('discount applied to over-100 orders', () => {
  // Arrange / Given
  const order = new Order({ items: [{ price: 150 }] });

  // Act / When
  order.applyDiscount();

  // Assert / Then
  expect(order.total).toBe(150 * 0.9);
});
```

### Test isolation

- Her test kendi setup/teardown.
- Shared fixture = bug magnet.
- Random order ile çalıştır (fail bulmak için).

### Coverage anlamlı mı?

> **Coverage hedef değil, sinyaldir.**
> %80 coverage + assertion'sız test = sahte güven.

**Daha iyi sinyaller:**
- Mutation score (Stryker, Pitest).
- Production bug ↔ test miss correlation.
- New code coverage > existing.

---

## 3. Integration Test

### Tanım

> Birden fazla unit'in **birlikte** doğru çalıştığını doğrular. Genelde gerçek DB, gerçek HTTP server, gerçek queue.

### Testcontainers

```java
@Testcontainers
class OrderServiceTest {
  @Container
  static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:16");

  @Test
  void createsOrder() {
    // Real Postgres in container, throwaway after test
  }
}
```

> Java, Go, Python, Node, .NET, Rust — Testcontainers yaygın.

### "Real dep" vs Mock

| | Real (Testcontainers) | Mock |
|---|---|---|
| Confidence | Yüksek | Düşük |
| Speed | Yavaş (saniyeler) | Hızlı (ms) |
| Setup | Karmaşık | Basit |
| Coverage | Real bug yakalar | Sahte yeşil |

**Modern öneri:** Hybrid — DB / queue **gerçek**, external API **mock** (cost + reliability).

### In-memory alternatifler

- H2 (Java) — Postgres emulation. **Fakat:** SQL dialect uyumsuzlukları.
- SQLite for Postgres — kötü idea, syntax/feature farkı.
- LocalStack — AWS emulation.
- KIND / k3d — local K8s.

> En doğrusu: production-parity. SQLite ile Postgres test = false confidence.

---

## 4. Contract Testing

### Niye?

> E2E pahalı, kırılgan. Microservice'lerin **birlikte çalıştığını** kanıtlamak için her seferinde tüm sistem ayakta tutulmaz.

**Çözüm:** Provider ↔ Consumer arasında **kontrat**.

### Pact (consumer-driven)

```javascript
// Consumer side: kontrat oluştur
provider.given('user 1 exists')
  .uponReceiving('a request for user 1')
  .withRequest({ method: 'GET', path: '/users/1' })
  .willRespondWith({
    status: 200,
    body: { id: 1, name: 'Alice' }
  });

// Bu kontrat broker'a yüklenir.

// Provider side: kontratı verify et
verifier.verify(); // Provider'a istek gönder, response'u kontrate karşı kontrol et
```

### Süreç

```
1. Consumer test → kontrat dosyası
2. Pact Broker'a yükle
3. Provider CI'da broker'dan al, verify
4. Verify pass → can-i-deploy yeşil
5. Provider deploy
6. Consumer deploy
```

### Pros / Cons

✅ E2E olmadan integration confidence.
✅ Breaking change provider tarafında erkenden tespit.
❌ Setup overhead.
❌ Kontrat eskidiğinde yanlış güven.

### OpenAPI / AsyncAPI alternatif

Schema-first API → linting + validation. Pact'tan basit ama daha az dynamic.

---

## 5. E2E ve Smoke Test

### E2E

> Browser/client → tüm zincir → DB → response. Real UI test.

Tools:
- **Playwright** — modern, stable, multi-browser.
- **Cypress** — JavaScript-only, dev experience iyi.
- **Selenium** — klasik, yavaş.

### Smoke test

> Deploy sonrası **temel akış çalışıyor mu?** Hızlı sanity check.

```
- /health endpoint OK?
- Login flow çalışıyor?
- Order create endpoint başarılı?
```

5-10 test, 1-2 dakika.

### Synthetic monitoring

> Production'da **periyodik** E2E. Real user'dan önce bug yakalar.

Tools: Datadog Synthetics, New Relic, Checkly, Grafana k6.

### "Test in production"

- Synthetic monitoring.
- Real user monitoring (RUM).
- Feature flag kademeli rollout.
- Canary deployment.

> "Test in production" ≠ "production'da hata bul." → "Production yapılarını **kasıtlı** olarak izle."

---

## 6. Property-Based Testing

> John Hughes, *QuickCheck* (Haskell, 1999). "Bu input'larda" değil "her input'ta" özellik test.

### Klasik unit test

```python
def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]
```

### Property-based

```python
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_reverse_twice_is_identity(xs):
    assert reverse(reverse(xs)) == xs

@given(st.lists(st.integers()))
def test_reverse_preserves_length(xs):
    assert len(reverse(xs)) == len(xs)
```

### Tools

| Dil | Tool |
|---|---|
| Haskell | QuickCheck |
| Scala | ScalaCheck |
| JS/TS | fast-check |
| Python | Hypothesis |
| Rust | proptest, quickcheck |
| Java | jqwik |
| Go | testing/quick (built-in) |

### Shrinking

> Property fail ettiğinde, **minimal counter-example** bulur.

```
Test failed: input=[5, 23, -7, 100, 0]
Shrinking → [0]  # minimal failing input
```

### Use case

- Pure function (parser, serializer, math).
- Invariant (idempotency, commutativity).
- Round-trip (encode → decode = identity).
- State machine model.

### Limitations

- Stateful side-effect zor.
- Distributed system için **deterministic simulator** + property check daha güçlü.

---

## 7. Mutation Testing

### Niye?

> Test coverage'ı **gerçek anlamda** ölçer.

```
1. Kod: if (x > 10) ...
2. Mutator: if (x >= 10), if (x < 10), if (true), ...
3. Her mutant için test çalıştır.
4. Mutant survived = test gap.
```

### Skor

```
Killed mutants / total mutants
   %90+ = excellent
   %70-90 = good
   < %50 = test seti zayıf
```

### Tools

- **Stryker** (JS, TS, C#).
- **PIT / Pitest** (Java).
- **Cosmic Ray** (Python).
- **mutmut** (Python).
- **mull** (C++).

### Trade-off

- Hesaplama pahalı (her mutant test run).
- Genelde nightly veya pre-release.
- Hot module / critical path için reasonable.

---

## 8. Snapshot Testing

### Tanım

```javascript
test('user serialization', () => {
  expect(serialize(user)).toMatchSnapshot();
});
```

İlk run → snapshot dosyası kaydet. Sonraki run'lar → diff.

### İyi kullanım

- Output format stable.
- Component render (frontend).
- API response shape.

### Tehlike

- 🚨 **Otomatik update** alışkanlığı: `jest --updateSnapshot` her seferinde → review yok, bug görünmez.
- 🚨 Büyük snapshot → review imkansız.
- 🚨 Inline data → ne test ettiğin belirsiz.

### Disiplin

- Snapshot küçük + odaklı.
- Update **manuel review** sonrası.
- Behavior assertion'la kombinle, snapshot **tek kaynak değil**.

---

## 9. Fuzzing

### Random input dump

```bash
echo "random data" | parser  # crash bulmak için
```

### Coverage-guided fuzzing

> AFL, libFuzzer, Go fuzz, cargo-fuzz — **kod kapsamını** maximize eden input'ları üretir.

```go
// Go 1.18+ built-in
func FuzzParse(f *testing.F) {
    f.Add("hello")
    f.Fuzz(func(t *testing.T, s string) {
        Parse(s)  // crash, panic, hang yakalanır
    })
}
```

### Use case

- Parser, serializer.
- Network protocol.
- File format reader.
- Cryptographic primitive.
- Security boundary.

### OSS-Fuzz (Google)

> 1000+ open-source projeyi sürekli fuzz eder. Şimdiye kadar **40,000+ bug** bulundu.

---

## 10. Performance Test

### Çeşitleri

| Tip | Amaç |
|---|---|
| **Load test** | Beklenen yük altında SLO sağlanıyor mu? |
| **Stress test** | Sistem nerede patlar? |
| **Spike test** | Ani trafiğe dayanır mı? |
| **Soak test** | Saatler / günler boyunca stabil mi? (memory leak) |
| **Scalability test** | Linear scale ediyor mu? |

### Tools

- **k6** (Grafana) — JS-based, modern.
- **Gatling** — Scala/Java.
- **wrk2** — coordinated omission'sız.
- **Apache JMeter** — geniş protocol desteği.
- **Locust** — Python.

### Coordinated omission

> wrk, ab, JMeter klasik mod → kuyrukta beklemeyi ölçmüyor → yanıltıcı p99.

**Çözüm:** wrk2, gatling, k6 (constant arrival rate). HdrHistogram.
> Detay: [latency-numbers-ve-kapasite-matematigi.md](latency-numbers-ve-kapasite-matematigi.md) #6

### Baseline + regression

- Her major release öncesi load test.
- Baseline ile karşılaştır.
- %10+ regression = block.

---

## 11. Test Anti-Pattern'leri

### 1. Flaky test

```
Test geçer / kalır random.
"Retry yapsın" sloganı = bug görmezlikten gelme.
```

**Çözüm:** Quarantine + 1 hafta içinde fix veya delete. Asla retry.

### 2. Test interdependence

Test A, B'nin bıraktığı state'e bağlı.

**Çözüm:** Per-test isolation. Random order.

### 3. Implementation-detail test

```javascript
// ❌
expect(myObject.privateInternalCache.size).toBe(3);
```

Refactor → test kırılır. Unit test refactor güveni vermek için var, kırılganlık yaratmak için değil.

**Çözüm:** Public behavior test.

### 4. Mock everything

```javascript
mock(databaseConnection);
mock(httpClient);
mock(timeProvider);
mock(randomGenerator);
mock(...);
// Sonra test geçiyor ama sistem çalışmıyor.
```

**Çözüm:** Sınır mock (network, disk, time). Domain logic real.

### 5. God test

500 satır tek test. Setup karmaşık, assertion belirsiz.

**Çözüm:** Tek test = tek davranış.

### 6. Comment as docstring

```python
def test_user_can_login():
    # Tests user login. Logs in user, checks token.
    ...  # Test name zaten anlatıyor
```

**Çözüm:** Test ismi descriptif, comment gereksiz.

### 7. Test data builders'sız

Setup boilerplate her testte tekrar.

**Çözüm:** Object Mother, Builder pattern.

### 8. Slow unit tests

Unit test 5 saniye. CI suite saatler.

**Çözüm:** Real DB integration'a kaydır. Unit'i pure logic + fast tut.

### 9. No async test handling

```javascript
test('async', () => {
  doAsync();  // missing await
  expect(...).toBe(...);  // timing race
});
```

### 10. Test code'u review'sız

> Test code = production code. Review aynı disiplinle.

---

## 🎯 Staff+ Test Stratejisi

### Karar matrisi

| Code tipi | Test stratejisi |
|---|---|
| Pure function | Unit + property-based |
| API endpoint | Integration (Testcontainers) + contract |
| UI component | Snapshot + interaction |
| Database access | Integration (real DB) |
| Distributed protocol | Property-based + simulation |
| Parser / serializer | Fuzz + property-based |
| Critical security path | Mutation testing |
| Performance hot path | Load test baseline + regression |

### Quality gates

- ✅ PR pre-merge: lint + unit + integration < 10 dk.
- ✅ Pre-deploy: smoke + E2E (key flows) < 30 dk.
- ✅ Periodic: mutation, fuzz, load (nightly / weekly).
- ✅ Pre-release: full regression + performance.

---

## 📚 İleri Okuma

- *Unit Testing* — Vladimir Khorikov ([özet](../kod-kalitesi/unit-testing-turkce.md))
- *Test-Driven Development* — Kent Beck
- *Growing Object-Oriented Software, Guided by Tests* — Freeman & Pryce
- *xUnit Test Patterns* — Gerard Meszaros
- *Property-Based Testing with PropEr, Erlang, and Elixir* — Fred Hebert
- John Hughes — QuickCheck papers
- "How SQLite Is Tested" — sqlite.org/testing.html

> [⬅️ Pratik klasörü](README.md) · [📚 Sözlük](../glossary/terim-sozlugu.md) · [🔬 Kaynakça](../kaynakca.md)
