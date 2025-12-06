import axios from 'axios';

// Usamos una instancia para configurar la URL base una sola vez
const api = axios.create({
    // En desarrollo local con Docker, el puerto suele ser 5000
    baseURL: 'http://localhost:5000/api',
    headers: {
        'Content-Type': 'application/json',
    }
});
// INTERCEPTOR: Se ejecuta antes de cada petición
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            // Si hay token, lo pegamos en el header Authorization
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default api;