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

export default function Register() {
  const toast = useToast();
  const handleSubmit = e => {
    e.preventDefault();

    const username = e.target.username.value;
    const password = e.target.password.value;
    const phone = e.target.phone.value;

    axios
      .post(`${process.env.REACT_APP_API_URL}/register`, { username, password, phone })
      .then(res => {
        console.log(res.data);
        toast({ title: res.data.status });
      });
  };

  return (
    <Container mt="30vh">
      <Box bg="gray.900" p={10} borderRadius="3xl">
        <Text fontSize="4xl" mb={2}>
          註冊
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
          <FormControl isRequired mt={5}>
            <FormLabel htmlFor="phone">手機號碼</FormLabel>
            <Input id="phone" type="phone" />
          </FormControl>
          <Button mt={5} colorScheme="blue" type="submit" isFullWidth>
            註冊
          </Button>
        </form>
      </Box>
    </Container>
  );
}
