import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { datasetAPI } from '../services/api';

function Dashboard({ user }) {
    const [datasets, setDatasets] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        fetchDatasets();
    }, []);

    const fetchDatasets = async () => {
        try {
            const response = await datasetAPI.list();
            setDatasets(response.data.results || response.data);
        } catch (err) {
            setError('Failed to load datasets');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
    };

    if (loading) {
        return (
            <div className="loading">
                <div className="spinner"></div>
            </div>
        );
    }

    return (
        <div className="dashboard">
            <div className="container">
                <div className="dashboard-header">
                    <h1 className="dashboard-title">Welcome, {user.username}!</h1>
                    <p className="dashboard-subtitle">
                        Manage and analyze your chemical equipment data
                    </p>
                </div>

                {error && <div className="alert alert-error">{error}</div>}

                <div className="stats-grid">
                    <div className="stat-card">
                        <div className="stat-value">{datasets.length}</div>
                        <div className="stat-label">Total Datasets</div>
                    </div>

                    <div className="stat-card" style={{ background: 'linear-gradient(135deg, #667eea, #764ba2)' }}>
                        <div className="stat-value">
                            {datasets.reduce((sum, d) => sum + d.total_count, 0)}
                        </div>
                        <div className="stat-label">Total Equipment</div>
                    </div>

                    <div className="stat-card" style={{ background: 'linear-gradient(135deg, #f093fb, #f5576c)' }}>
                        <div className="stat-value">
                            {datasets.length > 0 ?
                                (datasets.reduce((sum, d) => sum + d.avg_temperature, 0) / datasets.length).toFixed(1)
                                : '0'}°C
                        </div>
                        <div className="stat-label">Avg Temperature</div>
                    </div>
                </div>

                <div className="card">
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
                        <h2 style={{ fontSize: '24px', fontWeight: '600' }}>All Datasets</h2>
                        <Link to="/upload" className="btn btn-primary">
                            + Upload New Dataset
                        </Link>
                    </div>

                    {datasets.length === 0 ? (
                        <div style={{ textAlign: 'center', padding: '40px', color: 'var(--text-secondary)' }}>
                            <p style={{ fontSize: '18px', marginBottom: '20px' }}>No datasets yet</p>
                            <Link to="/upload" className="btn btn-primary">
                                Upload Your First Dataset
                            </Link>
                        </div>
                    ) : (
                        <div className="dataset-list">
                            {datasets.map((dataset) => (
                                <Link
                                    key={dataset.id}
                                    to={`/dataset/${dataset.id}`}
                                    style={{ textDecoration: 'none', color: 'inherit' }}
                                >
                                    <div className="dataset-card">
                                        <div className="dataset-header">
                                            <div>
                                                <div className="dataset-name">{dataset.name}</div>
                                                <div className="dataset-date">
                                                    Uploaded: {formatDate(dataset.uploaded_at)}
                                                </div>
                                            </div>
                                            <div style={{ fontSize: '32px' }}>📊</div>
                                        </div>

                                        <div className="dataset-stats">
                                            <div className="dataset-stat">
                                                <div className="dataset-stat-label">Equipment</div>
                                                <div className="dataset-stat-value">{dataset.total_count}</div>
                                            </div>

                                            <div className="dataset-stat">
                                                <div className="dataset-stat-label">Avg Flowrate</div>
                                                <div className="dataset-stat-value">{dataset.avg_flowrate.toFixed(1)}</div>
                                            </div>

                                            <div className="dataset-stat">
                                                <div className="dataset-stat-label">Avg Pressure</div>
                                                <div className="dataset-stat-value">{dataset.avg_pressure.toFixed(1)}</div>
                                            </div>

                                            <div className="dataset-stat">
                                                <div className="dataset-stat-label">Avg Temp</div>
                                                <div className="dataset-stat-value">{dataset.avg_temperature.toFixed(1)}°C</div>
                                            </div>
                                        </div>
                                    </div>
                                </Link>
                            ))}
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

export default Dashboard;
