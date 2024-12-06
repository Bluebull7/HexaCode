import React from "react";
import { Card } from "antd";

const Console = ({ output }) => {
  return (
    <Card
      title="Console"
      bordered={false}
      bodyStyle={{ display: "flex", flexDirection: "column", height: "100%" }}
      style={{ boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)" }}
    >
      <pre
        style={{
          minHeight: "230px",
          whiteSpace: "pre-wrap",
          backgroundColor: "#f6f6f6",
          padding: "10px",
          borderRadius: "8px",
          fontFamily: "Courier, monospace",
          color: "#333",
          overflowY: "auto",
          flex: 1,
        }}
      >
        {output}
      </pre>
    </Card>
  );
};

export default Console;
