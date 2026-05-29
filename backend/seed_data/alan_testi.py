# =========================================================
# BİLGİSAYAR MÜHENDİSLİĞİNDE HANGİ ALANA YÖNELMELİSİN?
# =========================================================
#
# Bu testte her şık doğrudan bir yazılım alanına puan verir.
#
# A şıkkı -> Veri Bilimi / Yapay Zeka
# B şıkkı -> Siber Güvenlik
# C şıkkı -> Backend / Sistem Mimarisi
# D şıkkı -> Frontend / UI-UX
#
# Backend seçilen şıkların puanlarını toplar
# ve en yüksek puanı alan alanı sonuç olarak döndürür.
# =========================================================


ALAN_TESTI = {
    "slug": "bilgisayar-muhendisligi-hangi-alan",
    "title": "Bilgisayar Mühendisliğinde Hangi Alana Yönelmelisin?",
    "short_title": "Hangi Alana Yönelmelisin?",
    "description": "Yazılım dünyasında sana en uygun alanı keşfet.",
    "category": "Kariyer",
    "icon": "💻",
    "button_text": "Alanını Bul",
    "display_order": 3,

    "profiles": [
        {
            "code": "YAPAY_ZEKA_VERI",
            "title": "Veri Bilimi / Yapay Zeka",
            "icon": "🤖",
            "description":
                "Senin baskın yönelimin veri bilimi ve yapay zeka tarafı. Çünkü sen bilgiyi yalnızca tüketen biri gibi değil, onun içindeki yapıyı çözen biri gibi düşünüyorsun. Dağınık görünen detayları bir araya getirip arkasındaki mantığı bulmak, belirsiz bir durumdan anlam çıkarmak ve “bunun örüntüsü ne, bunun sonucu nereye gider?” diye düşünmek senin doğal gücün. Bu yüzden senin için en doğru kulvar; veriden içgörü çıkaran, tahmin kuran, model geliştiren ve karmaşık bilgiyi karar desteğine dönüştüren roller. Kısacası sen sadece kod yazmaya değil, sistemlere öngörü kazandırmaya yatkınsın. Bu sonuç tesadüfi değil; çünkü veri bilimci rolleri veriden anlam üretme, veri madenciliği, modelleme, makine öğrenmesi ve görselleştirme üzerine kurulu, bu rolde de dikkat, merak ve analitik derinlik çok yüksek önem taşıyor." 
        },
        {
            "code": "SIBER_GUVENLIK",
            "title": "Siber Güvenlik",
            "icon": "🛡️",
            "description":
                "•	Senin baskın yönelimin siber güvenlik. Çünkü senin zihnin bir sistemin sadece çalışıp çalışmadığına bakmıyor; nereden kırılabileceğine, hangi açığın büyüyebileceğine ve hangi zayıf halkanın tüm yapıyı riske atabileceğine odaklanıyor. Bu bakış açısı teknik dünyada son derece değerlidir; çünkü gerçek güvenlik, olay olduktan sonra müdahale etmekten çok, olay olmadan önce doğru savunma mantığını kurabilmektir. Güvenlik önlemleri tasarlamak, açıkları fark etmek, koruma katmanları inşa etmek ve kriz anında soğukkanlı kalmak tam olarak bu profilin doğal uzantısıdır. Senin güçlü tarafın yalnızca “tedbirli” olmak değil; dijital düzeni koruma sorumluluğu taşıyan stratejik bir bakış geliştirmek. Bu yüzden senin için en isabetli alan siber güvenlik, güvenlik mühendisliği, tehdit analizi ve savunma mimarisi eksenidir. "
        },
        {
            "code": "BACKEND_SISTEM",
            "title": "Backend / Sistem Mimarisi",
            "icon": "⚙️",
            "description":
                "•	Senin baskın yönelimin backend, sistem mimarisi ve altyapı geliştirme tarafı. Çünkü sen teknolojiye yüzeyden değil, iskeletinden bakıyorsun. Bir ürünün gerçekten ayakta kalmasını sağlayan şeyin ekran değil; akış, entegrasyon, performans, dayanıklılık ve mantıklı kurgu olduğunu sezgisel olarak anlıyorsun. Parçaların birbirine nasıl bağlandığı, hangi bileşenin hangi yükü taşıdığı ve sistemin uzun vadede nasıl stabil kalacağı senin için temel başarı ölçütü. Bu yüzden senin güçlü alanın; ihtiyacı çalışan çözüme dönüştüren, bileşenleri planlayan, sistemleri ölçeklenebilir hale getiren ve görünmeyen omurgayı kuran mühendislik rolleridir. Kısacası sen sadece problemi çözen değil, o çözümü ayakta tutan yapıyı kuran kişisin; bu da seni backend, platform ve sistem tasarımı tarafında çok güçlü bir yere koyar. "
        },
        {
            "code": "FRONTEND_UIUX",
            "title": "Frontend / UI-UX",
            "icon": "🎨",
            "description":
                "•	Senin baskın yönelimin frontend, UI-UX ve ürün deneyimi tasarımı tarafı. Çünkü sen teknolojiye yalnızca “doğru çalışıyor mu?” sorusuyla yaklaşmıyorsun; “kullanıcı bunu nasıl algılıyor, ne kadar rahat kullanıyor, nasıl bir his bırakıyor?” tarafı senin için en az teknik doğruluk kadar önemli. Karmaşık bir yapıyı sade, akıcı ve sezgisel hale getirebilmek; estetik ile işlevselliği aynı anda koruyabilmek; kullanıcıyı yormayan ama etkileyen deneyimler tasarlamak bu profilin merkezinde yer alıyor. Bu yüzden senin doğal sahnen; arayüz, deneyim, etkileşim ve dijital ürün dili üzerine kurulu roller. Sen ürünün sadece dışını güzelleştiren biri değilsin; iç mantık ile insan deneyimi arasında köprü kuran taraftasın. Tam da bu nedenle frontend geliştirme, UI-UX ve dijital ürün tasarımı senin için en net yönelimdir."
        },
    ],

    "questions": [
        {
            "text": "Kitaplığınızı düzenlemeniz gerekse, hangi yöntem size en huzurlu hissettirir?",
            "options": [
                {
                    "key": "A",
                    "text": "Kitapları türlerine ve okunma sıklıklarına göre gruplayarak bir kullanım düzeni oluşturmak.",
                    "scores": {"YAPAY_ZEKA_VERI": 1}
                },
                {
                    "key": "B",
                    "text": "Kitapların formunu koruyacak, dış etkenlerden etkilenmeyecek bir yerleşim yapmak.",
                    "scores": {"SIBER_GUVENLIK": 1}
                },
                {
                    "key": "C",
                    "text": "Mevcut alanı en verimli şekilde kullanan, sarsılmayacak kadar dengeli bir yapı kurmak.",
                    "scores": {"BACKEND_SISTEM": 1}
                },
                {
                    "key": "D",
                    "text": "Kitapları dış görünümlerine ve renk tonlarına göre dizerek şık bir duruş sergilemek.",
                    "scores": {"FRONTEND_UIUX": 1}
                },
            ],
        },
        {
            "text": "Bir çalışma masasında sizi en çok ne mutlu eder?",
            "options": [
                {
                    "key": "A",
                    "text": "Karmaşık durumları takip edebileceğiniz, bol verili büyük ekranlar.",
                    "scores": {"YAPAY_ZEKA_VERI": 1}
                },
                {
                    "key": "B",
                    "text": "Kimsenin müdahale edemeyeceği, tamamen kişisel ve izole bir çalışma alanı.",
                    "scores": {"SIBER_GUVENLIK": 1}
                },
                {
                    "key": "C",
                    "text": "Her parçası yerli yerinde olan, fonksiyonel ve tıkır tıkır işleyen düzenli bir alan.",
                    "scores": {"BACKEND_SISTEM": 1}
                },
                {
                    "key": "D",
                    "text": "İlham veren renklerle, görsellerle ve estetik detaylarla dolu bir masa.",
                    "scores": {"FRONTEND_UIUX": 1}
                },
            ],
        },
        {
            "text": "Bir restorana gittiğinizde dikkatinizi ilk olarak ne çeker?",
            "options": [
                {
                    "key": "A",
                    "text": "Servis hızı ile müşteri memnuniyeti arasındaki genel denge ve restoranın doluluk oranı.",
                    "scores": {"YAPAY_ZEKA_VERI": 1}
                },
                {
                    "key": "B",
                    "text": "Mutfak ve hazırlık süreçlerinin ne kadar şeffaf ve kurallara uygun olduğu.",
                    "scores": {"SIBER_GUVENLIK": 1}
                },
                {
                    "key": "C",
                    "text": "Restoranın genel operasyonel düzeni ve siparişten teslime kadar geçen sürecin akışı.",
                    "scores": {"BACKEND_SISTEM": 1}
                },
                {
                    "key": "D",
                    "text": "Mekanın dekorasyonu, ışıklandırması ve sunum tabağının genel estetiği.",
                    "scores": {"FRONTEND_UIUX": 1}
                },
            ],
        },
        {
            "text": "Bir arkadaş grubunda tatil planı yaparken rolünüz ne olur?",
            "options": [
                {
                    "key": "A",
                    "text": "Hava durumu, fiyatlar ve etkinlik verilerini toplayıp en mantıklı seçeneği sunan.",
                    "scores": {"YAPAY_ZEKA_VERI": 1}
                },
                {
                    "key": "B",
                    "text": "Grubun güvenliğini sağlayan, riskleri minimize eden koruyucu.",
                    "scores": {"SIBER_GUVENLIK": 1}
                },
                {
                    "key": "C",
                    "text": "Ulaşım, konaklama ve rezervasyon gibi sistemin işlemesini sağlayan kurucu.",
                    "scores": {"BACKEND_SISTEM": 1}
                },
                {
                    "key": "D",
                    "text": "Gidilecek yerlerin fotoğraflarını seçen ve grubun enerjisini yüksek tutan vizyoner.",
                    "scores": {"FRONTEND_UIUX": 1}
                },
            ],
        },
        {
            "text": "Bir gerilim filmi izlerken zihniniz en çok hangi noktaya takılır?",
            "options": [
                {
                    "key": "A",
                    "text": "Olay örgüsündeki küçük ipuçlarını birleştirerek sonucun nereye varacağını erkenden bulmaya.",
                    "scores": {"YAPAY_ZEKA_VERI": 1}
                },
                {
                    "key": "B",
                    "text": "Karakterlerin yaptığı dikkatsizlikleri yakalayıp kriz anında nerede hata yaptıklarını görmeye.",
                    "scores": {"SIBER_GUVENLIK": 1}
                },
                {
                    "key": "C",
                    "text": "Hikayenin kurgusundaki mantık hatalarına ve olayların birbirine bağlanma şekline.",
                    "scores": {"BACKEND_SISTEM": 1}
                },
                {
                    "key": "D",
                    "text": "Sahnelerin yarattığı atmosfere, dekorlara ve izleyicide bıraktığı genel duyguya.",
                    "scores": {"FRONTEND_UIUX": 1}
                },
            ],
        },
        {
            "text": "Problem çözerken en çok hangi hal size kendinizi güçlü hissettirir?",
            "options": [
                {
                    "key": "A",
                    "text": "Bilgi kırıntılarını birleştirip, kimsenin göremediği ana fikre ulaştığınız an.",
                    "scores": {"YAPAY_ZEKA_VERI": 1}
                },
                {
                    "key": "B",
                    "text": "Bir açığı veya zayıf halkayı erkenden fark edip müdahale ettiğiniz an.",
                    "scores": {"SIBER_GUVENLIK": 1}
                },
                {
                    "key": "C",
                    "text": "Bir mekanizmayı en ince ayrıntısına kadar planlayıp kusursuz çalıştırdığınız an.",
                    "scores": {"BACKEND_SISTEM": 1}
                },
                {
                    "key": "D",
                    "text": "Tasarladığınız bir şeyin insanlar tarafından hayranlıkla karşılandığı an.",
                    "scores": {"FRONTEND_UIUX": 1}
                },
            ],
        },
        {
            "text": "Size bir süper güç verilecek olsa, hangisini seçerdiniz?",
            "options": [
                {
                    "key": "A",
                    "text": "Geleceği görme gücü.",
                    "scores": {"YAPAY_ZEKA_VERI": 1}
                },
                {
                    "key": "B",
                    "text": "Görünmez olma gücü.",
                    "scores": {"SIBER_GUVENLIK": 1}
                },
                {
                    "key": "C",
                    "text": "Nesneleri kontrol edebilme gücü.",
                    "scores": {"BACKEND_SISTEM": 1}
                },
                {
                    "key": "D",
                    "text": "Dünyayı daha iyi bir yere dönüştürme gücü.",
                    "scores": {"FRONTEND_UIUX": 1}
                },
            ],
        },
        {
            "text": "Yeni bir şehre taşındığınızda ilk olarak neyle ilgilenirsiniz?",
            "options": [
                {
                    "key": "A",
                    "text": "İnsanların yaşam tarzını ve şehrin genel düzenini gözlemlemekle.",
                    "scores": {"YAPAY_ZEKA_VERI": 1}
                },
                {
                    "key": "B",
                    "text": "Güvenli bölgeleri ve dikkat edilmesi gereken yerleri öğrenmekle.",
                    "scores": {"SIBER_GUVENLIK": 1}
                },
                {
                    "key": "C",
                    "text": "Ulaşımın, yolların ve günlük işleyişin ne kadar düzenli olduğunu çözmekle.",
                    "scores": {"BACKEND_SISTEM": 1}
                },
                {
                    "key": "D",
                    "text": "Şehrin en güzel mekanlarını, kafelerini ve estetik noktalarını keşfetmekle.",
                    "scores": {"FRONTEND_UIUX": 1}
                },
            ],
        },
        {
            "text": "Çocukken bir oyuncağınız bozulduğunda ilk refleksiniz ne olurdu?",
            "options": [
                {
                    "key": "A",
                    "text": "İçini açıp neden bozulduğunu anlamaya çalışmak.",
                    "scores": {"YAPAY_ZEKA_VERI": 1}
                },
                {
                    "key": "B",
                    "text": "Bir daha bozulmaması için daha dikkatli kullanmak.",
                    "scores": {"SIBER_GUVENLIK": 1}
                },
                {
                    "key": "C",
                    "text": "Parçalarını söküp farklı şekilde çalıştırmayı denemek.",
                    "scores": {"BACKEND_SISTEM": 1}
                },
                {
                    "key": "D",
                    "text": "Görünüşünü değiştirip daha güzel hale getirmek.",
                    "scores": {"FRONTEND_UIUX": 1}
                },
            ],
        },
        {
            "text": "Bir uygulamayı veya oyunu uzun süre kullanmaya devam etmenizi en çok ne sağlar?",
            "is_tiebreaker": True,
            "tiebreaker_order": 1,
            "options": [
                {
                    "key": "A",
                    "text": "Zamanla yeni şeyler keşfettirmesi ve sizi düşündürmeye devam etmesi.",
                    "scores": {"YAPAY_ZEKA_VERI": 1}
                },
                {
                    "key": "B",
                    "text": "Güven vermesi, sorunsuz çalışması ve hata hissi oluşturmaması.",
                    "scores": {"SIBER_GUVENLIK": 1}
                },
                {
                    "key": "C",
                    "text": "Hızlı, akıcı ve her şeyin düzenli işlemesi.",
                    "scores": {"BACKEND_SISTEM": 1}
                },
                {
                    "key": "D",
                    "text": "Görsel tarzı, atmosferi ve kullanıcıya hissettirdiği deneyim.",
                    "scores": {"FRONTEND_UIUX": 1}
                },
            ],
        },
    ],
}