import React from "react";
import { Card, Input, Button } from "antd";
import { PlayCircleOutlined } from "@ant-design/icons";

const { TextArea } = Input;

const Editor = ({ script, setScript, executeCode }) => {
  return (
    <Card
      title="Editor"
      bordered={false}
      bodyStyle={{ display: "flex", flexDirection: "column", height: "100%" }}
      style={{ boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)" }}
    >
      <TextArea
        value={script}
        onChange={(e) => setScript(e.target.value)}
        rows={15}
        placeholder="// Write your HexaCode here..."
        style={{ flex: 1, borderRadius: "8px" }}
      />
      <Button
        type="primary"
        style={{ marginTop: "10px", width: "100%", borderRadius: "8px" }}
        onClick={executeCode}
        icon={<PlayCircleOutlined />}
      >
        Run Code
      </Button>
    </Card>
  );
};

export default Editor;
