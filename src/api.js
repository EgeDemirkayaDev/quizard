import { mockTests, mockTestDetails, mockResult } from "./data/mockTests";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api";

// Şu an gerçek backend'e bağlanıyoruz.
// Mock sistemi tamamen kapalı.
const USE_MOCK = false;

async function request(endpoint, options = {}) {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    headers: {
      "Content-Type": "application/json",
      ...options.headers
    },
    ...options
  });

  const data = await response.json().catch(() => null);

  if (!response.ok) {
    throw new Error(data?.detail || "API isteği başarısız oldu.");
  }

  return data;
}

export const api = {
  async getTests() {
    if (USE_MOCK) {
      return [...mockTests].sort((a, b) => a.order - b.order);
    }

    return request("/tests");
  },

  async getTestById(testId) {
    if (USE_MOCK) {
      return mockTestDetails[testId];
    }

    return request(`/tests/${testId}`);
  },

  async submitTest(testId, optionIds) {
    if (USE_MOCK) {
      return mockResult;
    }

    return request(`/tests/${testId}/submit`, {
      method: "POST",
      body: JSON.stringify({
        option_ids: optionIds
      })
    });
  },

  async getFavorites() {
    if (USE_MOCK) {
      return [];
    }

    return request("/favorites");
  },

  async getSavedTests() {
    if (USE_MOCK) {
      return [];
    }

    return request("/saved");
  },

  async register(userData) {
    return request("/register", {
      method: "POST",
      body: JSON.stringify(userData)
    });
  },

  async login(loginData) {
    return request("/login", {
      method: "POST",
      body: JSON.stringify(loginData)
    });
  }
};