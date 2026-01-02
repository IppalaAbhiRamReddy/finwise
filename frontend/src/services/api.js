/**
 * Central Axios instance with auth interceptors.
 */

import axios from "axios";
import { getAuthContext } from "./authHelper";

const api = axios.create({
  baseURL: "/api",
  withCredentials: true, // REQUIRED for refresh cookie
});

// Attach access token
api.interceptors.request.use((config) => {
  const { accessToken } = getAuthContext();
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }
  return config;
});

// Handle 401 silently
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (
      error.response?.status === 401 &&
      !originalRequest._retry
    ) {
      originalRequest._retry = true;

      try {
        const refreshResponse = await axios.post(
          "/api/auth/refresh/",
          {},
          { withCredentials: true }
        );

        const newAccessToken = refreshResponse.data.access;
        const { setAccessToken } = getAuthContext();
        setAccessToken(newAccessToken);

        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
        return api(originalRequest);
      } catch {
        window.location.href = "/login";
      }
    }

    return Promise.reject(error);
  }
);

export default api;
