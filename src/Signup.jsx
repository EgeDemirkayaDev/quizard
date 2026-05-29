import React, { useState } from "react";
import { api } from "./api";

function Signup({ onNavigate }) {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [message, setMessage] = useState("");
  const [messageType, setMessageType] = useState("");
  const [loading, setLoading] = useState(false);

  const handleRegister = async (e) => {
    e.preventDefault();

    setMessage("");
    setMessageType("");

    if (!email.trim() || !username.trim() || !password.trim()) {
      setMessage("Lütfen tüm alanları doldurun.");
      setMessageType("error");
      return;
    }

    if (password.length < 6) {
      setMessage("Şifre en az 6 karakter olmalıdır.");
      setMessageType("error");
      return;
    }

    try {
      setLoading(true);

      const response = await api.register({
        email: email.trim(),
        username: username.trim(),
        password: password
      });

      setMessage(response.message || "Üyelik başarıyla oluşturuldu.");
      setMessageType("success");

      setTimeout(() => {
        onNavigate("login");
      }, 1200);
    } catch (error) {
      setMessage(error.message || "Üyelik oluşturulurken bir hata oluştu.");
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
          <h2>Yeni Büyücü Kaydı 📜</h2>
          <p className="login-subtitle">Güçlerini keşfetmek için aramıza katıl!</p>

          {message && (
            <div className={`form-message ${messageType}`}>
              {message}
            </div>
          )}

          <form className="login-form" onSubmit={handleRegister}>
            <div className="input-group">
              <label>E-Posta</label>
              <input
                type="email"
                placeholder="baykus@hogwarts.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                disabled={loading}
              />
            </div>

            <div className="input-group">
              <label>Kullanıcı Adı</label>
              <input
                type="text"
                placeholder="GryffindorAslani"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                disabled={loading}
              />
            </div>

            <div className="input-group">
              <label>Şifre</label>
              <input
                type="password"
                placeholder="En az 6 karakter..."
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                disabled={loading}
              />
            </div>

            <button type="submit" className="signup-action-btn" disabled={loading}>
              {loading ? "Kaydediliyor..." : "Kaydı Tamamla"}
            </button>

            <div className="login-footer">
              <p>
                Zaten üye misin?{" "}
                <a href="#" onClick={(e) => { e.preventDefault(); onNavigate("login"); }}>
                  Giriş Yap
                </a>
              </p>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Signup;