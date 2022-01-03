import { Button, Container, Stack, Text } from "@chakra-ui/react";
import { useContext } from "react";
import { Link } from "react-router-dom";
import { TokenContext } from "../App";

export default function Index() {
  const tokenManager = useContext(TokenContext);

  return (
    <Container mt="30vh" centerContent>
      <Text fontSize={{ base: "4xl", md: "6xl" }}>台灣社交距離 2.0</Text>
      <Stack mt="62px">
        {tokenManager.token && tokenManager.userType === "user" && (
          <>
            <Link to="/scan">
              <Button colorScheme="blue" size="lg" w="256px">
                掃描
              </Button>
            </Link>
            <Link to="/profile">
              <Button colorScheme="blue" size="lg" w="256px">
                個人檔案
              </Button>
            </Link>
          </>
        )}

        {tokenManager.token && tokenManager.userType === "store" && (
          <>
            <Link to="/store/qrcode">
              <Button colorScheme="blue" size="lg" w="256px">
                QR Code
              </Button>
            </Link>
            <Link to="/store/history">
              <Button colorScheme="blue" size="lg" w="256px">
                歷史紀錄
              </Button>
            </Link>
          </>
        )}

        {tokenManager.token ? (
          <Button colorScheme="red" size="lg" w="256px" onClick={() => tokenManager.setToken("")}>
            登出
          </Button>
        ) : (
          <Link to="/login">
            <Button colorScheme="blue" size="lg" w="256px">
              登入
            </Button>
          </Link>
        )}
      </Stack>
    </Container>
  );
}
