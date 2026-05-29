import React, { useEffect, useState } from "react";
import { api } from "./api";

function Dashboard({
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
  const [searchQuery, setSearchQuery] = useState("");
  const [tests, setTests] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    api.getTests()
      .then((data) => {
        setTests(data);
        setErrorMessage("");
      })
      .catch(() => {
        setErrorMessage("Testler yüklenemedi.");
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  const filteredTests = tests.filter((test) => {
    const searchText = `${test.title} ${test.description} ${test.category}`.toLowerCase();
    return searchText.includes(searchQuery.toLowerCase());
  });

  return (
    <div className={`dash-wrapper ${isDarkMode ? "dash-dark" : "dash-light"}`}>
      <header className="dash-topbar">
        <div className="dash-left" style={{ width: "auto", gap: "15px" }}>
          <button className="dash-hamburger" onClick={() => setSidebarOpen(true)}>
            ☰
          </button>
          <div className="dash-logo">
            quizard <span>🧙‍♂️</span>
          </div>
        </div>

        <div className="dash-center">
          <input
            type="text"
            className="dash-search-input"
            placeholder="Testlerde ara..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
        </div>

        <div className="dash-right">
          <div className="dash-profile">🧙</div>
        </div>
      </header>

      <div className={`dash-sidebar-menu ${isSidebarOpen ? "is-open" : ""}`}>
        <button className="dash-close-btn" onClick={() => setSidebarOpen(false)}>
          ✖
        </button>

        <ul className="dash-menu-list">
          <li onClick={() => onNavigate("dashboard")} className="active-nav">
            <span className="dash-icon">🏠</span> Anasayfa
          </li>
          <li onClick={() => onNavigate("favorites")}>
            <span className="dash-icon">💜</span> Favoriler
          </li>
          <li onClick={() => onNavigate("saved")}>
            <span className="dash-icon">🔖</span> Kaydettiklerim
          </li>
          <li onClick={() => onNavigate("comments")}>
            <span className="dash-icon">💬</span> Yorumlarım
          </li>

          <li style={{ display: "flex", justifyContent: "space-between", alignItems: "center", cursor: "default" }}>
            <div style={{ display: "flex", alignItems: "center", gap: "15px" }}>
              <span className="dash-icon">🔔</span> Bildirimler
            </div>
            <label className="switch">
              <input
                type="checkbox"
                checked={notificationsEnabled}
                onChange={toggleNotifications}
              />
              <span className="slider"></span>
            </label>
          </li>

          <li onClick={() => onNavigate("settings")}>
            <span className="dash-icon">⚙️</span> Hesap Ayarları
          </li>
          <li onClick={toggleTheme} style={{ color: isDarkMode ? "#fde047" : "#059669", cursor: "pointer" }}>
            <span className="dash-icon">{isDarkMode ? "☀️" : "🌙"}</span>
            {isDarkMode ? "Gündüz Modu" : "Gece Modu"}
          </li>
          <li className="dash-logout" onClick={() => onNavigate("home")}>
            <span className="dash-icon">🚪</span> Çıkış Yap
          </li>
        </ul>
      </div>

      {isSidebarOpen && <div className="dash-overlay" onClick={() => setSidebarOpen(false)}></div>}

      <main className="dash-main-area">
        {loading && <div className="status-message">Testler yükleniyor...</div>}

        {!loading && errorMessage && (
          <div className="status-message error">{errorMessage}</div>
        )}

        {!loading && !errorMessage && (
          <div className="quiz-grid" style={{ maxWidth: "1000px", width: "100%", marginTop: "30px" }}>
            {filteredTests.map((test) => (
              <div key={test.id} className="quiz-card dash-card">
                <button
                  className={`card-action-btn favorite-btn ${favorites.includes(test.id) ? "active" : ""}`}
                  onClick={() => toggleFavorite(test.id)}
                >
                  {favorites.includes(test.id) ? "❤️" : "🤍"}
                </button>

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

                  <button
                    className="card-btn"
                    onClick={() => onNavigate("quiz", test.id)}
                  >
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

export default Dashboard;