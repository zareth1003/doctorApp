import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { actualizarCita, getCitas } from "../services/api";
import "./BookingsPage.css";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

const BookingsPage = () => {
  const [bookings, setBookings] = useState([]);
  const navigate = useNavigate();

  // Cargar la lista de reservas al montar el componente
  useEffect(() => {
    fetchBookings();
  }, []);

  const fetchBookings = async () => {
    try {
      const response = await getCitas();
      setBookings(response);
    } catch (error) {
      console.error("Error fetching bookings:", error);
    }
  };

  const handleCancel = async (id) => {
    try {
      var data = {
        status: "Cancelado",
      };
      await actualizarCita(id, data);
      fetchBookings();
    } catch (error) {
      console.error("Error canceling booking:", error);
    }
  };

  const handleCreate = () => {
    navigate("/bookings/new"); // Redirige al formulario de creación
  };

  return (
    <div>
      <Navbar />
      <main className="bookingList">
        <h1>Citas</h1>
        <button onClick={handleCreate}>Crear nueva cita</button>
        {bookings.length === 0 ? (
          <p>No bookings available.</p>
        ) : (
          <table>
            <thead>
              <tr>
                <th>Date</th>
                <th>Time</th>
                <th>Doctor</th>
                <th>Patient</th>
                <th>Status</th>
                <th>Reason</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {bookings.map((booking) => (
                <tr key={booking.id}>
                  <td>{booking.appointment_date}</td>
                  <td>{booking.appointment_time}</td>
                  <td>{booking.doctor_name}</td>
                  <td>{booking.patient_name}</td>
                  <td>{booking.status}</td>
                  <td>{booking.notes}</td>
                  <td>
                    <button onClick={() => handleCancel(booking.id)}>
                      Cancel
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </main>
      <Footer />
    </div>
  );
};

export default BookingsPage;
