from database import OturumYerel
from models import Test, Soru, Secenek

def verileri_yukle():
    db = OturumYerel()
    
    try:
        # 1. Önce Testin Kendisini Oluşturuyoruz
        yeni_test = Test(
            baslik="Trakya Üniversitesi'nde Hangi Hoca Olurdun?",
            aciklama="Trakya Üniversitesi Bilgisayar Mühendisliği bölümündeki efsane hocalardan hangisisin? Çöz ve öğren!",
            kategori="Eğlence",
            ikon="🎓"
        )
        db.add(yeni_test)
        db.commit()
        db.refresh(yeni_test)
        
        # 2. Soruları ve Şıkları Ekliyoruz
        sorular_ve_siklar = [
            {
                "metin": "1. Sabah 08:30 dersi için sınıfa giriş politikan nedir?",
                "secenekler": [
                    {"metin": "Kapı saniyeler içinde kapanır. 1 dakika geç kalanı bile içeri almam.", "etiket": "Turgut"},
                    {"metin": "10-15 dakika opsiyon tanırım. Geç gelenlere hadi geçin derim.", "etiket": "Aydın"},
                    {"metin": "Derse kimin girip çıktığıyla ilgilenmem, ben dersimi anlatırım.", "etiket": "Deniz"},
                    {"metin": "8:30 dersi ne ya? Onu ilk gün 10:00 dersi yapmışımdır zaten.", "etiket": "Özlem"}
                ]
            },
            {
                "metin": "2. Yoklamada imza sayısı ile sınıftaki kişi sayısı tutmuyor. Ne yaparsın?",
                "secenekler": [
                    {"metin": "İsimleri tek tek okurum, bir hata varsa asla affetmem.", "etiket": "Turgut"},
                    {"metin": "Tutarsızlık hissedersem öğrencilere laf söyler geçerim.", "etiket": "Fatma"},
                    {"metin": "Hocam siler misiniz diyene mail at halledelim derim.", "etiket": "Derya"},
                    {"metin": "İmza sayısını neden sayayım ki bence bunlar gereksiz şeyler.", "etiket": "Emir"}
                ]
            },
            {
                "metin": "3. Ödev 1 gün geç atılmış olsun. Puanlaman nasıl olur?",
                "secenekler": [
                    {"metin": "Asla tolerans göstermem, direkt 0 veririm.", "etiket": "Aydın"},
                    {"metin": "Ödev teslimi nedir? Bir de ödev okumakla mı uğraşacağız?", "etiket": "Fatma"},
                    {"metin": "Vaktinden geç gelse de kabul ederim, puan da kırmam.", "etiket": "Deniz"},
                    {"metin": "Çok geçerli bir sebebi varsa kabul ederim.", "etiket": "Emir"}
                ]
            }
            # Kanka test uzamasın diye şimdilik ilk 3 soruyu koydum, mantığı anladın :)
        ]

        # Döngü ile soruları ve şıkları veritabanına basıyoruz
        for i, soru_data in enumerate(sorular_ve_siklar):
            yeni_soru = Soru(
                test_id=yeni_test.id,
                soru_metni=soru_data["metin"],
                sira=i+1
            )
            db.add(yeni_soru)
            db.commit()
            db.refresh(yeni_soru)

            # Bu sorunun şıklarını ekliyoruz
            for secenek_data in soru_data["secenekler"]:
                yeni_secenek = Secenek(
                    soru_id=yeni_soru.id,
                    metin=secenek_data["metin"],
                    etiket=secenek_data["etiket"], # Hangi hocaya puan vereceği burada!
                    puan_agirligi=1.0
                )
                db.add(yeni_secenek)
            
            db.commit()

        print("🎉 BİNGO! Hoca Testi, soruları ve benzersiz ID'li şıklarıyla veritabanına eklendi!")
        
    except Exception as e:
        print("🚨 Hata oluştu:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Veriler veritabanına işleniyor, lütfen bekleyin...")
    verileri_yukle()