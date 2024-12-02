import React, { useState } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { reservarCita } from "../services/api";

const BookingsPage = () => {
  const [formData, setFormData] = useState({
    paciente_id: "",
    doctor_id: "",
    fecha: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    reservarCita(formData)
      .then((data) => {
        alert("Cita reservada con éxito");
        console.log(data);
      })
      .catch((error) => {
        console.error("Error al reservar cita:", error);
      });
  };

  return (
    <div>
      <Navbar />
      <h1>Reservar Cita</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="paciente_id"
          placeholder="ID del Paciente"
          value={formData.paciente_id}
          onChange={handleChange}
        />
        <input
          type="text"
          name="doctor_id"
          placeholder="ID del Doctor"
          value={formData.doctor_id}
          onChange={handleChange}
        />
        <input
          type="date"
          name="fecha"
          value={formData.fecha}
          onChange={handleChange}
        />
        <button type="submit">Reservar</button>
      </form>
      <Footer />
    </div>
  );
};

export default BookingsPage;
