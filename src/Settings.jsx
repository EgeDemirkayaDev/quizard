import React, { useState } from 'react';

function Settings({ onNavigate, isDarkMode, toggleTheme, notificationsEnabled, toggleNotifications }) {
  const [isSidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className={`dash-wrapper ${isDarkMode ? 'dash-dark' : 'dash-light'}`}>
      <header className="dash-topbar">
        <div className="dash-left" style={{ width: 'auto', gap: '15px' }}><button className="dash-hamburger" onClick={() => setSidebarOpen(true)}>☰</button><div className="dash-logo" style={{ display: 'flex', alignItems: 'center', gap: '8px', whiteSpace: 'nowrap' }}>Hesap Ayarları <span>⚙️</span></div></div>
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
          <li onClick={() => onNavigate('settings')} className="active-nav"><span className="dash-icon">⚙️</span> Hesap Ayarları</li>
          <li onClick={toggleTheme} style={{ color: isDarkMode ? '#fde047' : '#059669', cursor: 'pointer' }}><span className="dash-icon">{isDarkMode ? '☀️' : '🌙'}</span> {isDarkMode ? 'Gündüz Modu' : 'Gece Modu'}</li>
          <li className="dash-logout" onClick={() => onNavigate('home')}><span className="dash-icon">🚪</span> Çıkış Yap</li>
        </ul>
      </div>

      {isSidebarOpen && <div className="dash-overlay" onClick={() => setSidebarOpen(false)}></div>}

      <main className="dash-main-area">
        <div className="settings-container">
          <div className="settings-card"><h2>Hesap Bilgilerim 🦉</h2><div className="input-group"><label>Kayıtlı E-Posta Adresi</label><input type="email" value="baykus@hogwarts.com" disabled style={{ opacity: 0.7 }} /></div></div>
          <div className="settings-card"><h2>Şifremi Değiştir 🔑</h2><div className="input-group"><label>Mevcut Şifre</label><input type="password" placeholder="Şu anki şifreni gir..." /></div><div className="input-group"><label>Yeni Şifre</label><input type="password" placeholder="Yeni şifreni belirle..." /></div><button className="card-btn" style={{ marginTop: '10px' }}>Şifreyi Güncelle</button></div>
          <div className="settings-card danger-zone"><h2>Tehlikeli Bölge ⚠️</h2><p>Hesabını devre dışı bırakırsan tüm sihirli testlerin, favorilerin ve kaydettiklerin karanlık ormanda kaybolur. Bu işlem geri alınamaz!</p><button className="danger-btn">Hesabımı Devre Dışı Bırak</button></div>
        </div>
      </main>
    </div>
  );
}

export default Settings;