import React from 'react';
import { Typography, Menu } from 'antd';
import { Link } from 'react-router-dom';

const { Title, Paragraph } = Typography;

const Home = () => {
  return (
    <div style={{ padding: '20px' }}>
      <Title level={1}>Welcome to HexaCode</Title>
      <Paragraph>Explore our API, documentation, and playground.</Paragraph>
      <Menu mode="horizontal">
        <Menu.Item key="docs">
          <Link to="/introduction.html">Documentation</Link>
        </Menu.Item>
        <Menu.Item key="playground">
          <Link to="/playground">Playground</Link>
        </Menu.Item>
      </Menu>
    </div>
  );
};

export default Home;
