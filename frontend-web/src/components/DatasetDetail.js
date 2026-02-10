import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { datasetAPI } from '../services/api';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    LineElement,
    PointElement,
    Title,
    Tooltip,
    Legend,
    ArcElement,
} from 'chart.js';
import { Bar, Pie } from 'react-chartjs-2';

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    LineElement,
    PointElement,
    ArcElement,
    Title,
    Tooltip,
    Legend
);

function DatasetDetail() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [dataset, setDataset] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const [downloading, setDownloading] = useState(false);

    useEffect(() => {
        const fetchDataset = async () => {
            try {
                const response = await datasetAPI.get(id);
                setDataset(response.data);
            } catch (err) {
                setError('Failed to load dataset');
                console.error(err);
            } finally {
                setLoading(false);
            }
        };
        fetchDataset();
    }, [id]);

    const handleDownloadReport = async () => {
        setDownloading(true);
        try {
            const response = await datasetAPI.downloadReport(id);
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', `equipment_report_${id}.pdf`);
            document.body.appendChild(link);
            link.click();
            link.remove();
        } catch (err) {
            alert('Failed to download report');
            console.error(err);
        } finally {
            setDownloading(false);
        }
    };

    if (loading) {
        return (
            <div className="loading">
                <div className="spinner"></div>
            </div>
        );
    }

    if (error || !dataset) {
        return (
            <div className="container" style={{ paddingTop: '40px' }}>
                <div className="alert alert-error">{error || 'Dataset not found'}</div>
                <button onClick={() => navigate('/')} className="btn btn-primary">
                    Back to Dashboard
                </button>
            </div>
        );
    }

    // Prepare chart data
    const typeDistributionData = {
        labels: Object.keys(dataset.equipment_types),
        datasets: [
            {
                label: 'Equipment Count',
                data: Object.values(dataset.equipment_types),
                backgroundColor: [
                    'rgba(63, 81, 181, 0.8)',
                    'rgba(102, 126, 234, 0.8)',
                    'rgba(255, 64, 129, 0.8)',
                    'rgba(76, 175, 80, 0.8)',
                    'rgba(255, 152, 0, 0.8)',
                    'rgba(156, 39, 176, 0.8)',
                    'rgba(0, 188, 212, 0.8)',
                    'rgba(255, 235, 59, 0.8)',
                ],
                borderColor: [
                    'rgba(63, 81, 181, 1)',
                    'rgba(102, 126, 234, 1)',
                    'rgba(255, 64, 129, 1)',
                    'rgba(76, 175, 80, 1)',
                    'rgba(255, 152, 0, 1)',
                    'rgba(156, 39, 176, 1)',
                    'rgba(0, 188, 212, 1)',
                    'rgba(255, 235, 59, 1)',
                ],
                borderWidth: 2,
            },
        ],
    };

    // Parameter comparison chart
    const parameterData = {
        labels: dataset.equipment.slice(0, 10).map(eq => eq.equipment_name.substring(0, 15)),
        datasets: [
            {
                label: 'Flowrate',
                data: dataset.equipment.slice(0, 10).map(eq => eq.flowrate),
                backgroundColor: 'rgba(63, 81, 181, 0.6)',
                borderColor: 'rgba(63, 81, 181, 1)',
                borderWidth: 2,
            },
            {
                label: 'Pressure',
                data: dataset.equipment.slice(0, 10).map(eq => eq.pressure),
                backgroundColor: 'rgba(255, 64, 129, 0.6)',
                borderColor: 'rgba(255, 64, 129, 1)',
                borderWidth: 2,
            },
            {
                label: 'Temperature',
                data: dataset.equipment.slice(0, 10).map(eq => eq.temperature),
                backgroundColor: 'rgba(76, 175, 80, 0.6)',
                borderColor: 'rgba(76, 175, 80, 1)',
                borderWidth: 2,
            },
        ],
    };

    const chartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'top',
            },
        },
    };

    return (
        <div className="container" style={{ paddingTop: '40px', paddingBottom: '40px' }}>
            <div className="card">
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '20px' }}>
                    <div>
                        <h1 style={{ fontSize: '32px', fontWeight: '700', marginBottom: '10px' }}>
                            {dataset.name}
                        </h1>
                        <p style={{ color: 'var(--text-secondary)' }}>
                            Uploaded: {new Date(dataset.uploaded_at).toLocaleString()}
                        </p>
                    </div>
                    <div style={{ display: 'flex', gap: '10px' }}>
                        <button
                            onClick={handleDownloadReport}
                            className="btn btn-success"
                            disabled={downloading}
                        >
                            {downloading ? 'Generating...' : '📄 Download PDF Report'}
                        </button>
                        <button onClick={() => navigate('/')} className="btn btn-secondary">
                            ← Back
                        </button>
                    </div>
                </div>

                {/* Statistics Grid */}
                <div className="stats-grid" style={{ marginTop: '30px' }}>
                    <div className="stat-card">
                        <div className="stat-value">{dataset.total_count}</div>
                        <div className="stat-label">Total Equipment</div>
                    </div>
                    <div className="stat-card" style={{ background: 'linear-gradient(135deg, #667eea, #764ba2)' }}>
                        <div className="stat-value">{dataset.avg_flowrate.toFixed(2)}</div>
                        <div className="stat-label">Avg Flowrate</div>
                    </div>
                    <div className="stat-card" style={{ background: 'linear-gradient(135deg, #f093fb, #f5576c)' }}>
                        <div className="stat-value">{dataset.avg_pressure.toFixed(2)}</div>
                        <div className="stat-label">Avg Pressure</div>
                    </div>
                    <div className="stat-card" style={{ background: 'linear-gradient(135deg, #4facfe, #00f2fe)' }}>
                        <div className="stat-value">{dataset.avg_temperature.toFixed(2)}°C</div>
                        <div className="stat-label">Avg Temperature</div>
                    </div>
                </div>
            </div>

            {/* Charts */}
            <div className="charts-grid">
                <div className="chart-card">
                    <h3 className="chart-title">Equipment Type Distribution</h3>
                    <div style={{ height: '350px' }}>
                        <Bar data={typeDistributionData} options={chartOptions} />
                    </div>
                </div>

                <div className="chart-card">
                    <h3 className="chart-title">Equipment Type Breakdown</h3>
                    <div style={{ height: '350px' }}>
                        <Pie data={typeDistributionData} options={chartOptions} />
                    </div>
                </div>
            </div>

            <div className="card" style={{ marginTop: '20px' }}>
                <h3 className="chart-title">Parameter Comparison (First 10 Equipment)</h3>
                <div style={{ height: '400px' }}>
                    <Bar data={parameterData} options={chartOptions} />
                </div>
            </div>

            {/* Equipment Table */}
            <div className="card">
                <h3 style={{ fontSize: '24px', fontWeight: '600', marginBottom: '20px' }}>
                    Equipment Details
                </h3>
                <div style={{ overflowX: 'auto' }}>
                    <table className="table">
                        <thead>
                            <tr>
                                <th>Equipment Name</th>
                                <th>Type</th>
                                <th>Flowrate</th>
                                <th>Pressure</th>
                                <th>Temperature</th>
                            </tr>
                        </thead>
                        <tbody>
                            {dataset.equipment.map((eq) => (
                                <tr key={eq.id}>
                                    <td>{eq.equipment_name}</td>
                                    <td>{eq.equipment_type}</td>
                                    <td>{eq.flowrate.toFixed(2)}</td>
                                    <td>{eq.pressure.toFixed(2)}</td>
                                    <td>{eq.temperature.toFixed(2)}°C</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
}

export default DatasetDetail;
