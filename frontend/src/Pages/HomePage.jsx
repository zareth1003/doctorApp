import React from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import "./HomePage.css";

const HomePage = () => {
  return (
    <div>
      <Navbar />
      <main className="home">
        <h1>Bienvenido a DoctorApp</h1>
        <p>Gestiona tus citas médicas de manera sencilla.</p>
      </main>
      <Footer />
    </div>
  );
};

export default HomePage;
