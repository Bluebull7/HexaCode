import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";
import { Layout, Button, Typography } from "antd";


const { Content } = Layout;
const { Title } = Typography;

const Docs = () => {
  const { docPage } = useParams(); // Capture the page name from the URL
  const navigate = useNavigate(); // For navigation
  const [htmlContent, setHtmlContent] = useState(""); // Store fetched HTML content
  const [error, setError] = useState(null); // Handle errors

  useEffect(() => {
    const fetchDocs = async () => {
      try {
        const page = docPage ? `${docPage}.html` : "index.html"; // Default to index.html
        const response = await axios.get(`http://localhost:5000/docs/${page}`);
        setHtmlContent(response.data); // Set the HTML content
      } catch (err) {
        setError("The requested documentation page could not be loaded.");
        console.error(err);
      }
    };

    fetchDocs();
  }, [docPage]);

  return (
    <Layout style={{ minHeight: "100vh", backgroundColor: "#f0f2f5" }}>
      <Content style={{ padding: "20px" }}>
        {error ? (
          <div style={{ textAlign: "center" }}>
            <Title level={3} style={{ color: "#ff4d4f" }}>
              Error
            </Title>
            <p>{error}</p>
            <Button onClick={() => navigate("/")}>Go Back to Home</Button>
          </div>
        ) : (
          <div
            dangerouslySetInnerHTML={{ __html: htmlContent }} // Render raw HTML
            style={{
              backgroundColor: "#fff",
              padding: "20px",
              borderRadius: "8px",
              boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)",
            }}
          ></div>
        )}
      </Content>
    </Layout>
  );
};

export default Docs;
