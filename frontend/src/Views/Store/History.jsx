import { Container, Text, Box, Divider } from "@chakra-ui/react";
import axios from "axios";
import { useContext, useEffect, useState } from "react";
import { TokenContext } from "../../App";

export default function History() {
  const tokenManager = useContext(TokenContext);
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_API_URL}/store/${tokenManager.username}/history`, {
        headers: {
          Authorization: `Bearer ${tokenManager.token}`,
        },
      })
      .then(res => {
        setData(res.data);
      });
  }, [tokenManager.token, tokenManager.username]);

  return (
    <Container mt="30vh">
      <Box bg="gray.900" p={10} borderRadius="3xl">
        <Text fontSize="4xl" mb={2}>
          {tokenManager.username} 的歷史紀錄
        </Text>
        <Divider my={3} />
        {data?.map((history, index) => (
          <Box my={3} p={3} bg="gray.800" borderRadius="xl" key={index}>
            <Text fontSize="xl">{history.username}</Text>
            <Text>{new Date(history.timestamp * 1000).toLocaleString()}</Text>
          </Box>
        ))}
      </Box>
    </Container>
  );
}
