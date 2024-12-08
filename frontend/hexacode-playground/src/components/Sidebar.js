import React from 'react';
import { Menu } from 'antd';
import { Link } from 'react-router-dom';

const Sidebar = () => {
  return (
    <Menu mode="inline" style={{ height: '100%', borderRight: 0 }}>
      <Menu.Item key="introduction">
        <Link to="/docs/introduction">Introduction</Link>
      </Menu.Item>
      <Menu.Item key="getting-started">
        <Link to="/docs/getting-started">Getting Started</Link>
      </Menu.Item>
    </Menu>
  );
};

export default Sidebar;
