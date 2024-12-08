import React, { useState } from 'react';
import { Typography, Input, Button, Alert, Card } from 'antd';

const { Title } = Typography;
const { TextArea } = Input;

const Playground = () => {
  const [script, setScript] = useState('');
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');

  const executeScript = () => {
    fetch('/api/execute', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ script }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          setError(data.error);
          setOutput('');
        } else {
          setOutput(data.output);
          setError('');
        }
      })
      .catch(() => setError('Failed to execute script.'));
  };

  return (
    <div style={{ padding: '20px' }}>
      <Title level={1}>HexaCode Playground</Title>
      <TextArea
        placeholder="Write your HexaCode script here..."
        value={script}
        onChange={(e) => setScript(e.target.value)}
        rows={10}
      />
      <Button type="primary" style={{ marginTop: '10px' }} onClick={executeScript}>
        Run
      </Button>
      {error && (
        <Alert
          message="Error"
          description={error}
          type="error"
          showIcon
          style={{ marginTop: '20px' }}
        />
      )}
      {output && (
        <Card title="Output" style={{ marginTop: '20px' }}>
          <pre>{output}</pre>
        </Card>
      )}
    </div>
  );
};

export default Playground;
