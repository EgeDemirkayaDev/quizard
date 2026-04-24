import React, { useState } from 'react';

function Saved({ onNavigate, favorites, toggleFavorite, saved, toggleSave, isDarkMode, toggleTheme, notificationsEnabled, toggleNotifications }) {
  const [isSidebarOpen, setSidebarOpen] = useState(false);

  const allQuizzes = [
    { id: 1, title: 'Kişilik Testi', desc: 'Gizemli derinliklerini keşfet.', btn: 'Yoluna Başla', icon: '🔮' },
    { id: 2, title: 'Bölümde Hangi Hocasın?', desc: 'Akademik bilgeliğini ölç.', btn: 'Hocanı Bul', icon: '❓' },
    { id: 3, title: 'Yazılım Alanın Ne?', desc: 'Sihirli kodlama yolunu seç.', btn: 'Kodla', icon: '🪄' },
    { id: 4, title: 'Hangi Hayvansın?', desc: 'Ruh hayvanınla tanış.', btn: 'Keşfet', icon: '🦉' }
  ];

  const savedQuizzes = allQuizzes.filter(q => saved.includes(q.id));

  return (
    <div className={`dash-wrapper ${isDarkMode ? 'dash-dark' : 'dash-light'}`}>
      <header className="dash-topbar">
        <div className="dash-left" style={{ width: 'auto', gap: '15px' }}><button className="dash-hamburger" onClick={() => setSidebarOpen(true)}>☰</button><div className="dash-logo" style={{ display: 'flex', alignItems: 'center', gap: '8px', whiteSpace: 'nowrap' }}>Kaydettiklerim <span>🔖</span></div></div>
        <div className="dash-right"><div className="dash-profile">🧙</div></div>
      </header>

      <div className={`dash-sidebar-menu ${isSidebarOpen ? 'is-open' : ''}`}>
        <button className="dash-close-btn" onClick={() => setSidebarOpen(false)}>✖</button>
        <ul className="dash-menu-list">
          <li onClick={() => onNavigate('dashboard')}><span className="dash-icon">🏠</span> Anasayfa</li>
          <li onClick={() => onNavigate('favorites')}><span className="dash-icon">💜</span> Favoriler</li>
          <li onClick={() => onNavigate('saved')} className="active-nav"><span className="dash-icon">🔖</span> Kaydettiklerim</li>
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

      <main className="dash-main-area">
        {savedQuizzes.length > 0 ? (
          <div className="quiz-grid" style={{ maxWidth: '1000px', width: '100%', marginTop: '30px' }}>
            {savedQuizzes.map(q => (
              <div key={q.id} className="quiz-card dash-card">
                <button className={`card-action-btn favorite-btn ${favorites.includes(q.id) ? 'active' : ''}`} onClick={() => toggleFavorite(q.id)}>{favorites.includes(q.id) ? '❤️' : '🤍'}</button>
                <div className="card-icon">{q.icon}</div>
                <div className="card-info">
                  <h3>{q.title}</h3>
                  <p>{q.desc}</p>
                  <button className="card-btn" onClick={() => onNavigate('quiz', q.id)}>{q.btn}</button>
                </div>
                <button className="card-action-btn save-btn active" onClick={() => toggleSave(q.id)}>💾</button>
              </div>
            ))}
          </div>
        ) : (
          <div className="dash-empty-state"><h2>Henüz kaydettiğin bir test yok! ✨</h2><p style={{marginBottom: '25px', opacity: 0.7}}>Daha sonra çözmek istediklerini buraya kaydedebilirsin.</p><button className="card-btn" onClick={() => onNavigate('dashboard')}>Test Keşfet</button></div>
        )}
      </main>
    </div>
  );
}

export default Saved;