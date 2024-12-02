import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./Pages/HomePage";
import DoctoresPage from "./Pages/DoctoresPage";
import PacientesPage from "./Pages/PacientesPage";
import BookingsPage from "./Pages/BookingsPage";
import BookingsPageDetail from "./Pages/BookingsPageDetail";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/doctores" element={<DoctoresPage />} />
        <Route path="/pacientes" element={<PacientesPage />} />
        <Route path="/bookings" element={<BookingsPage />} />
        <Route path="/bookings/new" element={<BookingsPageDetail />} />
      </Routes>
    </Router>
  );
};

export default App;
