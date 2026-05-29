import React, { useEffect, useState } from "react";
import { api } from "./api";

function App({ onNavigate }) {
  const [ozelIsim, setOzelIsim] = useState("");
  const [tests, setTests] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const isim = params.get("kime");

    if (isim) {
      const formatliIsim = isim.charAt(0).toUpperCase() + isim.slice(1);
      setOzelIsim(formatliIsim);
    }
  }, []);

  useEffect(() => {
    api.getTests()
      .then((data) => {
        setTests(data);
        setErrorMessage("");
      })
      .catch(() => {
        setErrorMessage("Testler yüklenirken bir sorun oluştu.");
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return (
    <div className="main-wrapper">
      <header className="wizard-header">
        <div className="logo">🧙‍♂️ quizard ✨</div>

        <nav>
          <a href="#" onClick={(e) => { e.preventDefault(); onNavigate("home"); }}>
            Anasayfa
          </a>
          <a href="#" onClick={(e) => { e.preventDefault(); onNavigate("about"); }}>
            Hakkımızda
          </a>
        </nav>

        <button onClick={() => onNavigate("login")} className="login-btn">
          Giriş Yap
        </button>
      </header>

      <div className="center-content">
        <div className="wizard-container">
          <main className="main-content">
            <section className="home-tests-area">
              <div className="welcome-banner">
                <h2>
                  {ozelIsim
                    ? `Hoş geldin ${ozelIsim}! Seçilmiş kişi sen misin? ⚡`
                    : "Hoş geldin Büyücü! Sihirli yolculuğuna başla. ⚡"}
                </h2>
              </div>

              {loading && (
                <div className="status-message">Testler yükleniyor...</div>
              )}

              {!loading && errorMessage && (
                <div className="status-message error">{errorMessage}</div>
              )}

              {!loading && !errorMessage && (
                <div className="quiz-grid">
                  {tests.map((test) => (
                    <div key={test.id} className="quiz-card">
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
            </section>

            <aside className="right-sidebar">
              <h2>Topluluğa Katıl</h2>
              <p className="sidebar-subtitle">
                Test sonuçlarını kaydetmek, favorilerine eklemek ve yorum yapmak için giriş yap.
              </p>
              <button className="signup-action-btn" onClick={() => onNavigate("signup")}>
                Kayıt Ol
              </button>
              <p className="copyright">© Quizard</p>
            </aside>
          </main>
        </div>
      </div>
    </div>
  );
}

export default App;