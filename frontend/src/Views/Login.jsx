import {
  Container,
  Text,
  FormControl,
  FormLabel,
  Input,
  Box,
  Button,
  Divider,
  useToast,
} from "@chakra-ui/react";
import axios from "axios";
import { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { TokenContext } from "../App";

export default function Login() {
  const toast = useToast();
  const tokenManager = useContext(TokenContext);
  const navigate = useNavigate();

  const handleSubmit = e => {
    e.preventDefault();
    console.log(e);

    const username = e.target.username.value;
    const password = e.target.password.value;

    axios.post(`${process.env.REACT_APP_API_URL}/login`, { username, password }).then(res => {
      console.log(res.data);
      toast({ title: res.data.status });
      if (res.data.token) {
        tokenManager.setToken(res.data.token);
        navigate("/");
      }
    });
  };

  return (
    <Container mt="30vh">
      <Box bg="gray.900" p={10} borderRadius="3xl">
        <Text fontSize="4xl" mb={2}>
          登入
        </Text>
        <Divider />
        <form onSubmit={handleSubmit}>
          <FormControl isRequired mt={5}>
            <FormLabel htmlFor="username">帳號</FormLabel>
            <Input id="username" type="username" />
          </FormControl>
          <FormControl isRequired mt={5}>
            <FormLabel htmlFor="password">密碼</FormLabel>
            <Input id="password" type="password" />
          </FormControl>
          <Button mt={5} colorScheme="blue" type="submit" isFullWidth>
            登入
          </Button>
          <Link to="/register">
            <Button mt={5} isFullWidth>
              註冊
            </Button>
          </Link>
        </form>
      </Box>
    </Container>
  );
}
