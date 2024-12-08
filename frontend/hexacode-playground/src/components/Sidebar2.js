import React from 'react';
import { Menu } from 'antd';
import { Link } from 'react-router-dom';

const Sidebar2 = () => {
  return (
    <Menu mode="inline" style={{ height: '100%' }}>
      <Menu.Item key="introduction">
        <Link to="/introduction.html">Introduction</Link>
      </Menu.Item>
      <Menu.Item key="getting-started">
        <Link to="/DOCS.html">Getting Started</Link>
      </Menu.Item>
      <Menu.Item key="api">
        <Link to="/api-reference.html">API Reference</Link>
      </Menu.Item>
    </Menu>
  );
};

export default Sidebar2;
