import { Container, Text, Box, Divider } from "@chakra-ui/react";
import axios from "axios";
import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { TokenContext } from "../App";

export default function Profile() {
  const tokenManager = useContext(TokenContext);
  const navigate = useNavigate();
  const [data, setData] = useState({});

  useEffect(() => {
    if (!tokenManager.token) {
      navigate("/login");
    } else {
      axios
        .get(`${process.env.REACT_APP_API_URL}/profile`, {
          headers: {
            Authorization: `Bearer ${tokenManager.token}`,
          },
        })
        .then(res => {
          const locations = res.data.locations?.sort((a, b) => b.timestamp - a.timestamp);
          setData({ username: res.data.username, locations });
        });
    }
  }, [navigate, tokenManager.token]);

  return (
    <Container my="10vh">
      <Box bg="gray.900" p={10} borderRadius="3xl">
        <Text fontSize="4xl" mb={2}>
          {data.username} 的個人檔案
        </Text>
        <Divider my={3} />
        <Text>我的紀錄</Text>
        {data.locations?.map((location, index) => (
          <Box my={3} p={3} bg="gray.800" borderRadius="xl" key={index}>
            <Text fontSize="xl">{location.store}</Text>
            <Text>{new Date(location.timestamp * 1000).toLocaleString()}</Text>
          </Box>
        ))}
      </Box>
    </Container>
  );
}
