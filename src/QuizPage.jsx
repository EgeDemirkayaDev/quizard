import React, { useState, useEffect } from 'react';

function QuizPage({ onNavigate, quizId, isDarkMode, toggleTheme, notificationsEnabled, toggleNotifications }) {
  const [isSidebarOpen, setSidebarOpen] = useState(false);

  // --- 🔥 BACKEND İLETİŞİMİ İÇİN YENİ STATE'LER 🔥 ---
  const [testData, setTestData] = useState(null); // Backend'den gelen sorular
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0); // Hangi sorudayız?
  const [selectedAnswers, setSelectedAnswers] = useState([]); // Kullanıcının seçtiği şıkların ID'leri
  const [result, setResult] = useState(null); // Backend'in hesapladığı sonuç
  const [loading, setLoading] = useState(true); // Yükleniyor animasyonu için

  // 1. ADIM: SAYFA AÇILIR AÇILMAZ BACKEND'DEN SORULARI ÇEK
  useEffect(() => {
    // Sadece testId 1 (Hoca testi) ise çekiyoruz, diğerlerini henüz backend'e eklemedik.
    fetch(`http://127.0.0.1:8000/api/testler/${quizId}`)
      .then(res => {
        if (!res.ok) throw new Error("Test bulunamadı");
        return res.json();
      })
      .then(data => {
        setTestData(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Hata:", err);
        setLoading(false);
      });
  }, [quizId]);

  // 2. ADIM: KULLANICI BİR ŞIKKA TIKLADIĞINDA NE OLACAK?
  const handleOptionSelect = (secenekId) => {
    // Seçilen şıkkın ID'sini sepete ekle
    const newAnswers = [...selectedAnswers, secenekId];
    setSelectedAnswers(newAnswers);

    // Eğer son soruya gelmediysek, sıradaki soruya geç
    if (currentQuestionIndex < testData.sorular.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      // 3. ADIM: SON SORUYSA BACKEND'E POSTALA VE SONUCU HESAPLAT
      setLoading(true);
      fetch(`http://127.0.0.1:8000/api/testler/${quizId}/hesapla`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ secenek_idleri: newAnswers })
      })
      .then(res => res.json())
      .then(data => {
        setResult(data); // Backend'den gelen analiz metnini kaydet
        setLoading(false);
      })
      .catch(err => {
        console.error("Hesaplama hatası:", err);
        setLoading(false);
      });
    }
  };

  return (
    <div className={`dash-wrapper ${isDarkMode ? 'dash-dark' : 'dash-light'}`}>
      <header className="dash-topbar">
        <div className="dash-left" style={{ width: 'auto', gap: '15px' }}>
          <button className="dash-hamburger" onClick={() => setSidebarOpen(true)}>☰</button>
          <div className="dash-logo" style={{ cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '8px', whiteSpace: 'nowrap' }} onClick={() => onNavigate('dashboard')}>
            quizard <span>🧙‍♂️</span>
          </div>
        </div>
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
          <li onClick={() => onNavigate('settings')}><span className="dash-icon">⚙️</span> Hesap Ayarları</li>
          <li onClick={toggleTheme} style={{ color: isDarkMode ? '#fde047' : '#059669', cursor: 'pointer' }}><span className="dash-icon">{isDarkMode ? '☀️' : '🌙'}</span> {isDarkMode ? 'Gündüz Modu' : 'Gece Modu'}</li>
          <li className="dash-logout" onClick={() => onNavigate('home')}><span className="dash-icon">🚪</span> Çıkış Yap</li>
        </ul>
      </div>

      {isSidebarOpen && <div className="dash-overlay" onClick={() => setSidebarOpen(false)}></div>}

      <main className="dash-main-area" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '80vh' }}>
        <div className="settings-card" style={{ maxWidth: '700px', width: '100%', padding: '2rem' }}>
          
          {/* EKRAN 1: Yükleniyor */}
          {loading && (
            <div style={{ textAlign: 'center' }}>
              <h2>Sihir Yükleniyor... 🪄</h2>
            </div>
          )}

          {/* EKRAN 2: Test Sonucu (Hesaplandıysa Göster) */}
          {!loading && result && (
            <div style={{ textAlign: 'center', animation: 'fadeIn 0.5s' }}>
              <h1 style={{ fontSize: '3rem', margin: '10px 0' }}>🎓</h1>
              <h2 style={{ color: '#7c3aed', marginBottom: '15px' }}>{result.kazanan} Hoca Olurdun!</h2>
              <p style={{ fontSize: '1.2rem', lineHeight: '1.6', opacity: 0.9 }}>
                {result.aciklama}
              </p>
              <button className="card-btn" style={{ marginTop: '30px' }} onClick={() => onNavigate('dashboard')}>Panoya Geri Dön</button>
            </div>
          )}

          {/* EKRAN 3: Soruları Göster */}
          {!loading && !result && testData && (
            <div>
              <div style={{ textAlign: 'center', marginBottom: '30px' }}>
                <h2>{testData.baslik} {testData.ikon}</h2>
                <p style={{ opacity: 0.7, marginTop: '5px' }}>Soru {currentQuestionIndex + 1} / {testData.sorular.length}</p>
              </div>

              <div style={{ marginBottom: '20px' }}>
                <h3 style={{ fontSize: '1.3rem', marginBottom: '20px', lineHeight: '1.4' }}>
                  {testData.sorular[currentQuestionIndex].metin}
                </h3>
                
                <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                  {testData.sorular[currentQuestionIndex].secenekler.map((secenek) => (
                    <button 
                      key={secenek.id} 
                      onClick={() => handleOptionSelect(secenek.id)}
                      style={{
                        padding: '15px 20px',
                        fontSize: '1rem',
                        textAlign: 'left',
                        backgroundColor: isDarkMode ? '#334155' : '#f8fafc',
                        color: isDarkMode ? '#f8fafc' : '#1e293b',
                        border: `1px solid ${isDarkMode ? '#475569' : '#cbd5e1'}`,
                        borderRadius: '10px',
                        cursor: 'pointer',
                        transition: 'all 0.2s'
                      }}
                      onMouseOver={(e) => e.currentTarget.style.borderColor = '#7c3aed'}
                      onMouseOut={(e) => e.currentTarget.style.borderColor = isDarkMode ? '#475569' : '#cbd5e1'}
                    >
                      {secenek.metin}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* EKRAN 4: Test Bulunamadı Hatası */}
          {!loading && !testData && !result && (
            <div style={{ textAlign: 'center' }}>
              <h2>🚨 Hata! Test Bulunamadı.</h2>
              <p style={{ marginTop: '10px' }}>Bu test henüz veritabanına eklenmemiş olabilir. Şimdilik ID: 1 olan (Hocanı Bul) testini deneyin.</p>
              <button className="card-btn" style={{ marginTop: '20px' }} onClick={() => onNavigate('dashboard')}>Panoya Geri Dön</button>
            </div>
          )}

        </div>
      </main>
    </div>
  );
}

export default QuizPage;