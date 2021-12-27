import { useColorMode } from "@chakra-ui/react";
import { useEffect, useState, createContext } from "react";
import { HashRouter, Route, Routes } from "react-router-dom";
import Index from "./Views/Index";
import Login from "./Views/Login";
import Register from "./Views/Register";

export const TokenContext = createContext();

export default function App() {
  const [token, setToken] = useState("");
  const { colorMode, toggleColorMode } = useColorMode();

  useEffect(() => {
    if (colorMode === "light") {
      toggleColorMode();
    }
  }, []);

  return (
    <TokenContext.Provider value={{ token: token, setToken: setToken }}>
      <HashRouter>
        <Routes>
          <Route path="/" element={<Index />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </HashRouter>
    </TokenContext.Provider>
  );
}
