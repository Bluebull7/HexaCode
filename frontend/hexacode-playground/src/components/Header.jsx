import React from "react";
import { Menu, Layout } from "antd";
import { HomeOutlined, FileTextOutlined } from "@ant-design/icons";

const { Header } = Layout;

const NavBar = ({ activeMenu, setActiveMenu, navigateToDocs }) => {
  return (
    <Header style={{ backgroundColor: "#001529", padding: "0" }}>
      <Menu
        theme="dark"
        mode="horizontal"
        selectedKeys={[activeMenu]}
        style={{ display: "flex", justifyContent: "space-between" }}
      >
        <Menu.Item
          key="home"
          icon={<HomeOutlined />}
          onClick={() => setActiveMenu("home")}
        >
          HexaCode Playground
        </Menu.Item>
        <Menu.Item
          key="docs"
          icon={<FileTextOutlined />}
          onClick={navigateToDocs}
        >
          Documentation
        </Menu.Item>
      </Menu>
    </Header>
  );
};

export default NavBar;
