import React, { useState } from 'react';

function Login({ onNavigate }) {
  const [showPassword, setShowPassword] = useState(false);

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
          <h2>Büyücü Girişi 🔮</h2>
          <p className="login-subtitle">Sihirli dünyana geri dön!</p>
          <form className="login-form">
            <div className="input-group">
              <label>Kullanıcı Adı</label>
              <input type="text" placeholder="Büyücü adını gir..." />
            </div>
            <div className="input-group">
              <label>Şifre</label>
              <div className="input-with-icon">
                <input type={showPassword ? "text" : "password"} placeholder="Gizli parolanı gir..." />
                <button type="button" className="eye-btn" onClick={() => setShowPassword(!showPassword)}>
                  {showPassword ? "👁️‍🗨️" : "👁️"}
                </button>
              </div>
            </div>
            
            {/* 👇 İŞTE DEĞİŞEN KISIM BURASI: Artık 'dashboard' sayfasına gidiyor 👇 */}
            <button type="button" className="signup-action-btn" onClick={() => onNavigate('dashboard')}>
              Giriş Yap
            </button>
            
            <div className="login-footer">
              <p style={{marginBottom: '10px'}}>
                <a href="#" onClick={(e) => { e.preventDefault(); onNavigate('forgot'); }}>Şifremi Unuttum?</a>
              </p>
              <p>Hesabın yok mu? <a href="#" onClick={(e) => { e.preventDefault(); onNavigate('signup'); }}>Kayıt Ol</a></p>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;