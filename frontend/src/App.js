import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./Pages/HomePage";
import DoctoresPage from "./Pages/DoctoresPage";
import PacientesPage from "./Pages/PacientesPage";
import BookingsPage from "./Pages/BookingsPage";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/doctores" element={<DoctoresPage />} />
        <Route path="/pacientes" element={<PacientesPage />} />
        <Route path="/bookings" element={<BookingsPage />} />
      </Routes>
    </Router>
  );
};

export default App;
