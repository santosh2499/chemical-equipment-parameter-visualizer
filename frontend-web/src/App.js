import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import './App.css';
import Login from './components/Login';
import Register from './components/Register';
import Dashboard from './components/Dashboard';
import DatasetDetail from './components/DatasetDetail';
import Upload from './components/Upload';
import Navbar from './components/Navbar';
import { authAPI } from './services/api';

function App() {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        checkAuth();
    }, []);

    const checkAuth = async () => {
        try {
            const response = await authAPI.getCurrentUser();
            setUser(response.data);
        } catch (error) {
            setUser(null);
        } finally {
            setLoading(false);
        }
    };

    const handleLogin = (userData) => {
        setUser(userData);
    };

    const handleLogout = async () => {
        try {
            await authAPI.logout();
            setUser(null);
        } catch (error) {
            console.error('Logout error:', error);
        }
    };

    if (loading) {
        return (
            <div className="loading">
                <div className="spinner"></div>
            </div>
        );
    }

    return (
        <Router>
            <div className="App">
                {user && <Navbar user={user} onLogout={handleLogout} />}

                <Routes>
                    <Route
                        path="/login"
                        element={user ? <Navigate to="/" /> : <Login onLogin={handleLogin} />}
                    />
                    <Route
                        path="/register"
                        element={user ? <Navigate to="/" /> : <Register onRegister={handleLogin} />}
                    />
                    <Route
                        path="/"
                        element={user ? <Dashboard user={user} /> : <Navigate to="/login" />}
                    />
                    <Route
                        path="/upload"
                        element={user ? <Upload /> : <Navigate to="/login" />}
                    />
                    <Route
                        path="/dataset/:id"
                        element={user ? <DatasetDetail /> : <Navigate to="/login" />}
                    />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
