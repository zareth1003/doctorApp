import React from "react";
import "./Navbar.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-brand">DoctorApp</div>
      <ul className="navbar-links">
        <li>
          <a href="/">Inicio</a>
        </li>
        <li>
          <a href="/doctores">Doctores</a>
        </li>
        <li>
          <a href="/pacientes">Pacientes</a>
        </li>
        <li>
          <a href="/bookings">Citas</a>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
