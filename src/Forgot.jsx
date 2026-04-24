import React from 'react';

function Forgot({ onNavigate }) {
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
          <h2>Şifremi Unuttum 🦉</h2>
          <p className="login-subtitle">Baykuşlarımız sana yeni bir parola getirecek.</p>
          <form className="login-form">
            <div className="input-group">
              <label>Kayıtlı E-Posta Adresin</label>
              <input type="email" placeholder="baykus@hogwarts.com" />
            </div>
            <button type="button" className="signup-action-btn">Sıfırlama Linki Gönder</button>
            <div className="login-footer">
              <p>Hatırladın mı? <a href="#" onClick={(e) => { e.preventDefault(); onNavigate('login'); }}>Geri Dön</a></p>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Forgot;