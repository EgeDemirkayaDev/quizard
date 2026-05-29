import React, { useState } from "react";
import { api } from "./api";

function Login({ onNavigate }) {
  const [showPassword, setShowPassword] = useState(false);

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [message, setMessage] = useState("");
  const [messageType, setMessageType] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();

    setMessage("");
    setMessageType("");

    if (!username.trim() || !password.trim()) {
      setMessage("Kullanıcı adı ve şifre boş bırakılamaz.");
      setMessageType("error");
      return;
    }

    try {
      setLoading(true);

      const response = await api.login({
        username: username.trim(),
        password: password
      });

      localStorage.setItem("quizard_user", JSON.stringify(response.user));

      setMessage(response.message || "Giriş başarılı.");
      setMessageType("success");

      setTimeout(() => {
        onNavigate("dashboard");
      }, 800);
    } catch (error) {
      setMessage(error.message || "Giriş yapılırken bir hata oluştu.");
      setMessageType("error");
    } finally {
      setLoading(false);
    }
  };

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
        <div className="login-card">
          <h2>Büyücü Girişi 🔮</h2>
          <p className="login-subtitle">Sihirli dünyana geri dön!</p>

          {message && (
            <div className={`form-message ${messageType}`}>
              {message}
            </div>
          )}

          <form className="login-form" onSubmit={handleLogin}>
            <div className="input-group">
              <label>Kullanıcı Adı</label>
              <input
                type="text"
                placeholder="Büyücü adını gir..."
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                disabled={loading}
              />
            </div>

            <div className="input-group">
              <label>Şifre</label>

              <div className="input-with-icon">
                <input
                  type={showPassword ? "text" : "password"}
                  placeholder="Gizli parolanı gir..."
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  disabled={loading}
                />

                <button
                  type="button"
                  className="eye-btn"
                  onClick={() => setShowPassword(!showPassword)}
                  disabled={loading}
                >
                  {showPassword ? "👁️‍🗨️" : "👁️"}
                </button>
              </div>
            </div>

            <button type="submit" className="signup-action-btn" disabled={loading}>
              {loading ? "Giriş yapılıyor..." : "Giriş Yap"}
            </button>

            <div className="login-footer">
              <p style={{ marginBottom: "10px" }}>
                <a href="#" onClick={(e) => { e.preventDefault(); onNavigate("forgot"); }}>
                  Şifremi Unuttum?
                </a>
              </p>

              <p>
                Hesabın yok mu?{" "}
                <a href="#" onClick={(e) => { e.preventDefault(); onNavigate("signup"); }}>
                  Kayıt Ol
                </a>
              </p>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;