import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Layout } from 'antd';
import Home from './components/Home';
import Docs from './components/Docs';
import Playground from './components/Playground';
import Sidebar from './components/Sidebar';
import AppHeader from './components/Header';
import 'antd/dist/reset.css'; // For Ant Design styles

const { Content, Sider, Footer } = Layout;

const App = () => {
  return (
    <Router>
      <Layout style={{ minHeight: '100vh' }}>
        {/* Header Component */}
        <AppHeader />

        <Layout>
          {/* Sidebar Component */}
          <Sider width={200} style={{ background: '#fff' }}>
            <Sidebar />
          </Sider>

          {/* Main Content */}
          <Content style={{ padding: '20px' }}>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/docs/:docName" element={<Docs />} />
              <Route path="/playground" element={<Playground />} />
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
