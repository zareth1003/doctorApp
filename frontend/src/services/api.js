import axios from "axios";

const API_BASE = "http://localhost:8000/api"; // Ajusta según tu configuración

export const getDoctores = async () => {
  const response = await axios.get(`${API_BASE}/doctors/`);
  return response.data;
};

export const getPacientes = async () => {
  const response = await axios.get(`${API_BASE}/patients/`);
  return response.data;
};

export const getDisponibilidad = async () => {
  const response = await axios.get(`${API_BASE}/appointments/`);
  return response.data;
};

export const getCitas = async () => {
  const response = await axios.get(`${API_BASE}/appointments/`);
  return response.data;
};
export const reservarCita = async (data) => {
  const response = await axios.post(`${API_BASE}/appointments/`, data);
  return response.data;
};

export const actualizarCita = async (id, data) => {
  const response = await axios.patch(`${API_BASE}/appointments/${id}/`, data);
  return response.data;
};
