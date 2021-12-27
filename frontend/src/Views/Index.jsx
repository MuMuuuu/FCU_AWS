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
        <Link to="/login">
          <Button colorScheme="blue" size="lg" w="256px">
            登入
          </Button>
        </Link>
      </Stack>
      <Text>LoginState: {tokenManager.token|| "Not login"}</Text>
    </Container>
  );
}
