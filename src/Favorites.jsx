import React, { useEffect, useState } from "react";
import { api } from "./api";

function Favorites({
  onNavigate,
  favorites,
  toggleFavorite,
  saved,
  toggleSave,
  isDarkMode,
  toggleTheme,
  notificationsEnabled,
  toggleNotifications
}) {
  const [isSidebarOpen, setSidebarOpen] = useState(false);
  const [tests, setTests] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.getTests()
      .then((data) => setTests(data))
      .finally(() => setLoading(false));
  }, []);

  const favoriteTests = tests.filter((test) => favorites.includes(test.id));

  return (
    <div className={`dash-wrapper ${isDarkMode ? "dash-dark" : "dash-light"}`}>
      <header className="dash-topbar">
        <div className="dash-left" style={{ width: "auto", gap: "15px" }}>
          <button className="dash-hamburger" onClick={() => setSidebarOpen(true)}>☰</button>
          <div className="dash-logo">Favorilerim <span>💜</span></div>
        </div>
        <div className="dash-right"><div className="dash-profile">🧙</div></div>
      </header>

      <div className={`dash-sidebar-menu ${isSidebarOpen ? "is-open" : ""}`}>
        <button className="dash-close-btn" onClick={() => setSidebarOpen(false)}>✖</button>

        <ul className="dash-menu-list">
          <li onClick={() => onNavigate("dashboard")}><span className="dash-icon">🏠</span> Anasayfa</li>
          <li onClick={() => onNavigate("favorites")} className="active-nav"><span className="dash-icon">💜</span> Favoriler</li>
          <li onClick={() => onNavigate("saved")}><span className="dash-icon">🔖</span> Kaydettiklerim</li>
          <li onClick={() => onNavigate("comments")}><span className="dash-icon">💬</span> Yorumlarım</li>

          <li style={{ display: "flex", justifyContent: "space-between", alignItems: "center", cursor: "default" }}>
            <div style={{ display: "flex", alignItems: "center", gap: "15px" }}>
              <span className="dash-icon">🔔</span> Bildirimler
            </div>
            <label className="switch">
              <input type="checkbox" checked={notificationsEnabled} onChange={toggleNotifications} />
              <span className="slider"></span>
            </label>
          </li>

          <li onClick={() => onNavigate("settings")}><span className="dash-icon">⚙️</span> Hesap Ayarları</li>
          <li onClick={toggleTheme}><span className="dash-icon">{isDarkMode ? "☀️" : "🌙"}</span>{isDarkMode ? "Gündüz Modu" : "Gece Modu"}</li>
          <li className="dash-logout" onClick={() => onNavigate("home")}><span className="dash-icon">🚪</span> Çıkış Yap</li>
        </ul>
      </div>

      {isSidebarOpen && <div className="dash-overlay" onClick={() => setSidebarOpen(false)}></div>}

      <main className="dash-main-area">
        {loading && <div className="status-message">Favoriler yükleniyor...</div>}

        {!loading && favoriteTests.length === 0 && (
          <div className="empty-state">
            <h2>Henüz favori testin yok 💜</h2>
            <p>Beğendiğin testleri favorilere ekleyebilirsin.</p>
            <button className="card-btn" onClick={() => onNavigate("dashboard")}>
              Testlere Git
            </button>
          </div>
        )}

        {!loading && favoriteTests.length > 0 && (
          <div className="quiz-grid" style={{ maxWidth: "1000px", width: "100%", marginTop: "30px" }}>
            {favoriteTests.map((test) => (
              <div key={test.id} className="quiz-card dash-card">
                <button className="card-action-btn favorite-btn active" onClick={() => toggleFavorite(test.id)}>❤️</button>

                <button
                  className={`card-action-btn save-btn ${saved.includes(test.id) ? "active" : ""}`}
                  onClick={() => toggleSave(test.id)}
                >
                  {saved.includes(test.id) ? "🔖" : "📑"}
                </button>

                <div className="card-icon">{test.icon}</div>

                <div className="card-info">
                  <span className="card-category">{test.category}</span>
                  <h3>{test.shortTitle || test.title}</h3>
                  <p>{test.description}</p>
                  <button className="card-btn" onClick={() => onNavigate("quiz", test.id)}>
                    {test.buttonText || "Teste Başla"}
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}

export default Favorites;