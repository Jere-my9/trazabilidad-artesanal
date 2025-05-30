import axios from 'axios';

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export const crearProducto = (data) =>
  API.post('/productos/', data, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });

export const listarProductos = () =>
  API.get('/productos/');
