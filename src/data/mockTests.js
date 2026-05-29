export const mockTests = [
  {
    id: 1,
    slug: "zihninin-derinliklerinde",
    title: "Zihninin Derinliklerinde Hangi Kişilik Yatıyor?",
    shortTitle: "Zihninin Derinliklerinde",
    description: "DYE-15 ile içsel yönelimlerini keşfet.",
    category: "Kişilik",
    icon: "🔮",
    buttonText: "Kendini Keşfet",
    order: 1
  },
  {
    id: 2,
    slug: "tu-hangi-hoca",
    title: "TÜ’de Hangi Hoca Olurdun?",
    shortTitle: "TÜ’de Hangi Hoca Olurdun?",
    description: "Trakya Üniversitesi ruhunu test et.",
    category: "Eğlence",
    icon: "🎓",
    buttonText: "Hocanı Bul",
    order: 2
  },
  {
    id: 3,
    slug: "bilgisayar-muhendisligi-alani",
    title: "Bilgisayar Mühendisliğinde Hangi Alana Yönelmelisin?",
    shortTitle: "Hangi Alana Yönelmelisin?",
    description: "Yazılım dünyasındaki doğal yönünü öğren.",
    category: "Kariyer",
    icon: "💻",
    buttonText: "Alanını Bul",
    order: 3
  },
  {
    id: 4,
    slug: "iliskide-nasil-birisin",
    title: "İlişkide Nasıl Birisin?",
    shortTitle: "İlişkide Nasıl Birisin?",
    description: "İlişkilerdeki davranış tarzını keşfet.",
    category: "İlişki",
    icon: "💘",
    buttonText: "Teste Başla",
    order: 4
  }
];

export const mockTestDetails = {
  1: {
    id: 1,
    title: "Zihninin Derinliklerinde Hangi Kişilik Yatıyor?",
    icon: "🔮",
    description: "Derin Yansıma Envanteri DYE-15",
    questions: [
      {
        id: 101,
        text: "Uzun zamandır planladığınız bir şey son anda iptal oluyor. İlk tepkiniz genellikle ne olur?",
        options: [
          { id: 1001, text: "Yeni bir alternatif üretmeye çalışırım." },
          { id: 1002, text: "İçten içe hayal kırıklığı yaşarım ama belli etmem." },
          { id: 1003, text: "Neden böyle hissettiğimi düşünmeye başlarım." },
          { id: 1004, text: "Durumu kontrol edememek beni huzursuz eder." }
        ]
      }
    ]
  },
  2: {
    id: 2,
    title: "TÜ’de Hangi Hoca Olurdun?",
    icon: "🎓",
    description: "Trakya Üniversitesi Bilgisayar Mühendisliği hoca testi",
    questions: [
      {
        id: 201,
        text: "Sabah 08:30 dersi için sınıfa giriş politikan nedir?",
        options: [
          { id: 2001, text: "Kapı saniyeler içinde kapanır. 1 dakika geç kalanı bile içeri almam." },
          { id: 2002, text: "10-15 dakika opsiyon tanırım." },
          { id: 2003, text: "Derse kimin girip çıktığıyla ilgilenmem." },
          { id: 2004, text: "8:30 dersi ne ya? Onu ilk gün 10:00 yapmışımdır." }
        ]
      }
    ]
  },
  3: {
    id: 3,
    title: "Bilgisayar Mühendisliğinde Hangi Alana Yönelmelisin?",
    icon: "💻",
    description: "Yazılım alanı yönelim testi",
    questions: [
      {
        id: 301,
        text: "Bir çalışma masasında sizi en çok ne mutlu eder?",
        options: [
          { id: 3001, text: "Bol verili büyük ekranlar." },
          { id: 3002, text: "Tamamen kişisel ve izole bir çalışma alanı." },
          { id: 3003, text: "Fonksiyonel ve tıkır tıkır işleyen düzen." },
          { id: 3004, text: "Estetik detaylarla dolu bir masa." }
        ]
      }
    ]
  },
  4: {
    id: 4,
    title: "İlişkide Nasıl Birisin?",
    icon: "💘",
    description: "İlişki tarzı testi",
    questions: [
      {
        id: 401,
        text: "İlişkide seni en iyi anlatan davranış hangisi?",
        options: [
          { id: 4001, text: "Duygularımı açıkça gösteririm." },
          { id: 4002, text: "Güven ve sadakat benim için en önemlisidir." },
          { id: 4003, text: "Alanıma ve özgürlüğüme önem veririm." },
          { id: 4004, text: "Romantik ve ilgili bir yapım vardır." }
        ]
      }
    ]
  }
};

export const mockResult = {
  resultTitle: "Sonucun Hazır!",
  resultDescription: "Backend bağlandığında bu sonuç gerçek algoritmaya göre hesaplanacak.",
  scores: {}
};