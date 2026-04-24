import React, { useState } from 'react';

function QuizPage({ onNavigate, quizId, isDarkMode, toggleTheme, notificationsEnabled, toggleNotifications }) {
  const [isSidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className={`dash-wrapper ${isDarkMode ? 'dash-dark' : 'dash-light'}`}>
      <header className="dash-topbar">
        <div className="dash-left" style={{ width: 'auto', gap: '15px' }}>
          <button className="dash-hamburger" onClick={() => setSidebarOpen(true)}>☰</button>
          <div className="dash-logo" style={{ cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '8px', whiteSpace: 'nowrap' }} onClick={() => onNavigate('dashboard')}>
            quizard <span>🧙‍♂️</span>
          </div>
        </div>
        <div className="dash-right"><div className="dash-profile">🧙</div></div>
      </header>

      <div className={`dash-sidebar-menu ${isSidebarOpen ? 'is-open' : ''}`}>
        <button className="dash-close-btn" onClick={() => setSidebarOpen(false)}>✖</button>
        <ul className="dash-menu-list">
          <li onClick={() => onNavigate('dashboard')}><span className="dash-icon">🏠</span> Anasayfa</li>
          <li onClick={() => onNavigate('favorites')}><span className="dash-icon">💜</span> Favoriler</li>
          <li onClick={() => onNavigate('saved')}><span className="dash-icon">🔖</span> Kaydettiklerim</li>
          <li onClick={() => onNavigate('comments')}><span className="dash-icon">💬</span> Yorumlarım</li>
          <li style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', cursor: 'default' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}><span className="dash-icon">🔔</span> Bildirimler</div>
            <label className="switch">
              <input type="checkbox" checked={notificationsEnabled} onChange={toggleNotifications} />
              <span className="slider"></span>
            </label>
          </li>
          <li onClick={() => onNavigate('settings')}><span className="dash-icon">⚙️</span> Hesap Ayarları</li>
          <li onClick={toggleTheme} style={{ color: isDarkMode ? '#fde047' : '#059669', cursor: 'pointer' }}><span className="dash-icon">{isDarkMode ? '☀️' : '🌙'}</span> {isDarkMode ? 'Gündüz Modu' : 'Gece Modu'}</li>
          <li className="dash-logout" onClick={() => onNavigate('home')}><span className="dash-icon">🚪</span> Çıkış Yap</li>
        </ul>
      </div>

      {isSidebarOpen && <div className="dash-overlay" onClick={() => setSidebarOpen(false)}></div>}

      <main className="dash-main-area" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <div className="settings-card" style={{ textAlign: 'center', maxWidth: '600px', width: '100%' }}>
          <h2>Test Ekranı 📝</h2>
          <p style={{ fontSize: '1.2rem', marginTop: '10px' }}>Seçilen Test ID: <strong>{quizId}</strong></p>
          <div style={{ padding: '30px', border: '2px dashed #7c3aed', borderRadius: '15px', margin: '30px 0' }}>
            <p style={{ opacity: 0.8 }}>
              Backend geliştirici arkadaşlar;<br/><br/>
              API'den çekeceğiniz <strong>soruları ve şıkları</strong> bu componentin içerisine bağlayabilirsiniz. <br/>
              <em>(Şu an arayüz testleri bekliyor)</em>
            </p>
          </div>
          <button className="card-btn" onClick={() => onNavigate('dashboard')}>Panoya Geri Dön</button>
        </div>
      </main>
    </div>
  );
}

export default QuizPage;