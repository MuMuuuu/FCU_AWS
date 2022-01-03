import { useColorMode } from "@chakra-ui/react";
import { useEffect, useState, createContext, useContext } from "react";
import { HashRouter, Route, Routes, useNavigate, Outlet } from "react-router-dom";
import Index from "./Views/Index";
import Login from "./Views/Login";
import Profile from "./Views/Profile";
import Register from "./Views/Register";
import History from "./Views/Store/History";
import QRcode from "./Views/Store/QRcode";

export const TokenContext = createContext();

export default function App() {
  const [token, setToken] = useState(null);
  const [userType, setUserType] = useState("user");
  const [username, setUsername] = useState("");
  const { colorMode, toggleColorMode } = useColorMode();

  const handleSetToken = token => {
    localStorage.setItem("token", token);
    const payloads = token.split(".");

    if (payloads.length === 3) {
      const payload = JSON.parse(atob(payloads[1]));

      if (payload.exp * 1000 < Date.now()) {
        localStorage.removeItem("token");
        token = "";
      } else {
        setUserType(payload.type);
        setUsername(payload.username);
      }
    }

    setToken(token);
  };

  useEffect(() => {
    let token = localStorage.getItem("token") || "";
    handleSetToken(token);
  }, []);

  useEffect(() => {
    if (colorMode === "light") {
      toggleColorMode();
    }
  }, [toggleColorMode, colorMode]);

  return (
    token !== null && (
      <TokenContext.Provider
        value={{ token: token, setToken: handleSetToken, userType: userType, username: username }}
      >
        <HashRouter>
          <Routes>
            <Route path="/" element={<Index />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/store" element={<StoreWrapper />}>
              <Route path="history" element={<History />} />
              <Route path="qrcode" element={<QRcode />} />
            </Route>
          </Routes>
        </HashRouter>
      </TokenContext.Provider>
    )
  );
}

const StoreWrapper = () => {
  const tokenManager = useContext(TokenContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (!tokenManager.token) {
      navigate("/login");
    } else if (tokenManager.userType !== "store") {
      navigate("/");
    }
  }, [tokenManager.token, tokenManager.userType, navigate]);

  return <Outlet />;
};
