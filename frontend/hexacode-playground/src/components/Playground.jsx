import React, { useState } from "react";
import { Layout, Row, Col, Card, Input, Button } from "antd";
import axios from "axios";

const { TextArea } = Input;
const { Content } = Layout;

const Playground = () => {
  const [script, setScript] = useState("");
  const [output, setOutput] = useState("");

  const executeCode = async () => {
    try {
      const response = await axios.post("http://localhost:5000/api/execute", {
        script,
      });
      setOutput(response.data.output);
    } catch (error) {
      console.error(error);
      setOutput(error.response?.data?.error || "An error occurred.");
    }
  };

  return (
    <Layout style={{ minHeight: "100vh", backgroundColor: "#f0f2f5" }}>
      <Content style={{ padding: "20px" }}>
        <Row gutter={[16, 16]}>
          {/* Editor */}
          <Col xs={24} md={12}>
            <Card
              title="Editor"
              style={{
                boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)",
                borderRadius: "8px",
              }}
            >
              <TextArea
                value={script}
                onChange={(e) => setScript(e.target.value)}
                rows={15}
                placeholder="// Write your HexaCode here..."
              />
              <Button
                type="primary"
                style={{ marginTop: "10px", width: "100%" }}
                onClick={executeCode}
              >
                Run Code
              </Button>
            </Card>
          </Col>

          {/* Console */}
          <Col xs={24} md={12}>
            <Card
              title="Console"
              style={{
                boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)",
                borderRadius: "8px",
              }}
            >
              <pre
                style={{
                  whiteSpace: "pre-wrap",
                  backgroundColor: "#f6f6f6",
                  padding: "10px",
                  borderRadius: "8px",
                  fontFamily: "Courier, monospace",
                  color: "#333",
                  minHeight: "230px",
                  overflowY: "auto",
                }}
              >
                {output}
              </pre>
            </Card>
          </Col>
        </Row>
      </Content>
    </Layout>
  );
};

export default Playground;
