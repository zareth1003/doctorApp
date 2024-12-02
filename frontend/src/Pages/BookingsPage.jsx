import React, { useState, useEffect } from "react";
import { getDoctores, getPacientes, reservarCita } from "../services/api";
import "./BookingsPage.css";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

const BookingsPage = ({ fetchAppointments }) => {
  const [formData, setFormData] = useState({
    appointment_date: "",
    appointment_time: "",
    doctor: "",
    patient: "",
    notes: "",
    status: "confirmar",
  });
  const [doctores, setDoctores] = useState([]);
  const [pacientes, setPacientes] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        getDoctores()
          .then(setDoctores)
          .catch((error) => {
            console.error("Error al cargar los doctores:", error);
          });
        getPacientes()
          .then(setPacientes)
          .catch((error) => {
            console.error("Error al cargar los doctores:", error);
          });
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await reservarCita(formData);
      // fetchAppointments();
      setFormData({
        appointment_date: "",
        appointment_time: "",
        doctor: "",
        patient: "",
        notes: "",
        status: "confirmar",
      });
    } catch (error) {
      console.error("Error creating appointment:", error);
    }
  };

  return (
    <div>
      <Navbar />
      <form onSubmit={handleSubmit}>
        <div>
          <label>Fecha:</label>
          <input
            type="date"
            name="appointment_date"
            value={formData.appointment_date}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Hora:</label>
          <input
            type="time"
            name="appointment_time"
            value={formData.appointment_time}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Doctor:</label>
          <select
            name="doctor"
            value={formData.doctor}
            onChange={handleChange}
            required
          >
            <option value="">Select a doctor</option>
            {doctores.map((Doctor) => (
              <option key={Doctor.id} value={Doctor.id}>
                {Doctor.first_name} {Doctor.last_name}
              </option>
            ))}
          </select>
        </div>
        <div>
          <label>Paciente:</label>
          <select
            name="patient"
            value={formData.patient}
            onChange={handleChange}
            required
          >
            <option value="">Select a patient</option>
            {pacientes.map((patient) => (
              <option key={patient.id} value={patient.id}>
                {patient.first_name} {patient.last_name}
              </option>
            ))}
          </select>
        </div>
        <div>
          <label>Motivo:</label>
          <textarea
            name="notes"
            value={formData.notes}
            onChange={handleChange}
          ></textarea>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default BookingsPage;
