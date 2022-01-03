import { Container, Text, Image, Center } from "@chakra-ui/react";
import axios from "axios";
import { useContext, useEffect, useState } from "react";
import { TokenContext } from "../../App";

export default function QRcode() {
  const tokenManager = useContext(TokenContext);
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_API_URL}/store/${tokenManager.username}/qrcode`, {
        headers: {
          Authorization: `Bearer ${tokenManager.token}`,
        },
      })
      .then(res => {
        setData(res.data);
      });
  }, [tokenManager.token, tokenManager.username]);

  return (
    <Container mt="10vh" textAlign="center">
      <Text fontSize="4xl" mb={2}>
        {tokenManager.username}
      </Text>
      <Center bg="gray.900" p={10} borderRadius="3xl">
        <Image src={data} boxSize="100%" />
      </Center>
    </Container>
  );
}
