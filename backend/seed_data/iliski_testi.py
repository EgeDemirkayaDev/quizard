# =========================================================
# İLİŞKİDE NASIL BİRİSİN TESTİ
# =========================================================
#
# Bu dosya:
# - test bilgilerini
# - sonuç profillerini
# - soruları
# - seçenekleri
# - puan algoritmasını
#
# içerir.
#
# Her seçenek belirli bir profile puan verir.
# Backend tarafında sonuç hesaplanırken bu puanlar toplanır.
# =========================================================


ILISKI_TESTI = {
    "slug": "iliskide-nasil-birisin",

    # Testin ana başlığı
    "title": "İlişkide Nasıl Birisin?",

    # Kart üzerinde gözükecek kısa başlık
    "short_title": "İlişkide Nasıl Birisin?",

    # Kart açıklaması
    "description": "İlişkilerdeki davranış tarzını ve duygusal reflekslerini keşfet.",

    # Kart kategorisi
    "category": "İlişki",

    # Kart ikonu
    "icon": "💘",

    # Kart buton yazısı
    "button_text": "Teste Başla",

    # Ana sayfadaki sırası
    "display_order": 4,

    # =====================================================
    # SONUÇ PROFİLLERİ
    # =====================================================

    "profiles": [

        {
            "code": "GOLDEN_RETRIEVER",

            "title": "Golden Retriever",

            "icon": "🐶",

            "description":
                "Sen ilişkinin duygusal taşıyıcısısın. İnsanlar senin yanında sevildiğini, önemsendiğini ve güvende olduğunu hissediyor. Sadakat ve şefkat senin için her şeyden önemli. Partnerinin mutluluğu seni de mutlu ediyor ve sorunları her zaman tatlı dille, empati kurarak çözmekten yanasın. Kötü günlerde sığınılacak güvenli bir limansın ancak bazen karşındakini mutlu etmek adına kendi ihtiyaçlarını göz ardı edip gereğinden fazla fedakarlık yapma eğiliminde olabilirsin. Kalbinin kırılmaması için kendi sınırlarını da korumayı öğrenmelisin."
        },

        {
            "code": "DOMINANT",

            "title": "Dominant",

            "icon": "🛡️",

            "description":
                "Sen ilişkide koruyucu, güçlü ve sahiplenen taraftasın. Partnerin yanında kendini asla yalnız veya savunmasız hissetmez çünkü kontrolü eline alan, sorunları çözen ve kriz anlarını yöneten kişi çoğunlukla sensin. Saygı, güven ve dürüstlük senin kırmızı çizgilerin. Sevdiklerine karşı aşırı korumacı bir yapın var. Ancak bu yoğun sahiplenici tavrın bazen karşı taraf için boğucu bir hal alabilir. Kontrolü bazen biraz esnetmek ve partnerine kendi kişisel alanını tanımak, ilişkinizin çok daha dengeli ve sağlıklı ilerlemesini sağlayacaktır."
        },

        {
            "code": "MANIPULATIF_KARIZMA",

            "title": "Manipülatif Karizma",

            "icon": "🧠",

            "description":
                "Sen ilişkiyi sadece duyguyla değil, zeka, strateji ve psikolojiyle yaşayan taraftasın. İnsanların zaaflarını çok hızlı okur, davranışların altındaki gerçek sebepleri şıp diye anlarsın. Tutku ve zihinsel çekim senin için fiziksel özellikler kadar vazgeçilmezdir. İnsanları analiz etmek senin için adeta gizli bir hobidir. Karşı konulmaz, çekici ve gizemli auran sayesinde partnerin üzerinde unutulması zor bir etki bırakırsın. Fakat güç savaşlarına ve her şeyi kontrol etme isteğine olan düşkünlüğünün, ilişkinizdeki şeffaflığı ve samimiyeti zedelemesine izin vermemelisin."
        },

        {
            "code": "GHOSTLAYAN_KAOTIK_RUH",

            "title": "Ghostlayan Kaotik Ruh",

            "icon": "🌪️",

            "description":
                """Sen sevgiyi oldukça yoğun yaşayabilen ama aynı anda özgürlüğüne en çok düşkün olan taraftasın. Bağımsızlığının kısıtlandığını hissettiğin, hesap vermek zorunda bırakıldığın an hızla kendi kabuğuna çekilir veya sessizce uzaklaşırsın. İlişkide durağanlıktan, rutinleşmekten hiç hoşlanmaz, anı yaşamanın getirdiği heyecanı seversin. Partnerin için çoğu zaman çözülmesi zor bir bulmaca gibisin; bir an çok sıcak ve ilgiliyken, ertesi gün kendi dünyana kapanıp buz kesebilirsin. Bu gizemli ve öngörülemez yapın seni çok çekici yapsa da, karşındakini kaybetmemek ve ona güven vermek için iletişim kurmaktan kaçmamalısın."""
        },
    ],

    # =====================================================
    # SORULAR
    # =====================================================

    "questions": [

        # -------------------------------------------------
        # SORU 1
        # -------------------------------------------------

        {
            "text":
                "Partnerin “konuşmamız lazım” yazdı. İlk tepkin?",

            "options": [

                {
                    "key": "A",

                    "text":
                        "“Ne oldu aşkım?” diye direkt ararım.",

                    # Bu seçenek Golden Retriever profiline 1 puan verir.
                    "scores": {
                        "GOLDEN_RETRIEVER": 1
                    }
                },

                {
                    "key": "B",

                    "text":
                        "“Kim canını sıktı?” diye savunma moduna geçerim.",

                    "scores": {
                        "DOMINANT": 1
                    }
                },

                {
                    "key": "C",

                    "text":
                        "Önce eski konuşmaları okuyup olay analizi yaparım.",

                    "scores": {
                        "MANIPULATIF_KARIZMA": 1
                    }
                },

                {
                    "key": "D",

                    "text":
                        "Bildirimi görüp psikolojik hazırlık yaparım.",

                    "scores": {
                        "GHOSTLAYAN_KAOTIK_RUH": 1
                    }
                },
            ],
        },

        # -------------------------------------------------
        # SORU 2
        # -------------------------------------------------

        {
            "text":
                "İlişkide seni en çok ne sinirlendirir?",

            "options": [

                {
                    "key": "A",

                    "text":
                        "Soğuk davranılması.",

                    "scores": {
                        "GOLDEN_RETRIEVER": 1
                    }
                },

                {
                    "key": "B",

                    "text":
                        "Saygısızlık edilmesi.",

                    "scores": {
                        "DOMINANT": 1
                    }
                },

                {
                    "key": "C",

                    "text":
                        "Manipüle edilmeye çalışılmak.",

                    "scores": {
                        "MANIPULATIF_KARIZMA": 1
                    }
                },

                {
                    "key": "D",

                    "text":
                        "Sürekli hesap verilmesinin beklenmesi.",

                    "scores": {
                        "GHOSTLAYAN_KAOTIK_RUH": 1
                    }
                },
            ],
        },
                {
            "text": "Partnerin “biraz yalnız kalmak istiyorum” dediğinde?",
            "options": [
                {"key": "A", "text": "Destek olurum ama içim hafif kırılır.", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "“Bir sorun mu var?” diye sorgularım.", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "Bunun altında başka bir anlam ararım.", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "“Tamamdır görüşürüz” deyip kendi dünyama dönerim.", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
        {
            "text": "İlişkideki tartışma stilin hangisi?",
            "is_tiebreaker": True,
            "tiebreaker_order": 5,
            "options": [
                {"key": "A", "text": "Konuşup çözmeye çalışırım.", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "Ses tonum sertleşebilir ama korumacı davranırım.", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "Karşı tarafın açıklarını unutmayıp zamanı gelince kullanırım.", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "Ortadan kaybolurum.", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
        {
            "text": "Partnerin story’sine biri fazla samimi yorum attı.",
            "options": [
                {"key": "A", "text": "İçten içe kıskansam da düzgünce konuşurum.", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "O yorumu atan kişinin soy ağacını araştırırım.", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "Hiçbir şey demeyip davranış değiştiririm.", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "“Banane ya” derim ama gece düşünürüm.", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
        {
            "text": "İlk buluşmada seni en çok etkileyen şey?",
            "options": [
                {"key": "A", "text": "Samimiyet ve sıcaklık.", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "Güçlü duruş ve özgüven.", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "Zeka ve gizemli aura.", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "Rahat hissettirmesi ve kasmaması.", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
        {
            "text": "Partnerin moral olarak çökmüş durumda. Ne yaparsın?",
            "options": [
                {"key": "A", "text": "Saatlerce yanında olurum.", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "Sorunu çözmek için aksiyon alırım.", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "Gerçek problemin ne olduğunu çözmeye çalışırım.", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "Alan tanıyıp hazır olunca konuşurum.", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
        {
            "text": "Aşk hayatındaki en büyük problemin?",
            "is_tiebreaker": True,
            "tiebreaker_order": 4,
            "options": [
                {"key": "A", "text": "Fazla bağlanmak.", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "Fazla sahiplenmek.", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "Güven problemleri ve güç oyunları.", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "Bir süre sonra bunalmam.", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
        {
            "text": "İlişkide romantizm anlayışın?",
            "options": [
                {"key": "A", "text": "Küçük detaylarla mutlu etmek.", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "Partnerimi güvende hissettirmek.", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "Akılda kalacak psikolojik etki bırakmak.", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "Plansız spontane anlar yaşamak.", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
        {
            "text": "Partnerin eski sevgilisini stalkladığını öğrendin.",
            "options": [
                {"key": "A", "text": "Hafif üzülürüm ama konuşurum.", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "Direkt nedenini sorarım.", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "Ben de stalklayıp veri toplarım.", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "“İnsan merak eder ya” deyip geçerim.", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
        {
            "text": "İlişkide hangi cümle sana daha yakın?",
            "is_tiebreaker": True,
            "tiebreaker_order": 3,
            "options": [
                {"key": "A", "text": "“Biz olalım yeter.”", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "“Ben varken sana bir şey olmaz.”", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "“İnsanları çözmek zor ama keyifli.”", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "“Beni çok sıkıştırmayın.”", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
        {
            "text": "Partnerin seni kıskandığını söylediğinde?",
            "options": [
                {"key": "A", "text": "Tatlı bulurum.", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "Normal karşılarım çünkü ben de kıskanırım.", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "Güç dengesi değişiyor mu diye düşünürüm.", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "Hafif geri çekilirim.", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
        {
            "text": "Bir ilişkide en önemli şey?",
            "is_tiebreaker": True,
            "tiebreaker_order": 2,
            "options": [
                {"key": "A", "text": "Sadakat.", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "Güven ve saygı.", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "Tutku ve zihinsel çekim.", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "Alan ve özgürlük.", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
        {
            "text": "Ayrılık sonrası halin nasıl olur?",
            "options": [
                {"key": "A", "text": "Özlerim ama güzel anıları hatırlarım.", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "Kolay kolay belli etmem.", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "Sessizce stalk master’a dönüşürüm.", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "Bir anda yeni bir hayata başlamaya çalışırım.", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
        {
            "text": "Partnerin seni tek kelimeyle nasıl tanımlar?",
            "is_tiebreaker": True,
            "tiebreaker_order": 1,
            "options": [
                {"key": "A", "text": "“Huzur.”", "scores": {"GOLDEN_RETRIEVER": 1}},
                {"key": "B", "text": "“Güçlü.”", "scores": {"DOMINANT": 1}},
                {"key": "C", "text": "“Tehlikeli derecede çekici.”", "scores": {"MANIPULATIF_KARIZMA": 1}},
                {"key": "D", "text": "“Çözmesi imkansız.”", "scores": {"GHOSTLAYAN_KAOTIK_RUH": 1}},
            ],
        },
    ],
}