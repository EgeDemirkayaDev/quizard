import React from 'react';

function Signup({ onNavigate }) {
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
        <div className="login-card">
          <h2>Yeni Büyücü Kaydı 📜</h2>
          <p className="login-subtitle">Güçlerini keşfetmek için aramıza katıl!</p>
          <form className="login-form">
            <div className="input-group"><label>E-Posta</label><input type="email" placeholder="baykus@hogwarts.com" /></div>
            <div className="input-group"><label>Kullanıcı Adı</label><input type="text" placeholder="GryffindorAslani" /></div>
            <div className="input-group"><label>Şifre</label><input type="password" placeholder="En az 8 karakter..." /></div>
            
            {/* 👇 İŞTE DEĞİŞEN KISIM BURASI: Artık 'dashboard' sayfasına gidiyor 👇 */}
            <button type="button" className="signup-action-btn" onClick={() => onNavigate('dashboard')}>
              Kaydı Tamamla
            </button>
            
            <div className="login-footer">
              <p>Zaten üye misin? <a href="#" onClick={(e) => { e.preventDefault(); onNavigate('login'); }}>Giriş Yap</a></p>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Signup;