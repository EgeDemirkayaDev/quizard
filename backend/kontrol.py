from database import motor, Taban
from sqlalchemy import text
import models

try:
    print("Veritabanı temizliğine başlanıyor...")
    with motor.begin() as baglanti:
        # 1. Korumaları geçici olarak kapat (Kancaları sök)
        baglanti.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
        
        # 2. Eski ve hayalet tabloların hepsini acımadan sil
        baglanti.execute(text("DROP TABLE IF EXISTS kaydedilenler, yorumlar, favoriler, secenekler, test_sonuclari, sorular, testler, kullanicilar;"))
        
        # 3. Korumaları geri aç
        baglanti.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
        
    print("🧹 Eski hayalet tablolar başarıyla temizlendi!")
    
    # 4. Yeni mimariyle tertemiz inşa et
    Taban.metadata.create_all(bind=motor)
    print("🎉 BİNGO! Yeni tablolar kusursuz şekilde kuruldu!")
    
except Exception as hata:
    print("🚨 Ups! Bir sorun var:", hata)