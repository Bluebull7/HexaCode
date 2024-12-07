import React from "react";
import { Layout, Typography, Button } from "antd";
import { Link } from "react-router-dom";

const { Content } = Layout;
const { Title, Paragraph } = Typography;

const Home = () => {
  return (
    <Layout style={{ minHeight: "100vh", backgroundColor: "#f0f2f5" }}>
      <Content style={{ padding: "20px" }}>
        <div
          style={{
            textAlign: "center",
            margin: "auto",
            padding: "40px",
            backgroundColor: "#fff",
            borderRadius: "8px",
            boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)",
          }}
        >
          <Title level={2}>Welcome to HexaCode</Title>
          <Paragraph>
            HexaCode is a custom French-based programming language designed for
            educational and creative purposes. Explore the playground to write
            and execute code, or dive into the documentation to learn more.
          </Paragraph>
          <div style={{ marginTop: "20px" }}>
            <Link to="/playground">
              <Button type="primary" style={{ marginRight: "10px" }}>
                Go to Playground
              </Button>
            </Link>
            <Link to="/docs">
              <Button type="default">View Documentation</Button>
            </Link>
          </div>
        </div>
      </Content>
    </Layout>
  );
};

export default Home;
