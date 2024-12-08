import React from 'react';
import { Layout } from 'antd';

const { Header } = Layout;

const AppHeader = () => (
  <Header style={{ background: '#001529', padding: '0 20px' }}>
    <h1 style={{ color: '#fff', margin: 0 }}>HexaCode Documentation</h1>
  </Header>
);

export default AppHeader;
