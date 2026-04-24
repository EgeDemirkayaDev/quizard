import React, { useState } from 'react';

function Dashboard({ onNavigate, favorites, toggleFavorite, saved, toggleSave, isDarkMode, toggleTheme, notificationsEnabled, toggleNotifications }) {
  const [isSidebarOpen, setSidebarOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');

  const quizzes = [
    { id: 1, title: 'Kişilik Testi', desc: 'Gizemli derinliklerini keşfet.', btn: 'Yoluna Başla', icon: '🔮' },
    { id: 2, title: 'Bölümde Hangi Hocasın?', desc: 'Akademik bilgeliğini ölç.', btn: 'Hocanı Bul', icon: '❓' },
    { id: 3, title: 'Yazılım Alanın Ne?', desc: 'Sihirli kodlama yolunu seç.', btn: 'Kodla', icon: '🪄' },
    { id: 4, title: 'Hangi Hayvansın?', desc: 'Ruh hayvanınla tanış.', btn: 'Keşfet', icon: '🦉' }
  ];

  const filteredQuizzes = quizzes.filter(q => 
    q.title.toLowerCase().includes(searchQuery.toLowerCase()) || 
    q.desc.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className={`dash-wrapper ${isDarkMode ? 'dash-dark' : 'dash-light'}`}>
      <header className="dash-topbar">
        <div className="dash-left" style={{ width: 'auto', gap: '15px' }}>
          <button className="dash-hamburger" onClick={() => setSidebarOpen(true)}>☰</button>
          <div className="dash-logo" style={{ display: 'flex', alignItems: 'center', gap: '8px', whiteSpace: 'nowrap' }}>
            quizard <span>🧙‍♂️</span>
          </div>
        </div>
        <div className="dash-center">
          <input type="text" className="dash-search-input" placeholder="Büyülü dünyada ara..." value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} />
        </div>
        <div className="dash-right"><div className="dash-profile">🧙</div></div>
      </header>

      <div className={`dash-sidebar-menu ${isSidebarOpen ? 'is-open' : ''}`}>
        <button className="dash-close-btn" onClick={() => setSidebarOpen(false)}>✖</button>
        <ul className="dash-menu-list">
          <li onClick={() => onNavigate('dashboard')} className="active-nav"><span className="dash-icon">🏠</span> Anasayfa</li>
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

      <main className="dash-main-area">
        <div className="quiz-grid" style={{ maxWidth: '1000px', width: '100%', marginTop: '30px' }}>
          {filteredQuizzes.length > 0 ? (
            filteredQuizzes.map(q => (
              <div key={q.id} className="quiz-card dash-card">
                <button className={`card-action-btn favorite-btn ${favorites.includes(q.id) ? 'active' : ''}`} onClick={() => toggleFavorite(q.id)}>{favorites.includes(q.id) ? '❤️' : '🤍'}</button>
                <div className="card-icon">{q.icon}</div>
                <div className="card-info">
                  <h3>{q.title}</h3>
                  <p>{q.desc}</p>
                  <button className="card-btn" onClick={() => onNavigate('quiz', q.id)}>{q.btn}</button>
                </div>
                <button className={`card-action-btn save-btn ${saved.includes(q.id) ? 'active' : ''}`} onClick={() => toggleSave(q.id)}>{saved.includes(q.id) ? '💾' : '🔖'}</button>
              </div>
            ))
          ) : (
            <div className="dash-empty-state" style={{ gridColumn: '1 / -1' }}><h2>Sihirli sözlükte bunu bulamadık 🥺</h2><p style={{ opacity: 0.7 }}>Başka bir kelime denemeye ne dersin?</p></div>
          )}
        </div>
      </main>
    </div>
  );
}

export default Dashboard;