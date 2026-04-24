import React from 'react';

function About({ onNavigate }) {
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
        <div className="about-container">
          <h1 className="about-title">Quizard'ın Sırrı 🔮</h1>
          
          <div className="about-section">
            <h2>Vizyonumuz 🌟</h2>
            <p>Bilginin sadece sıkıcı ders kitaplarında değil, sihirli bir keşif yolculuğunda olduğuna inanıyoruz. Her kullanıcının içindeki potansiyeli, eğlenceli ve gizemli testlerle gün yüzüne çıkarmayı hedefliyoruz.</p>
          </div>

          <div className="about-section">
            <h2>Misyonumuz 🪄</h2>
            <p>Karmaşık algoritmalardan kişilik analizlerine kadar her konuyu, büyücülerin dünyasından birer parça haline getirerek sunmak. Dijital dünyada eğlenirken öğreten en büyük "Büyücülük Akademisi" olmak için çalışıyoruz.</p>
          </div>

          <div className="about-section">
            <h2>Testler Nasıl Oluşuyor? 📜</h2>
            <p>Testlerimiz, akademik veriler ile antik büyücü bilgeliğinin birleşimiyle hazırlanıyor. Sorularımız, senin verdiğin her cevapla aslında senin dijital auranı analiz ediyor.</p>
          </div>

          <button onClick={() => onNavigate('home')} className="signup-action-btn" style={{marginTop: '20px'}}>Anasayfaya Dön</button>
        </div>
      </div>
    </div>
  );
}

export default About;