import React from "react";
import ReactDOM from "react-dom/client";
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Layout from "./navbar/Layout";
import Home from "./navbar/Home";
import Profile from "./navbar/Profile";


ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="profiles" element={<Profile />} />
      </Route>
    </Routes>
  </BrowserRouter>
);