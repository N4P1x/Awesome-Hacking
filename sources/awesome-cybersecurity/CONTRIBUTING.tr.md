# Katkı Rehberi

🇬🇧 [English contributing guide](CONTRIBUTING.md)

Bu listeyi birlikte büyütelim. Yeni kaynak eklemeden veya düzeltme yapmadan önce aşağıdaki kurallara göz atın.

## Kaynak Ekleme Kriterleri

Bir kaynağın listeye girmesi için:

1. **Aktif ve güvenilir** olmalı (son 12 ayda güncellenmiş veya köklü bir referans).
2. **Yasal ve etik** olmalı. Korsan içerik, sızdırılmış kurs, crack, zararlı yazılım dağıtan siteler **kabul edilmez**.
3. **Doğru kategoriye** eklenmeli. Birden fazla alana uyuyorsa ilgili tüm bölümlere eklenebilir.
4. **Fiyat bilgisi** rozetle belirtilmeli:
   - 🟢 Ücretsiz
   - 🟡 Freemium (ücretsiz katman + ücretli)
   - 🔴 Ücretli
5. **Yön / Rol rozeti** belirtilmeli:
   - ⚔️ Ofansif: Pentest, Web, Bug Bounty, Red Team, Exploit/RE, Mobil, API, Bulut, AI Red Team, CTF
   - 🛡️ Defansif: SOC, DFIR, Tespit, Zararlı Analizi, AppSec, Zafiyet Yön., Sertleştirme, Tehdit İst., Bulut Güvenliği
   - ⚔️🛡️ Karma: hem ofansif hem defansif içerik sunan kaynaklar (Purple Team)
   - 🏛️ GRC: yönetişim, risk, uyum
   - 🧩 Ortak: temeller, kriptografi, standartlar, haber, genel kaynaklar

   Rozet, kaynağın **ağırlıklı içeriğine** göre seçilir. Emin değilseniz PR açıklamasında belirtin.
6. Reklam veya affiliate bağlantısı içermemeli; resmi bağlantı kullanılmalı.

## Dil ve Dosyalar

Liste iki dosyada tutulur: **README.md** (İngilizce) ve **OKUBENI.md** (Türkçe). Eklediğiniz kaynağı iki dosyaya da, aynı bölüme ve aynı tabloya ekleyin. Türkçe veya İngilizce yazamıyorsanız PR açıklamasında belirtin; bakımcılar karşı dili tamamlar.

## Satır Formatı

Her bölümde iki tablo vardır: **🟢 Ücretsiz** ve **💳 Ücretli**. Tamamen ücretsiz kaynaklar (🟢) ilk tabloya, ücretsiz katmanı olan (🟡) veya ücretli (🔴) kaynaklar ikinci tabloya eklenir. Tabloda yalnızca kaynak listelenir; "şuradan başla" gibi öğrenme yolu veya sıralama önerileri eklenmez.

Tablolardaki sütun sırasını koruyun. Örnek:

```markdown
| [Kaynak Adı](https://ornek.com) | ⚔️ Pentest | Tür | 🟡 | Başlangıç | Tek cümlelik, tarafsız açıklama |
```

Sütun sırası: **Kaynak · Yön / Rol · Tür · Fiyat · Seviye · Not**. (Bazı tablolarda Tür veya Seviye sütunu yoktur; o bölümdeki mevcut sütunları izleyin.)

- Tablolar **alfabetik** veya **seviye sırasına** göre tutulur; mevcut düzeni bozmayın.
- Açıklama tek cümle olmalı; pazarlama dili kullanmayın.
- Kesin fiyat yazmayın (değişkendir); rozet yeterli.

## Pull Request Kontrol Listesi

- [ ] Bağlantı çalışıyor ve resmi kaynağa gidiyor
- [ ] Fiyat rozeti doğru
- [ ] Yön / Rol rozeti doğru
- [ ] Seviye ve tür doğru
- [ ] Doğru bölümde ve aynı biçimde
- [ ] Aynı kaynak listede zaten yok
- [ ] Kaynak hem README.md hem OKUBENI.md dosyasına eklendi
- [ ] Kaynak sayısı değiştiyse README.md ve OKUBENI.md'deki `resources` rozeti güncellendi

## Güncelleme ve Düzeltme

Fiyat, plan veya sertifika adı değiştiyse PR açın ve değişikliğin kaynağını (resmi sayfa bağlantısı) PR açıklamasına ekleyin.

## Bağlantı Kontrolü

Repo, her hafta ve her PR'da bağlantıları otomatik denetleyen bir GitHub Actions iş akışı içerir (`.github/workflows/link-check.yml`). Kırık bağlantı raporlarını issue olarak açabilir veya doğrudan düzeltme PR'ı gönderebilirsiniz.

## Yerel Kontrol

PR açmadan önce `python scripts/validate.py` komutunu çalıştırın (Python 3, ek bağımlılık yok). Bu betik `README.md` ve `OKUBENI.md` dosyalarının aynı kaynakları listelediğini, tabloların düzgün olduğunu, sayfa içi bağlantıların çalıştığını ve `resources` rozetinin doğru olduğunu denetler. Aynı kontrol her PR'da otomatik de çalışır.

Kaynak önermek veya kırık bağlantı bildirmek için [issue şablonlarını](https://github.com/cveburak/awesome-cybersecurity/issues/new/choose) da kullanabilirsiniz.

## Davranış

Saygılı olun. Kişisel saldırılara ve rekabet amaçlı kaynak kötülemeye yer yok. [Davranış Kuralları](.github/CODE_OF_CONDUCT.md) dosyasına bakın.
