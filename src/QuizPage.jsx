import React, { useEffect, useState } from "react";
import { api } from "./api";

function QuizPage({
  onNavigate,
  quizId,
  isDarkMode,
  toggleTheme,
  notificationsEnabled,
  toggleNotifications
}) {
  const [isSidebarOpen, setSidebarOpen] = useState(false);
  const [testData, setTestData] = useState(null);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedOptionIds, setSelectedOptionIds] = useState([]);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    if (!quizId) {
      setErrorMessage("Test bilgisi bulunamadı.");
      setLoading(false);
      return;
    }

    api.getTestById(quizId)
      .then((data) => {
        setTestData(data);
        setErrorMessage("");
      })
      .catch(() => {
        setErrorMessage("Test yüklenirken bir sorun oluştu.");
      })
      .finally(() => {
        setLoading(false);
      });
  }, [quizId]);

  const handleOptionSelect = async (optionId) => {
    const updatedAnswers = [...selectedOptionIds, optionId];
    setSelectedOptionIds(updatedAnswers);

    const isLastQuestion = currentQuestionIndex >= testData.questions.length - 1;

    if (!isLastQuestion) {
      setCurrentQuestionIndex((prev) => prev + 1);
      return;
    }

    try {
      setLoading(true);
      const data = await api.submitTest(testData.id, updatedAnswers);
      setResult(data);
    } catch {
      setErrorMessage("Sonuç hesaplanırken bir hata oluştu.");
    } finally {
      setLoading(false);
    }
  };

  const currentQuestion = testData?.questions?.[currentQuestionIndex];

  return (
    <div className={`dash-wrapper ${isDarkMode ? "dash-dark" : "dash-light"}`}>
      <header className="dash-topbar">
        <div className="dash-left" style={{ width: "auto", gap: "15px" }}>
          <button className="dash-hamburger" onClick={() => setSidebarOpen(true)}>
            ☰
          </button>
          <div
            className="dash-logo"
            style={{ cursor: "pointer" }}
            onClick={() => onNavigate("dashboard")}
          >
            quizard <span>🧙‍♂️</span>
          </div>
        </div>

        <div className="dash-right">
          <div className="dash-profile">🧙</div>
        </div>
      </header>

      <div className={`dash-sidebar-menu ${isSidebarOpen ? "is-open" : ""}`}>
        <button className="dash-close-btn" onClick={() => setSidebarOpen(false)}>✖</button>

        <ul className="dash-menu-list">
          <li onClick={() => onNavigate("dashboard")}><span className="dash-icon">🏠</span> Anasayfa</li>
          <li onClick={() => onNavigate("favorites")}><span className="dash-icon">💜</span> Favoriler</li>
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

      <main className="dash-main-area quiz-page-area">
        <div className="settings-card quiz-panel">
          {loading && (
            <div className="status-message">
              Sihir yükleniyor... 🪄
            </div>
          )}

          {!loading && errorMessage && (
            <div className="status-message error">
              {errorMessage}
              <br />
              <button className="card-btn" onClick={() => onNavigate("dashboard")}>
                Panoya Dön
              </button>
            </div>
          )}

          {!loading && result && (
            <div className="result-box">
              <h1>{testData?.icon || "✨"}</h1>
              <h2>{result.resultTitle || result.kazanan || "Sonucun Hazır!"}</h2>
              <p>{result.resultDescription || result.aciklama}</p>

              <button className="card-btn" onClick={() => onNavigate("dashboard")}>
                Panoya Geri Dön
              </button>
            </div>
          )}

          {!loading && !result && !errorMessage && testData && currentQuestion && (
            <div className="question-box">
              <div className="question-header">
                <h2>{testData.title} {testData.icon}</h2>
                <p>
                  Soru {currentQuestionIndex + 1} / {testData.questions.length}
                </p>
              </div>

              <h3 className="question-text">{currentQuestion.text}</h3>

              <div className="option-list">
                {currentQuestion.options.map((option) => (
                  <button
                    key={option.id}
                    className="option-btn"
                    onClick={() => handleOptionSelect(option.id)}
                  >
                    {option.text}
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default QuizPage;