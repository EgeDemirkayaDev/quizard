```mermaid
erDiagram
    kullanicilar ||--o{ favoriler : "sahiptir"
    kullanicilar ||--o{ kaydedilenler : "kaydeder"
    kullanicilar ||--o{ yorumlar : "yazar"
    testler ||--o{ favoriler : "eklenir"
    testler ||--o{ kaydedilenler : "kaydedilir"
    testler ||--o{ yorumlar : "alır"

    kullanicilar {
        INT id PK "Otomatik Artan"
        VARCHAR kullanici_adi "Benzersiz (Unique)"
        VARCHAR eposta "Benzersiz (Unique)"
        VARCHAR sifre_hash
        BOOLEAN bildirimler_acik
        VARCHAR tema_tercihi
        BOOLEAN aktif_mi
        TIMESTAMP olusturulma_tarihi
    }

    testler {
        INT id PK "Otomatik Artan"
        VARCHAR baslik
        TEXT aciklama
        VARCHAR ikon
        VARCHAR buton_metni
    }

    favoriler {
        INT id PK
        INT kullanici_id FK "CASCADE"
        INT test_id FK "CASCADE"
        TIMESTAMP olusturulma_tarihi
    }

    kaydedilenler {
        INT id PK
        INT kullanici_id FK "CASCADE"
        INT test_id FK "CASCADE"
        TIMESTAMP olusturulma_tarihi
    }

    yorumlar {
        INT id PK
        INT kullanici_id FK "CASCADE"
        INT test_id FK "CASCADE"
        TEXT icerik
        TIMESTAMP olusturulma_tarihi
    }
```