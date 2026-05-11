import React, { useState, useEffect } from 'react';

function App({ onNavigate }) {
  // 1. URL'den gelen özel ismi tutacağımız state
  const [ozelIsim, setOzelIsim] = useState("");

  // 2. Sayfa yüklendiğinde linkin sonundaki "?kime=isim" kısmını yakalama
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const isim = params.get('kime'); 
    if (isim) {
      // İlk harfi büyütüp state'e kaydediyoruz
      const formatliIsim = isim.charAt(0).toUpperCase() + isim.slice(1);
      setOzelIsim(formatliIsim);
    }
  }, []);

  const quizzes = [
    { id: 2, title: 'Kişilik Testi', desc: 'Gizemli derinliklerini keşfet.', btn: 'Yoluna Başla', icon: '🔮' },
    { id: 1, title: 'Bölümde Hangi Hocasın?', desc: 'Akademik bilgeliğini ölç.', btn: 'Hocanı Bul', icon: '❓' },
    { id: 3, title: 'Yazılım Alanın Ne?', desc: 'Sihirli kodlama yolunu seç.', btn: 'Kodla', icon: '🪄' },
    { id: 4, title: 'Hangi Hayvansın?', desc: 'Ruh hayvanınla tanış.', btn: 'Keşfet', icon: '🦉' }
  ];

  return (
    <div className="main-wrapper">
      <header className="wizard-header">
        <div className="logo">🧙‍♂️ quizard ✨</div>
        <nav>
          <a href="#" onClick={(e) => { e.preventDefault(); onNavigate('home'); }}>Anasayfa</a>
          <a href="#" onClick={(e) => { e.preventDefault(); onNavigate('about'); }}>Hakkımızda</a>
        </nav>
        <button onClick={() => onNavigate('login')} className="login-btn">Giriş Yap</button>
      </header>

      <div className="center-content">
        <div className="wizard-container">
          <main className="main-content">
            
            {/* 👇 DİNAMİK KARŞILAMA MESAJI BURADA 👇 */}
            <div className="welcome-banner" style={{ textAlign: 'center', marginBottom: '2rem' }}>
              <h2>
                {ozelIsim ? `Hoş geldin ${ozelIsim}! Seçilmiş kişi sen misin? ⚡` : "Hoş geldin Büyücü! Sihirli yolculuğuna başla. ⚡"}
              </h2>
            </div>

            <div className="quiz-grid">
              {quizzes.map(q => (
                <div key={q.id} className="quiz-card">
                  <div className="card-icon">{q.icon}</div>
                  <div className="card-info">
                    <h3>{q.title}</h3>
                    <p>{q.desc}</p>
                    <button className="card-btn" onClick={() => onNavigate('quiz', q.id)}>{q.btn}</button>
                  </div>
                </div>
              ))}
            </div>

            <aside className="right-sidebar">
              <h2>Topluluğa Katıl</h2>
              <p className="sidebar-subtitle">İlerlemeni takip etmek için aramıza katıl!</p>
              <button onClick={() => onNavigate('signup')} className="signup-action-btn">Üye Ol</button>
              <p className="copyright">© 2026 Quizard</p>
            </aside>
          </main>
        </div>
      </div>
    </div>
  );
}

export default App;