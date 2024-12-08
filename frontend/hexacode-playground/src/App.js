import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Docs from "./components/Docs";
import Playground from "./components/Playground";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/playground" element={<Playground />} />
        <Route path="/docs/*" element={<Docs />} />
      </Routes>
    </Router>
  );
}

export default App;
