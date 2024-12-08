import React, { useState, useEffect } from 'react';
import { Typography, Card, Spin, Alert } from 'antd';

const { Title, Paragraph } = Typography;

const Docs = () => {
  const [docs, setDocs] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch('/api/docs/index.html') // Adjust the endpoint as needed
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch documentation');
        }
        return response.text();
      })
      .then((data) => {
        setDocs(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <Spin size="large" style={{ display: 'block', margin: '20px auto' }} />;
  }

  return (
    <div style={{ padding: '20px' }}>
      <Title level={1}>Documentation</Title>
      {error ? (
        <Alert message="Error" description={error} type="error" showIcon />
      ) : (
        <Card>
          <div dangerouslySetInnerHTML={{ __html: docs }} />
        </Card>
      )}
    </div>
  );
};

export default Docs;
