// frontend/src/services/api.js
import axios from 'axios';

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL, // Asegúrate que esta variable coincida con tu .env
});

// Interceptor para logs (opcional, pero útil para depurar)
API.interceptors.request.use(request => {
    console.log('Starting Request', JSON.stringify(request.data, null, 2));
    return request;
});

API.interceptors.response.use(response => {
    console.log('Response:', JSON.stringify(response.data, null, 2));
    return response;
}, error => {
    console.error('API Error:', error.response ? error.response.data : error.message);
    return Promise.reject(error);
});


export const crearProducto = (data) => {
  // Axios automáticamente detecta FormData y establece el Content-Type adecuado
  // No necesitas el header 'Content-Type': 'multipart/form-data' aquí si 'data' es un FormData.
  // Si 'data' es un objeto JSON y no una imagen, necesitarías 'application/json'.
  return API.post('/productos/', data);
};

export const listarProductos = () =>
  API.get('/productos/');
