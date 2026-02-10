import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { datasetAPI } from '../services/api';

function Upload() {
    const [file, setFile] = useState(null);
    const [name, setName] = useState('');
    const [uploading, setUploading] = useState(false);
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');
    const [dragOver, setDragOver] = useState(false);
    const navigate = useNavigate();

    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0];
        if (selectedFile) {
            setFile(selectedFile);
            if (!name) {
                setName(selectedFile.name.replace('.csv', ''));
            }
        }
    };

    const handleDragOver = (e) => {
        e.preventDefault();
        setDragOver(true);
    };

    const handleDragLeave = (e) => {
        e.preventDefault();
        setDragOver(false);
    };

    const handleDrop = (e) => {
        e.preventDefault();
        setDragOver(false);

        const droppedFile = e.dataTransfer.files[0];
        if (droppedFile && droppedFile.name.endsWith('.csv')) {
            setFile(droppedFile);
            if (!name) {
                setName(droppedFile.name.replace('.csv', ''));
            }
        } else {
            setError('Please drop a CSV file');
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!file) {
            setError('Please select a file');
            return;
        }

        setError('');
        setSuccess('');
        setUploading(true);

        const formData = new FormData();
        formData.append('file', file);
        formData.append('name', name || file.name);

        try {
            const response = await datasetAPI.upload(formData);
            setSuccess('File uploaded successfully!');
            setTimeout(() => {
                navigate(`/dataset/${response.data.dataset.id}`);
            }, 1500);
        } catch (err) {
            setError(err.response?.data?.error || 'Upload failed. Please try again.');
        } finally {
            setUploading(false);
        }
    };

    return (
        <div className="upload-container">
            <div className="card">
                <h1 style={{ fontSize: '32px', fontWeight: '700', marginBottom: '10px' }}>
                    Upload Dataset
                </h1>
                <p style={{ color: 'var(--text-secondary)', marginBottom: '30px' }}>
                    Upload a CSV file containing equipment data
                </p>

                {error && <div className="alert alert-error">{error}</div>}
                {success && <div className="alert alert-success">{success}</div>}

                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label className="form-label">Dataset Name</label>
                        <input
                            type="text"
                            className="form-input"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            placeholder="Enter dataset name"
                            required
                        />
                    </div>

                    <div
                        className={`upload-area ${dragOver ? 'drag-over' : ''}`}
                        onDragOver={handleDragOver}
                        onDragLeave={handleDragLeave}
                        onDrop={handleDrop}
                        onClick={() => document.getElementById('fileInput').click()}
                    >
                        <div className="upload-icon">📁</div>
                        <div className="upload-text">
                            {file ? file.name : 'Click to browse or drag and drop'}
                        </div>
                        <div className="upload-hint">
                            CSV files only (max 5MB)
                        </div>
                        <input
                            id="fileInput"
                            type="file"
                            className="file-input"
                            accept=".csv"
                            onChange={handleFileChange}
                        />
                    </div>

                    {file && (
                        <div className="selected-file">
                            <div>
                                <strong>{file.name}</strong>
                                <div style={{ fontSize: '14px', color: 'var(--text-secondary)' }}>
                                    {(file.size / 1024).toFixed(2)} KB
                                </div>
                            </div>
                            <button
                                type="button"
                                className="btn btn-danger"
                                onClick={() => setFile(null)}
                                style={{ padding: '8px 16px' }}
                            >
                                Remove
                            </button>
                        </div>
                    )}

                    <div style={{ marginTop: '30px', display: 'flex', gap: '10px' }}>
                        <button
                            type="submit"
                            className="btn btn-primary"
                            disabled={uploading || !file}
                            style={{ flex: 1 }}
                        >
                            {uploading ? 'Uploading...' : 'Upload Dataset'}
                        </button>
                        <button
                            type="button"
                            className="btn btn-secondary"
                            onClick={() => navigate('/')}
                            style={{ padding: '12px 24px' }}
                        >
                            Cancel
                        </button>
                    </div>
                </form>

                <div style={{ marginTop: '30px', padding: '20px', background: 'var(--background)', borderRadius: '8px' }}>
                    <h3 style={{ fontSize: '18px', fontWeight: '600', marginBottom: '10px' }}>
                        Required CSV Format
                    </h3>
                    <p style={{ color: 'var(--text-secondary)', marginBottom: '10px' }}>
                        Your CSV file must contain the following columns:
                    </p>
                    <ul style={{ paddingLeft: '20px', color: 'var(--text-secondary)' }}>
                        <li>Equipment Name</li>
                        <li>Type</li>
                        <li>Flowrate</li>
                        <li>Pressure</li>
                        <li>Temperature</li>
                    </ul>
                </div>
            </div>
        </div>
    );
}

export default Upload;
