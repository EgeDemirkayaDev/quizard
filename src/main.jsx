import React, { useState } from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import Login from './Login.jsx'
import Signup from './Signup.jsx'
import About from './About.jsx'
import Forgot from './Forgot.jsx'
import Dashboard from './Dashboard.jsx'
import Favorites from './Favorites.jsx'
import Saved from './Saved.jsx'
import Settings from './Settings.jsx'
import QuizPage from './QuizPage.jsx'
import Comments from './Comments.jsx' /* 👇 YENİ SAYFAMIZ 👇 */
import './index.css'

function Root() {
  const [page, setPage] = useState('home');
  const [activeQuizId, setActiveQuizId] = useState(null); 
  
  const handleNavigate = (targetPage, data = null) => {
    setPage(targetPage);
    if (data !== null) {
      setActiveQuizId(data);
    }
  };

  const [favorites, setFavorites] = useState([]);
  const toggleFavorite = (id) => setFavorites(prev => prev.includes(id) ? prev.filter(fId => fId !== id) : [...prev, id]);

  const [saved, setSaved] = useState([]);
  const toggleSave = (id) => setSaved(prev => prev.includes(id) ? prev.filter(sId => sId !== id) : [...prev, id]);

  const [isDarkMode, setIsDarkMode] = useState(false);
  const toggleTheme = () => setIsDarkMode(!isDarkMode);

  // 👇 YENİ: Bildirim Aç/Kapa Hafızası 👇
  const [notificationsEnabled, setNotificationsEnabled] = useState(true); // Başlangıçta açık
  const toggleNotifications = () => setNotificationsEnabled(!notificationsEnabled);

  const renderPage = () => {
    // Ortak props'ları bir araya topladık ki kod kalabalığı olmasın
    const sharedProps = {
      onNavigate: handleNavigate,
      favorites, toggleFavorite,
      saved, toggleSave,
      isDarkMode, toggleTheme,
      notificationsEnabled, toggleNotifications // Bildirim durumu her sayfaya gidiyor
    };

    switch(page) {
      case 'home': return <App onNavigate={handleNavigate} />;
      case 'login': return <Login onNavigate={handleNavigate} />;
      case 'signup': return <Signup onNavigate={handleNavigate} />;
      case 'about': return <About onNavigate={handleNavigate} />;
      case 'forgot': return <Forgot onNavigate={handleNavigate} />;
      case 'dashboard': return <Dashboard {...sharedProps} />;
      case 'favorites': return <Favorites {...sharedProps} />;
      case 'saved': return <Saved {...sharedProps} />;
      case 'settings': return <Settings {...sharedProps} />;
      case 'quiz': return <QuizPage {...sharedProps} quizId={activeQuizId} />;
      case 'comments': return <Comments {...sharedProps} />; /* YORUMLAR SAYFASI */
      default: return <App onNavigate={handleNavigate} />;
    }
  };

  return <React.StrictMode>{renderPage()}</React.StrictMode>;
}

ReactDOM.createRoot(document.getElementById('root')).render(<Root />);