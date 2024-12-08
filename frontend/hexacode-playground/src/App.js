import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link, Navigate } from 'react-router-dom';
import { Layout, Menu } from 'antd';
import Home from './components/Home';
import Docs from './components/Docs';
import Playground from './components/Playground';
import Sidebar from './components/Sidebar2';
import AppHeader from './components/Header';
import 'antd/dist/reset.css'; // For Ant Design styles

const { Content, Sider, Footer } = Layout;

const App = () => {
  return (
    <Router>
      <Layout style={{ minHeight: '100vh' }}>
        {/* Application Header */}
        <AppHeader />

        <Layout>
          {/* Sidebar for Documentation Navigation */}
          <Sider width={200} style={{ background: '#fff' }}>
            <Sidebar />
          </Sider>

          {/* Main Content Area */}
          <Content style={{ padding: '20px' }}>
            <Routes>
              {/* Home Route */}
              <Route path="/" element={<Home />} />

              {/* Playground Route */}
              <Route path="/playground" element={<Playground />} />

              {/* Documentation Route */}
              <Route path="/docs" element={<Docs />} />

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
