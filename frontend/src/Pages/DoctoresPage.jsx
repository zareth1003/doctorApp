import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import "./DoctoresPage.css";
import { getDoctores } from "../services/api";

const DoctoresPage = () => {
  const [doctores, setDoctores] = useState([]);

  useEffect(() => {
    // Llama a la API al cargar el componente.
    getDoctores()
      .then(setDoctores)
      .catch((error) => {
        console.error("Error al cargar los doctores:", error);
      });
  }, []);

  return (
    <div>
      <Navbar />
      <main className="doctores">
        <h1>Doctores Disponibles</h1>
        <ul>
          {doctores.map((Doctor) => (
            <li key={Doctor.id}>
              <h2>
                {Doctor.first_name} {Doctor.last_name}
              </h2>
              <p>{Doctor.qualification}</p>
              <p>Contacto: {Doctor.contact_number}</p>
              <p>Correo: {Doctor.email}</p>
            </li>
          ))}
        </ul>
      </main>
      <Footer />
    </div>
  );
};

export default DoctoresPage;
