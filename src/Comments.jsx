import React, { useState } from 'react';

function Comments({ onNavigate, isDarkMode, toggleTheme, notificationsEnabled, toggleNotifications }) {
  const [isSidebarOpen, setSidebarOpen] = useState(false);

  // Şimdilik yorumlar boş (Backend'ci arkadaş burayı dolduracak)
  const myComments = []; 

  return (
    <div className={`dash-wrapper ${isDarkMode ? 'dash-dark' : 'dash-light'}`}>
      <header className="dash-topbar">
        <div className="dash-left" style={{ width: 'auto', gap: '15px' }}>
          <button className="dash-hamburger" onClick={() => setSidebarOpen(true)}>☰</button>
          <div className="dash-logo" style={{ display: 'flex', alignItems: 'center', gap: '8px', whiteSpace: 'nowrap' }}>
            Yorumlarım <span>💬</span>
          </div>
        </div>
        <div className="dash-right"><div className="dash-profile">🧙</div></div>
      </header>

      <div className={`dash-sidebar-menu ${isSidebarOpen ? 'is-open' : ''}`}>
        <button className="dash-close-btn" onClick={() => setSidebarOpen(false)}>✖</button>
        
        {/* 👇 YENİ GÜNCELLENMİŞ MENÜMÜZ 👇 */}
        <ul className="dash-menu-list">
          <li onClick={() => onNavigate('dashboard')}><span className="dash-icon">🏠</span> Anasayfa</li>
          <li onClick={() => onNavigate('favorites')}><span className="dash-icon">💜</span> Favoriler</li>
          <li onClick={() => onNavigate('saved')}><span className="dash-icon">🔖</span> Kaydettiklerim</li>
          
          <li onClick={() => onNavigate('comments')} className="active-nav"><span className="dash-icon">💬</span> Yorumlarım</li>
          
          {/* KAYDIRMALI BİLDİRİM BUTONU */}
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
        {myComments.length > 0 ? (
          <div>{/* Backend geldiğinde yorumlar burada listelenecek */}</div>
        ) : (
          <div className="dash-empty-state">
            <h2>Henüz bir yorumun yok! ✨</h2>
            <p style={{marginBottom: '25px', opacity: 0.7}}>Hemen sihirli testlere gidip kendi yorumlarını bırakabilirsin.</p>
            <button className="card-btn" onClick={() => onNavigate('dashboard')}>Testlere Git</button>
          </div>
        )}
      </main>
    </div>
  );
}

export default Comments;