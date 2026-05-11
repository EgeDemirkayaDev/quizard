// Backend'ci arkadaşın FastAPI sunucusunun adresi. 
// (FastAPI genelde 8000 portunda çalışır. Onlar sana farklı bir port verirse burayı değiştirirsin kanka)
const BASE_URL = 'http://localhost:8000/api';

// Güvenlik Kapısı: Kullanıcı giriş yaptığında aldığımız "Token"ı her isteğin cebine koyan yardımcı fonksiyon
const getAuthHeaders = () => {
  const token = localStorage.getItem('token'); // Token'ı tarayıcı hafızasından alıyoruz
  return {
    'Content-Type': 'application/json',
    ...(token && { 'Authorization': `Bearer ${token}` })
  };
};

// Bütün API isteklerimizi tutan ana obje (Backend'ci abiler buraya bayılacak)
export const api = {
  
  // ==========================================
  // 1. KULLANICI İŞLEMLERİ (AUTH & SETTINGS)
  // ==========================================
  
  login: async (email, password) => {
    const response = await fetch(`${BASE_URL}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    return response.json();
  },

  register: async (userData) => {
    const response = await fetch(`${BASE_URL}/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });
    return response.json();
  },

  updateSettings: async (settingsData) => {
    const response = await fetch(`${BASE_URL}/settings`, {
      method: 'PUT',
      headers: getAuthHeaders(),
      body: JSON.stringify(settingsData)
    });
    return response.json();
  },

  // ==========================================
  // 2. TESTLER (QUIZZES)
  // ==========================================
  
  getAllQuizzes: async () => {
    const response = await fetch(`${BASE_URL}/quizzes`, {
      method: 'GET',
      headers: getAuthHeaders()
    });
    return response.json();
  },

  getQuizById: async (quizId) => {
    const response = await fetch(`${BASE_URL}/quizzes/${quizId}`, {
      method: 'GET',
      headers: getAuthHeaders()
    });
    return response.json();
  },

  // ==========================================
  // 3. FAVORİLER VE KAYDEDİLENLER
  // ==========================================
  
  toggleFavorite: async (quizId) => {
    const response = await fetch(`${BASE_URL}/favorites/toggle`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify({ quiz_id: quizId })
    });
    return response.json();
  },

  toggleSaved: async (quizId) => {
    const response = await fetch(`${BASE_URL}/saved/toggle`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify({ quiz_id: quizId })
    });
    return response.json();
  },

  // ==========================================
  // 4. YORUMLAR (COMMENTS)
  // ==========================================
  
  getMyComments: async () => {
    const response = await fetch(`${BASE_URL}/comments/me`, {
      method: 'GET',
      headers: getAuthHeaders()
    });
    return response.json();
  },

  addComment: async (quizId, content) => {
    const response = await fetch(`${BASE_URL}/comments`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify({ quiz_id: quizId, content })
    });
    return response.json();
  }
};