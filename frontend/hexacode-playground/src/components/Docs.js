import React, { useState, useEffect } from 'react';
import { Layout, Typography, Card, Spin, Alert } from 'antd';
import { useParams } from 'react-router-dom';

const { Content } = Layout;
const { Title } = Typography;

const Docs = () => {
  const { docName } = useParams(); // Get the documentation name from the URL
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    // Fetch the documentation HTML
    fetch(`/docs/${docName}.html`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to load documentation');
        }
        return response.text();
      })
      .then((data) => {
        setContent(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, [docName]);

  return (
    <Layout style={{ padding: '20px' }}>
      <Content>
        <Title level={2} style={{ marginBottom: '20px' }}>{docName.replace('-', ' ').toUpperCase()}</Title>
        {loading ? (
          <Spin size="large" style={{ display: 'block', margin: '20px auto' }} />
        ) : error ? (
          <Alert message="Error" description={error} type="error" showIcon />
        ) : (
          <Card>
            {/* Render the fetched HTML content */}
            <div dangerouslySetInnerHTML={{ __html: content }} />
          </Card>
        )}
      </Content>
    </Layout>
  );
};

export default Docs;
