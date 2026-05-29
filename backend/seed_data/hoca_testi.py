# =========================================================
# TÜ'DE HANGİ HOCA OLURDUN TESTİ
# =========================================================
#
# Bu testte her seçenek tek bir hocaya değil,
# bazen birden fazla hocaya puan verebilir.
#
# Örnek:
# C şıkkı hem Emir'e hem Derya'ya hem Deniz'e yakınsa
# üç profile de puan eklenir.
# =========================================================


HOCA_TESTI = {
    "slug": "tu-hangi-hoca-olurdun",
    "title": "TÜ’de Hangi Hoca Olurdun?",
    "short_title": "TÜ’de Hangi Hoca Olurdun?",
    "description": "Trakya Üniversitesi Bilgisayar Mühendisliği ruhunu test et.",
    "category": "Eğlence",
    "icon": "🎓",
    "button_text": "Hocanı Bul",
    "display_order": 2,

    # Sonuç profilleri
    "profiles": [
        {
            "code": "TURGUT",
            "title": "Turgut Hoca",
            "icon": "📏",
            "description": "Trakya Üniversitesi’nde hoca olsaydın, Turgut hoca olurdun! Sende ders saati bir öneri değil, adeta bölüm anayasasının ilk maddesi gibidir; kapı açılmışsa açılmıştır, kapanmışsa da “ama trafik vardı” hikâyesi seni pek etkilemez. Yoklama kağıdında bir imza fazla ya da eksik gördüğünde olayın peşini bırakmaman, aslında kontrol manyaklığından çok “çalışanla çalışmayan aynı torbaya girmesin” refleksinden gelir. Geç teslim edilen ödeve sıcak yaklaşmazsın; çünkü senin gözünde tarih koyulduysa bir anlamı olmalıdır. Derste materyal verirsin ama öğrencinin de kafasını çalıştırıp hazırlıklı gelmesini beklersin; “her şeyi hazır önüne koyayım” anlayışı sana göre değildir. Sınavda yuvarlak cevaplar ve uydurma özgüven seni anında gerer; kağıdı okurken “ne yazdığı” kadar “nasıl düşündüğü”ne de bakarsın. Giyimde abartıdan uzak, tavırda net, küçük sohbette rekabet ve başarı diline yakınsın. Öğrenci sana gelebilir ama dürüst ve hazırlıklıysa; senin dersinin imzası korkuyla saygı arasındaki o ince çizgide duran disiplinli adalettir."
        },
        {
            "code": "AYDIN",
            "title": "Aydın Hoca",
            "icon": "📚",
            "description": "Trakya Üniversitesi’nde hoca olsaydın, Aydın hoca olurdun!  Sen tam anlamıyla klasik üniversite hocası enerjisi taşırsın: kuralları sever, düzeni önemser, ama bunu bağırıp çağırarak değil, hafif eski usul bir ciddiyetle yaparsın. Derse geç geleni ilk dakikada kapıdan çevirecek kadar keskin değilsindir; kısa bir toleransın vardır, yine de bu toleransı “nasıl olsa bir şey olmaz” rehavetine dönüştürenleri içten içe not edersin. Yoklama konusunda gevşek görünmezsin; imza ile sınıfın birbirini tutması gerektiğine dair içsel bir hassasiyetin vardır. Ödev işinde ise saatler ve tarihler bir anda kutsal metin seviyesine çıkar; geç gelen iş, ne kadar iyi olursa olsun senden kolay kolay merhamet görmez. Anlatım biçimin daha teorik, daha lineer ve daha klasik akar; slaytlar senin için sadece araç değil, dersin omurgasıdır. Sınav kağıdında öğrencinin ne bildiğini görmek istersin, ne uydurduğunu değil; bulanık cevaplar sende sabır değil, kaş çatma üretir. Giyimde sade ve düzenli çizgiyi korursun. Tavırda ölçülü, sohbette aile hayatı ya da gündelik yaşam üzerinden daha tanıdık bir ton kurarsın. Öğrenci sana gelebilir ama belli bir mesafeyi koruyarak; çünkü senin dersinde samimiyet vardır, laubalilik değil. Senin dersinin imzası, “yavaş ama köklü” hissi veren düzenli bir teorik akıştır."
        },
        {
            "code": "DENIZ",
            "title": "Deniz Hoca",
            "icon": "⚙️",
            "description": "Trakya Üniversitesi’nde hoca olsaydın, Deniz hoca olurdun! Senin enerjin sınıfa girer girmez “sert görünmeden otorite kurulabiliyormuş” hissi yaratır. Hani bazı hocalar vardır, sınıfa girince herkes susar ama bunun sebebi korku değil saygıdır, tam o enerji sende toplanır. Derse giren çıkan öğrenciyi dakika hesabıyla takip etmekten çok, dersin ritmine, sınıfın genel havasına, işin niteliğine ve öğrencinin gerçekten bir şey kapıp kapmadığına bakarsın. Yoklama ve imza gibi işler sende bürokratik savaş sebebi olmaz; biri makul bir dille konuşuyorsa çözüm ararsın, prosedürü kutsallaştırmazsın. Geç ödev konusunda da takvimden çok niyete ve emeğe bakarsın; öğrencinin tüm emeğini küçük bir gecikme yüzünden kaldırıp çöpe atmak sana verimsiz gelir.  Anlatım tarzında kuru bir okuma değil, deneyimle yoğrulmuş daha doğal bir akış vardır. Sınav kağıdında da “bu çocuk burada ne yapmaya çalışmış” diye bakar, tam puanı vermesen bile emeği kısmaktan hoşlanmazsın. Giyimde hafif resmiyet, tavırda sıcaklık, küçük sohbette teknik merak ve üretme hevesi vardır. Öğrenci sana yaklaşırken diken üstünde olmaz; senin dersinin imzası, ciddiyetini kaybetmeden destekleyici kalabilmendir."
        },
        {
            "code": "DERYA",
            "title": "Derya Hoca",
            "icon": "🌿",
            "description": "Trakya Üniversitesi’nde hoca olsaydın, Derya hoca olurdun! Senin hocallığın kurallardan tamamen kopuk değil ama her kuralı öğrencinin üstüne bir baskı aracı gibi koymayan, daha insani bir yerden çalışan bir enerji taşır. Derse giriş çıkış meselesini bir güvenlik kontrolüne çevirmediğin için öğrenciler senden çok “yaklaşılabilir” bir enerji alır. Yoklama, imza, küçük idari pürüzler sende dev bir meseleye dönüşmez; kuralların varlığını kabul eder ama onları öğrencinin başına sallanan sopa gibi kullanmazsın. Geç ödeve bakışın da benzer biçimde yumuşaktır; ortada gerçek bir çaba varsa keskin cezalar vermek sana anlamsız gelir. Anlatımında didaktik bir gösteriden çok, öğrenciyi rahatlatan bir ritim vardır; bazen tam da bu yüzden insanlar senden not kadar moral de alır. Sınav kağıdı okurken öğrenciyi gömmeye değil, ayakta tutmaya meyillisin; bir şeyler bilen öğrenciyi tamamen duvara toslatmak sana göre değildir. Giyimde günlük, tavırda sıcak, iletişimde çekincesizsin; saçma sorular karşısında bile sabrın kolay kolay tükenmez. Senin dersinin imzası, öğrenciye “yalnız değilsin” hissi vermesidir."
        },
        {
            "code": "FATMA",
            "title": "Fatma Hoca",
            "icon": "🧩",
            "description": "Trakya Üniversitesi’nde hoca olsaydın, Fatma hoca olurdun! Senin çizginde akademik hayat biraz netlik, biraz mesafe, biraz da “iş yapıyorsak doğru yapalım” ciddiyetiyle yürür. Sabahın köründe herkesi sıraya sokma merakın olmayabilir; ama bu, gevşek bir ders düzenin olduğu anlamına gelmez, çünkü sende saatten çok standart belirleyicidir. Yoklamada sayısal kusurlar seni rahatsız edebilir ama asıl derdin idari ayrıntının kendisinden çok, ciddiyetsizliğin derse sızmasıdır. Ödev konusunda fazladan duygusal yatırım yapan biri değilsindir; eksik kalan ya da savruk bırakılan iş sana göre öğrencinin kendi hesabıdır. Anlatım tarafında teorik omurgayı önemsersin; öğrencinin önüne bilgi koyarsın ama onu sindirip sindirmediğini de sınavda net biçimde görmek istersin. Değerlendirmende ise yüksek eşik vardır; kısmi doğrulara fazla alan tanımadığın için sınav kağıdında puan kazanmak da kolay değildir. Giyimde rahat ama karakterli bir çizgi, tavırda mesafe, küçük sohbette ise gereksiz dağılmayı sevmeyen bir seçicilik hissedilir. Gereksiz ya da hazırlıksız sorular karşısında sabrın çabuk tükenebilir. Senin dersinin imzası, tavizsiz netlik ve yüksek eşiktir; dersinden geçen öğrenci de bunun farkında olarak geçer."
        },
        {
            "code": "OZLEM",
            "title": "Özlem Hoca",
            "icon": "✨",
            "description": "Trakya Üniversitesi’nde hoca olsaydın, Özlem hocaolurdun! Senin sınıfa girişin yalnızca ders başlatmak değil, ortamın seviyesini ayarlamak gibidir; daha ilk dakikada düzen, özen ve belli bir profesyonellik hissi kurarsın. Sabahın köründe sırf program öyle yazıyor diye herkesin yarı uykulu sürünmesini çok anlamlı bulmaz, işin gerçekten verimli akacağı düzeni yaratmayı daha mantıklı görürsün. Yoklama ve imza gibi ayrıntılar sende dersin merkezine oturmaz; senin asıl derdin, sınıfın ritmi ve anlatının akışıdır. Anlatırken ezberden okunan bir ders tonu değil, kendi yorumunu ve kontrolünü taşıyan daha özgün bir akış kurarsın. Sınav ve değerlendirme tarafında özensizliği kolay tolere etmezsin; hazırlıksız gelen öğrenci bunu çoğu zaman senden söz duymadan da hisseder. Giyimde özenli, tavırda seçici, küçük muhabbette güncel dünya, mesleki dönüşüm ve sektör gündemine yakınsın. Öğrenci sana yaklaşabilir ama cümlesini toparlayarak gelirse daha rahat eder; çünkü senin dersinin imzası, şıklıkla ciddiyetin aynı masada oturabilmesidir."
        },
        {
            "code": "EMIR",
            "title": "Emir Hoca",
            "icon": "💻",
            "description": "Trakya Üniversitesi’nde hoca olsaydın, Emir hoca olurdun! Sende en dikkat çekici şey, üniversite hocası olmanın iki klişesine de tam düşmemen: ne gereksiz sertliğe yaslanırsın ne de “aman çocuklar üzülmesin” diye çizgiyi silersin. Dersinde de tavrında da güçlü bir denge hissedilir. Öğrencinin gözünde “rahat ama boş vermiş değil, ciddi ama kasıntı hiç değil” diye tarif edilen hoca tam olarak sensin. Derse giriş çıkış meselesini bir otorite gösterisine dönüştürmez, yoklama ve imza işinde şekilden çok mantığa bakarsın. Geç ödev konusunda kapıyı tamamen kapatmazsın ama bu da “ne zaman istersen at” rahatlığına dönüşmez; makul gerekçe, emek ve ciddiyet beklersin. Ders anlatırken canlı, uygulamalı ve üretken bir yol seçersin; kuru teoriyi ekrana, örneğe, uygulamaya ve mümkünse projeye bağlama refleksin güçlüdür; öğrenci senden yalnızca konu değil, iş yapma biçimi de öğrenir. Sınav kağıdında ne acımasız kıtlık ne de dağıtılan merhamet vardır; ne yaptıysa onu alır mantığıyla ilerlersin. Giyimde sade, iletişimde mütevazı, sohbette güncel teknoloji ve sektör dili öne çıkar. Acemice sorulara bile egoyla değil, ölçülü bir sabırla yaklaşman sayesinde senin dersinin imzası, proje odaklı öğrenme ve güven veren dengedir."
        },
    ],

    "questions": [
        {
            "text": "Sabah 08:30 dersi için sınıfa giriş politikan nedir?",
            "is_tiebreaker": True,
            "tiebreaker_order": 1,
            "options": [
                {
                    "key": "A",
                    "text": "Kapı saniyeler içinde kapanır. 1 dakika geç kalanı bile içeri almam, disiplin her şeydir.",
                    "scores": {"TURGUT": 3}
                },
                {
                    "key": "B",
                    "text": "10-15 dakika opsiyon tanırım. Geç gelenlere tamam hadi hadi geçin derim.",
                    "scores": {"AYDIN": 3}
                },
                {
                    "key": "C",
                    "text": "Derse kimin girip çıktığıyla ilgilenmem, ben dersimi anlatırım.",
                    "scores": {"EMIR": 2, "DERYA": 2, "DENIZ": 2}
                },
                {
                    "key": "D",
                    "text": "8:30 dersi ne ya? Onu ilk gün 10:00 dersi yapmışımdır zaten.",
                    "scores": {"OZLEM": 2, "FATMA": 2}
                },
            ],
        },
        {
            "text": "Yoklamada imza sayısı ile sınıftaki kişi sayısı tutmuyor. Ne yaparsın?",
            "is_tiebreaker": True,
            "tiebreaker_order": 2,
            "options": [
                {
                    "key": "A",
                    "text": "İsimleri tek tek okurum, bir hata varsa asla affetmem.",
                    "scores": {"TURGUT": 2, "AYDIN": 2}
                },
                {
                    "key": "B",
                    "text": "Saymam ama tutarsızlık hissedersem öğrencilere laf söyler geçerim.",
                    "scores": {"FATMA": 3}
                },
                {
                    "key": "C",
                    "text": "Hocam siler misiniz diyene mail at halledelim derim, umrumda olmaz.",
                    "scores": {"DENIZ": 2, "DERYA": 2}
                },
                {
                    "key": "D",
                    "text": "İmza sayısını neden sayayım ki bence bunlar gereksiz şeyler.",
                    "scores": {"EMIR": 2, "DERYA": 1, "DENIZ": 1}
                },
            ],
        },
        {
            "text": "Ödev 1 gün geç atılmış olsun. Puanlaman nasıl olur?",
            "options": [
                {
                    "key": "A",
                    "text": "Asla tolerans göstermem, direkt 0 veririm.",
                    "scores": {"AYDIN": 2, "TURGUT": 2}
                },
                {
                    "key": "B",
                    "text": "Ödev teslimi nedir? Bir de ödev okumakla mı uğraşacağız?",
                    "scores": {"FATMA": 3}
                },
                {
                    "key": "C",
                    "text": "Vaktinden geç gelse de kabul ederim, puan da kırmam.",
                    "scores": {"DERYA": 2, "DENIZ": 2}
                },
                {
                    "key": "D",
                    "text": "Çok çok çok geçerli bir sebebi varsa kabul ederim.",
                    "scores": {"EMIR": 3}
                },
            ],
        },
        {
            "text": "Ders anlatırken hangi yöntemi tercih edersin?",
            "options": [
                {
                    "key": "A",
                    "text": "Slaytları paylaşırım ama slaytlarda her şey yoktur, öğrencinin hazırlanıp gelmesini isterim.",
                    "scores": {"TURGUT": 3}
                },
                {
                    "key": "B",
                    "text": "Derste en sevdiğim aktivitelerden biri slayt okumaktır.",
                    "scores": {"AYDIN": 2, "FATMA": 2}
                },
                {
                    "key": "C",
                    "text": "Slayttan okumam; kendim anlatırım ya da doğal bir akışta ilerlerim.",
                    "scores": {"OZLEM": 2, "DENIZ": 2}
                },
                {
                    "key": "D",
                    "text": "Bilgisayarı açarım; kodu yazarken aynı anda anlatırım, slayt okumam.",
                    "scores": {"EMIR": 3}
                },
            ],
        },
        {
            "text": "Sınav kağıtlarını okurken nasıl bir tavır sergilersin?",
            "is_tiebreaker": True,
            "tiebreaker_order": 3,
            "options": [
                {
                    "key": "A",
                    "text": "Sallama bilgilere asla puan vermem, hatta sallıyorsa diğer sorularını da olumsuz etkilerim.",
                    "scores": {"TURGUT": 2, "AYDIN": 2}
                },
                {
                    "key": "B",
                    "text": "Tam ve doğru çözmediysen neredeyse 0 puan alırsın, gidiş yoluna bakmam.",
                    "scores": {"FATMA": 3}
                },
                {
                    "key": "C",
                    "text": "Eli çok bol biriyimdir, öğrenci geçsin diye uğraşırım; sınav anında ipucu bile veririm.",
                    "scores": {"DENIZ": 2, "DERYA": 2}
                },
                {
                    "key": "D",
                    "text": "Öğrenci yaptığı kadarına puan alır. Ne kıt puanlıyım ne de öğrenci geçsin diye uğraşırım.",
                    "scores": {"EMIR": 3}
                },
            ],
        },
        {
            "text": "Okula gelirken giyim tarzın nasıl olurdu?",
            "options": [
                {
                    "key": "A",
                    "text": "Takım elbise kravat tabii ki, başka ne ile geleceğim?",
                    "scores": {"DENIZ": 3}
                },
                {
                    "key": "B",
                    "text": "Günlük kıyafetler giyerim. Podyuma çıkmıyoruz sonuçta.",
                    "scores": {"EMIR": 1, "TURGUT": 1, "AYDIN": 1, "DERYA": 1}
                },
                {
                    "key": "C",
                    "text": "Rahat edeceğim, çoğu zaman boğazlı kıyafetler veya fular tercih ederim.",
                    "scores": {"FATMA": 3}
                },
                {
                    "key": "D",
                    "text": "Her derse topuklu ayakkabı ve özenli kombinlerle gelirim; look her şeydir.",
                    "scores": {"OZLEM": 3}
                },
            ],
        },
        {
            "text": "Derste hafif sohbet havasına girildiğinde nelerden konuşmayı seversin?",
            "options": [
                {
                    "key": "A",
                    "text": "Galatasarayın başarılarından ve Fenerlilerin gün yüzü görmeyişinden.",
                    "scores": {"TURGUT": 3}
                },
                {
                    "key": "B",
                    "text": "Hanımcıyımdır, hanımımdan ve ailevi konulardan bahsederim.",
                    "scores": {"AYDIN": 3}
                },
                {
                    "key": "C",
                    "text": "Donanım, mucitlik hikayeleri veya çocuklarımdan bahsetmeyi severim.",
                    "scores": {"DENIZ": 3}
                },
                {
                    "key": "D",
                    "text": "Güncel teknoloji, sektördeki yenilikler veya kadınların sektördeki yerinden bahsederim.",
                    "scores": {"OZLEM": 2, "EMIR": 2}
                },
            ],
        },
        {
            "text": "Bir öğrenci seninle herhangi bir konuda iletişime geçeceğinde sana nasıl yaklaşmalıdır?",
            "options": [
                {
                    "key": "A",
                    "text": "Saygılı ve mesafeli olmalı, odama girmeye bile çekinmeli.",
                    "scores": {"FATMA": 3}
                },
                {
                    "key": "B",
                    "text": "Disiplinli olduğumu bilmeli ama dürüstçe gelip şikayetini de söyleyebilmeli.",
                    "scores": {"TURGUT": 3}
                },
                {
                    "key": "C",
                    "text": "Hiç çekinmemeli; ben zaten o selam vermeden selamımı verecek bir hocayım.",
                    "scores": {"DENIZ": 2, "DERYA": 2}
                },
                {
                    "key": "D",
                    "text": "Kral hoca diyerek güvenle yaklaşabilir; mütevazı ve ego yapmayan biriyim.",
                    "scores": {"EMIR": 3}
                },
            ],
        },
        {
            "text": "Bir öğrencinin gereksiz veya iş bilmez sorularına tepkin nedir?",
            "options": [
                {
                    "key": "A",
                    "text": "Ters birine dönüşürüm, ciddi ve havalı duruşumu bozarım.",
                    "scores": {"OZLEM": 2, "FATMA": 2}
                },
                {
                    "key": "B",
                    "text": "Hazırlıklı gelmemişsin diye kızarım, sorumsuzluktan hiç hoşlanmam.",
                    "scores": {"TURGUT": 3}
                },
                {
                    "key": "C",
                    "text": "Anaç bir tavırla açıklarım. Öğrenci anlamasa bile anlatmaya devam ederim.",
                    "scores": {"DERYA": 3}
                },
                {
                    "key": "D",
                    "text": "İçimden bu da sorulmaz derim ama bunu belli etmeden cevaplarım.",
                    "scores": {"EMIR": 3}
                },
            ],
        },
        {
            "text": "Senin dersinin olmazsa olmaz imzası nedir?",
            "is_tiebreaker": True,
            "tiebreaker_order": 4,
            "options": [
                {
                    "key": "A",
                    "text": "Derse hazırlıklı gelinmesi ve adaletli bir ortam.",
                    "scores": {"TURGUT": 3}
                },
                {
                    "key": "B",
                    "text": "Uzun bir teorik anlatım süreci.",
                    "scores": {"AYDIN": 3}
                },
                {
                    "key": "C",
                    "text": "Öğrencinin bir şekilde desteklenerek dersi geçmesi.",
                    "scores": {"DERYA": 2, "DENIZ": 2}
                },
                {
                    "key": "D",
                    "text": "Her derste öğrencinin mutlaka bir proje süreci deneyimlemesi.",
                    "scores": {"EMIR": 3}
                },
            ],
        },
    ],
}