import axios from 'axios';

// Usamos una instancia para configurar la URL base una sola vez
const api = axios.create({
    // En desarrollo local con Docker, el puerto suele ser 5000
    baseURL: 'http://localhost:5000/api',
    headers: {
        'Content-Type': 'application/json',
    }
});

export default api;