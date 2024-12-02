import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import "./PacientesPage.css";
import { getPacientes } from "../services/api";

const PacientesPage = () => {
  const [pacientes, setPacientes] = useState([]);

  useEffect(() => {
    // Llama a la API al cargar el componente.
    getPacientes()
      .then(setPacientes)
      .catch((error) => {
        console.error("Error al cargar los doctores:", error);
      });
  }, []);

  return (
    <div>
      <Navbar />
      <main className="pacientes">
        <h1>Gestión de Pacientes</h1>
        <p>Administra la información de los pacientes aquí.</p>
        <ul>
          {pacientes.map((Patient) => (
            <li key={Patient.id}>
              <h2>
                {Patient.first_name} {Patient.last_name}
              </h2>
              <p>{Patient.qualification}</p>
              <p>Contacto: {Patient.contact_number}</p>
              <p>Correo: {Patient.email}</p>
            </li>
          ))}
        </ul>
      </main>
      <Footer />
    </div>
  );
};

export default PacientesPage;
