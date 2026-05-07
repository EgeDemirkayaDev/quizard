from database import motor, Taban
import models # Tablolarımızı (Modelleri) içeri alıyoruz ki motor görsün

try:
    print("Veritabanına bağlanılmaya çalışılıyor...")
    
    # Bu sihirli kod, models.py'daki her şeye bakar ve MySQL'de yoksa otomatik oluşturur.
    Taban.metadata.create_all(bind=motor)
    
    print("🎉 BİNGO! Veritabanı bağlantısı kusursuz çalışıyor!")
    print("✅ Bütün tablolar MySQL'de hazır ve nazır. Backend ekibi işe başlayabilir!")
    
except Exception as hata:
    print("🚨 Ups! Bir sorun var. Şifreni veya MySQL'in açık olup olmadığını kontrol et.")
    print("Hata detayı:", hata)