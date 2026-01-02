import api from "./api";
import posthog from "../analytics/posthog";

export const login = async (username, password) => {
  const response = await api.post("/auth/login/", {
    username,
    password,
  });

  posthog.capture("login_success");

  return response.data.access;
};

export const logout = async () => {
  await api.post("/auth/logout/");

  posthog.capture("logout");
};
