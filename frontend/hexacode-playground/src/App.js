import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { Layout, Menu } from 'antd';
import Home from './components/Home';
import Docs from './components/Docs';
import Playground from './components/Playground';
import 'antd/dist/reset.css'; // For Ant Design styles

const { Header, Content, Footer } = Layout;

const App = () => {
  return (
    <Router>
      <Layout style={{ minHeight: '100vh' }}>
        <Header>
          <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['home']}>
            <Menu.Item key="home">
              <Link to="/">Home</Link>
            </Menu.Item>
            <Menu.Item key="docs">
              <Link to="/docs">Docs</Link>
            </Menu.Item>
            <Menu.Item key="playground">
              <Link to="/playground">Playground</Link>
            </Menu.Item>
          </Menu>
        </Header>
        <Content style={{ padding: '20px' }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/docs" element={<Docs />} />
            <Route path="/playground" element={<Playground />} />
          </Routes>
        </Content>
        <Footer style={{ textAlign: 'center' }}>HexaCode ©2024</Footer>
      </Layout>
    </Router>
  );
};

export default App;
