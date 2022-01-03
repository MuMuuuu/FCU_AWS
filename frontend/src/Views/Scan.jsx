import { Container, Center, Box, useToast } from "@chakra-ui/react";
import axios from "axios";
import { useContext, useState } from "react";
import QrReader from "react-qr-reader";
import { TokenContext } from "../App";
import { useNavigate } from "react-router-dom";

export default function Scan() {
  const tokenManager = useContext(TokenContext);
  const [current, setCurrent] = useState(null);
  const navigate = useNavigate();
  const toast = useToast();

  const handleScan = data => {
    if (data !== current) {
      try {
        const payload = JSON.parse(data);
        report(payload.store);
      } catch (e) {
        console.log(e);
      } finally {
        setCurrent(data);
      }
    }
  };

  const report = store => {
    axios
      .post(`${process.env.REACT_APP_API_URL}/store/${store}/report`, null, {
        headers: {
          Authorization: `Bearer ${tokenManager.token}`,
        },
      })
      .then(res => {
        toast({ title: "掃描成功", status: "success" });
        console.log(res);
        navigate("/");
      });
  };

  return (
    <Container mt="10vh">
      <QrReader showViewFinder={false} onScan={handleScan} onError={err => console.log(err)} />
    </Container>
  );
}
