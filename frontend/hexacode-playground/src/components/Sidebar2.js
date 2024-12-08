import React from 'react';
import { Menu } from 'antd';

const Sidebar2 = () => {
  return (
    <Menu mode="inline" style={{ height: '100%' }}>
      <Menu.Item key="introduction">
        <a href="/introduction.html" target="_blank" rel="noopener noreferrer">
          Introduction
        </a>
      </Menu.Item>
      <Menu.Item key="getting-started">
        <a href="/usage.html" target="_blank" rel="noopener noreferrer">
          Getting Started
        </a>
      </Menu.Item>
      <Menu.Item key="api">
        <a href="/api-reference.html" target="_blank" rel="noopener noreferrer">
          API Reference
        </a>
      </Menu.Item>
    </Menu>
  );
};

export default Sidebar2;
