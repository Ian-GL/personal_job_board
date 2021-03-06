import React from "react";
import { createRoot } from 'react-dom/client';
import "./index.css";
import App from "./App";

// importing css stylesheet to use the bootstrap class
// add this line only in this file
import "bootstrap/dist/css/bootstrap.min.css";

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App tab="home" />);
