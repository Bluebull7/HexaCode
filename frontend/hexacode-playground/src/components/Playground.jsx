import React, { useState } from "react";
import { Layout, Row, Col } from "antd";
import Editor from "./Editor";
import Console from "./Console";

const { Content } = Layout;

const Playground = () => {
  const [script, setScript] = useState(""); // Code written in the editor
  const [output, setOutput] = useState(""); // Output from the backend

  const executeCode = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/execute", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ script }),
      });
      const data = await response.json();
      setOutput(data.output);
    } catch (error) {
      console.error(error);
      setOutput("An error occurred while executing the code.");
    }
  };

  return (
    <Layout style={{ minHeight: "100vh", backgroundColor: "#f0f2f5" }}>
      <Content style={{ padding: "20px" }}>
        <Row gutter={[16, 16]}>
          {/* Editor Section */}
          <Col xs={24} md={12}>
            <Editor script={script} setScript={setScript} executeCode={executeCode} />
          </Col>

          {/* Console Section */}
          <Col xs={24} md={12}>
            <Console output={output} />
          </Col>
        </Row>
      </Content>
    </Layout>
  );
};

export default Playground;
