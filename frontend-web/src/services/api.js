import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Configure axios defaults
axios.defaults.withCredentials = true;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const api = axios.create({
    baseURL: `${API_URL}/api`,
    withCredentials: true,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Authentication
export const authAPI = {
    register: (data) => api.post('/auth/register/', data),
    login: (data) => api.post('/auth/login/', data),
    logout: () => api.post('/auth/logout/'),
    getCurrentUser: () => api.get('/auth/user/'),
};

// Datasets
export const datasetAPI = {
    list: () => api.get('/datasets/'),
    get: (id) => api.get(`/datasets/${id}/`),
    upload: (formData) => {
        return api.post('/datasets/upload/', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
    },
    getSummary: (id) => api.get(`/datasets/${id}/summary/`),
    downloadReport: (id) => {
        return api.get(`/datasets/${id}/report/`, {
            responseType: 'blob',
        });
    },
    delete: (id) => api.delete(`/datasets/${id}/`),
};

export default api;
