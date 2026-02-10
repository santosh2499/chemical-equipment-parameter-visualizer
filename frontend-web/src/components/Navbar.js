import React from 'react';
import { Link } from 'react-router-dom';

function Navbar({ user, onLogout }) {
    return (
        <nav className="navbar">
            <div className="navbar-content">
                <Link to="/" className="navbar-brand">
                    🧪 Equipment Visualizer
                </Link>

                <div className="navbar-menu">
                    <Link to="/" className="navbar-link">Dashboard</Link>
                    <Link to="/upload" className="navbar-link">Upload</Link>

                    {user && (
                        <>
                            <span className="navbar-user">👤 {user.username}</span>
                            <button onClick={onLogout} className="navbar-logout">
                                Logout
                            </button>
                        </>
                    )}
                </div>
            </div>
        </nav>
    );
}

export default Navbar;
