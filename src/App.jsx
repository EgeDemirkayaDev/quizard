import React from 'react';

function App({ onNavigate }) {
  const quizzes = [
    { id: 1, title: 'Kişilik Testi', desc: 'Gizemli derinliklerini keşfet.', btn: 'Yoluna Başla', icon: '🔮' },
    { id: 2, title: 'Bölümde Hangi Hocasın?', desc: 'Akademik bilgeliğini ölç.', btn: 'Hocanı Bul', icon: '❓' },
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
            <div className="quiz-grid">
              {quizzes.map(q => (
                <div key={q.id} className="quiz-card">
                  <div className="card-icon">{q.icon}</div>
                  <div className="card-info">
                    <h3>{q.title}</h3>
                    <p>{q.desc}</p>
                    {/* 👇 İŞTE EKSİK OLAN SİHİR BURASI: Tıklayınca quiz sayfasına yönlendiriyor 👇 */}
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