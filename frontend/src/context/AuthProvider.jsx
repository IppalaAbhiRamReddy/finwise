import { useState } from "react";
import { AuthContext } from "./AuthContext";
import { setAuthContext } from "../services/authHelper";

export function AuthProvider({ children }) {
  const [accessToken, setAccessToken] = useState(null);

  setAuthContext({ accessToken, setAccessToken });

  return (
    <AuthContext.Provider value={{ accessToken, setAccessToken }}>
      {children}
    </AuthContext.Provider>
  );
}
