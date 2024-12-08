import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate, Link } from 'react-router-dom';
import { Layout, Menu } from 'antd';
import Home from './components/Home';
import Docs from './components/Docs';
import Playground from './components/Playground';
import Sidebar from './components/Sidebar2';
import AppHeader from './components/Header';
import 'antd/dist/reset.css'; // Ant Design styles

const { Header, Content, Sider, Footer } = Layout;

const App = () => {
  return (
    <Router>
      <Layout style={{ minHeight: '100vh' }}>
        {/* Header Navigation */}
        <Header>
          <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['home']}>
            <Menu.Item key="home">
              <Link to="/">Home</Link>
            </Menu.Item>
            <Menu.Item key="playground">
              <Link to="/playground">Playground</Link>
            </Menu.Item>
            <Menu.Item key="docs">
              <a href="/introduction.html" target="_blank" rel="noopener noreferrer">
                Documentation
              </a>
            </Menu.Item>
          </Menu>
        </Header>

        <Layout>
          {/* Sidebar for Documentation Navigation */}
          <Sider width={200} style={{ background: '#fff' }}>
            <Sidebar />
          </Sider>

          {/* Main Content */}
          <Content style={{ padding: '20px' }}>
            <Routes>
              {/* Home Route */}
              <Route path="/" element={<Home />} />

              {/* Playground Route */}
              <Route path="/playground" element={<Playground />} />

              {/* Redirect Invalid Routes */}
              <Route path="*" element={<Navigate to="/" />} />
            </Routes>
          </Content>
        </Layout>

        {/* Footer */}
        <Footer style={{ textAlign: 'center' }}>HexaCode ©2024</Footer>
      </Layout>
    </Router>
  );
};

export default App;
