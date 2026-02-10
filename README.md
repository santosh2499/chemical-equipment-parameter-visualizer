# Chemical Equipment Parameter Visualizer

A hybrid web and desktop application for visualizing and analyzing chemical equipment data. Built with Django REST Framework backend, React web frontend, and PyQt5 desktop frontend.

![Project Banner](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2-green.svg)
![React](https://img.shields.io/badge/React-18.2-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15-orange.svg)

## 🎯 Project Overview

This application allows users to upload CSV files containing chemical equipment data (Equipment Name, Type, Flowrate, Pressure, Temperature), automatically processes and analyzes the data, and provides interactive visualizations and PDF reports through both web and desktop interfaces.

### Key Features

✅ **CSV Upload** - Upload equipment data via web or desktop interface
✅ **Data Visualization** - Interactive charts using Chart.js (web) and Matplotlib (desktop)
✅ **Statistical Analysis** - Automatic calculation of averages and distributions
✅ **PDF Reports** - Generate professional PDF reports with tables and statistics
✅ **History Management** - Automatically stores last 5 datasets
✅ **Dual Interface** - Access via modern web browser or native desktop application
✅ **Common Backend** - Single Django REST API serves both frontends

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Users                                │
└────────────┬────────────────────────┬───────────────────┘
             │                        │
    ┌────────▼────────┐      ┌───────▼────────┐
    │   Web Browser   │      │  Desktop App   │
    │  (React + JS)   │      │    (PyQt5)     │
    └────────┬────────┘      └───────┬────────┘
             │                        │
             └────────┬───────────────┘
                      │
            ┌─────────▼──────────┐
            │   Django REST API   │
            │   (Backend)         │
            └─────────┬──────────┘
                      │
            ┌─────────▼──────────┐
            │   SQLite Database   │
            └────────────────────┘
```

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend (Web)** | React.js 18.2 + Chart.js 4.4 | Interactive web interface with charts |
| **Frontend (Desktop)** | PyQt5 5.15 + Matplotlib 3.8 | Native desktop application |
| **Backend** | Django 4.2 + Django REST Framework 3.14 | RESTful API server |
| **Data Processing** | Pandas 2.1.4 | CSV parsing and analytics |
| **Database** | SQLite | Data persistence |
| **PDF Generation** | ReportLab 4.0 | Professional PDF reports |

## 📋 Requirements

- Python 3.8 or higher
- Node.js 14 or higher
- npm 6 or higher

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/chemical-equipment-visualizer.git
cd chemical-equipment-visualizer
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Optional: for admin access
python manage.py runserver
```

Backend will run at: `http://localhost:8000`

### 3. Web Frontend Setup

Open a new terminal:

```bash
cd frontend-web
npm install
npm start
```

Web app will open at: `http://localhost:3000`

### 4. Desktop Frontend Setup

```bash
cd frontend-desktop

# Windows (using backend venv)
..\backend\venv\Scripts\python.exe main.py

# Linux/Mac
source ../backend/venv/bin/activate
python main.py
```

## 📊 Usage

### Web Application

1. Open `http://localhost:3000` in your browser
2. Click "Upload" in the navigation bar
3. Select `sample_equipment_data.csv` or your own CSV file
4. Enter a dataset name and click "Upload Dataset"
5. View interactive visualizations and download PDF reports

### Desktop Application

1. Launch the desktop app using the command above
2. Go to "Upload Dataset" tab
3. Browse for your CSV file
4. Enter a dataset name and upload
5. View visualizations in the "Visualization" tab
6. Download PDF reports

### CSV File Format

Your CSV file must have these columns:

```csv
Equipment Name,Type,Flowrate,Pressure,Temperature
Reactor-A1,Reactor,150.5,25.3,85.2
Heat Exchanger-B2,Heat Exchanger,200.8,15.7,120.5
```

## 🎨 Features

### Data Visualization

**Web (Chart.js)**:
- Bar charts for equipment type distribution
- Pie charts for type breakdown
- Multi-parameter comparison charts
- Interactive tooltips and legends

**Desktop (Matplotlib)**:
- Professional pie charts
- Multi-bar parameter comparison
- High-quality chart rendering
- Export-ready visualizations

### Statistical Analysis

- Total equipment count
- Average flowrate, pressure, and temperature
- Equipment type distribution
- Min/max values for all parameters

### PDF Reports

- Professional layout with headers
- Summary statistics table
- Equipment type distribution
- Detailed equipment list
- Automatic formatting

## 📁 Project Structure

```
chemical-equipment-visualizer/
├── backend/                    # Django backend
│   ├── equipment_visualizer/   # Django project settings
│   ├── api/                    # REST API app
│   │   ├── models.py          # Database models
│   │   ├── serializers.py     # DRF serializers
│   │   ├── views.py           # API endpoints
│   │   ├── utils.py           # Helper functions
│   │   └── middleware.py      # Custom middleware
│   ├── manage.py
│   └── requirements.txt
│
├── frontend-web/               # React web frontend
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── services/          # API service layer
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
├── frontend-desktop/           # PyQt5 desktop frontend
│   ├── main.py                # Main application
│   └── requirements.txt
│
├── sample_equipment_data.csv   # Sample data for testing
├── README.md                   # This file
├── QUICKSTART.md              # Quick setup guide
├── PROJECT_STRUCTURE.md        # Detailed structure
├── TESTING_GUIDE.md           # Testing instructions
└── .gitignore
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/datasets/` | GET | List all datasets |
| `/api/datasets/{id}/` | GET | Get dataset details |
| `/api/datasets/upload/` | POST | Upload CSV file |
| `/api/datasets/{id}/summary/` | GET | Get statistics |
| `/api/datasets/{id}/report/` | GET | Download PDF report |

## 🧪 Testing

See [TESTING_GUIDE.md](TESTING_GUIDE.md) for comprehensive testing instructions.

Quick test:
1. Start backend and web frontend
2. Upload `sample_equipment_data.csv`
3. Verify charts display correctly
4. Download and check PDF report

## 📸 Screenshots

### Web Application
- Modern, responsive interface
- Interactive Chart.js visualizations
- Drag-and-drop file upload

### Desktop Application
- Native PyQt5 interface
- Professional Matplotlib charts
- Tab-based navigation

## 🎥 Demo Video

[Link to demo video] - *TODO: Add link after recording*

The demo video shows:
- CSV file upload (web and desktop)
- Data visualization
- PDF report generation
- Dataset history management

## 🚀 Deployment (Optional)

### Backend (Railway/Render/Heroku)

1. Add `gunicorn` to requirements.txt
2. Create `Procfile`: `web: gunicorn equipment_visualizer.wsgi`
3. Set environment variables
4. Deploy

### Frontend (Vercel/Netlify)

1. Build: `npm run build`
2. Deploy `build` folder
3. Update API URL in environment variables

## 🤝 Contributing

This is an intern screening project. For educational purposes only.

## 📝 License

This project is created for educational purposes as part of an intern screening task.

## 👨‍💻 Author

[Your Name]
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Django REST Framework documentation
- React and Chart.js communities
- PyQt5 and Matplotlib documentation
- Sample data structure inspired by chemical engineering standards

## 📚 Additional Documentation

- [QUICKSTART.md](QUICKSTART.md) - Quick setup guide
- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) - Detailed code organization
- [TESTING_GUIDE.md](TESTING_GUIDE.md) - Testing procedures
- [DEMO_SCRIPT.md](DEMO_SCRIPT.md) - Demo video script
- [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - Feature completion status

## ⚙️ Configuration

### Environment Variables

Backend (`backend/.env`):
```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

Web Frontend (`frontend-web/.env`):
```
REACT_APP_API_URL=http://localhost:8000
```

## 🐛 Troubleshooting

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues and solutions.

Common issues:
- **CORS errors**: Ensure backend CORS settings include frontend URL
- **Upload fails**: Check file format and size (max 5MB)
- **Desktop app won't start**: Use backend's virtual environment

## 📊 Project Statistics

- **Total Lines of Code**: 3,000+
- **API Endpoints**: 8
- **React Components**: 6
- **Database Models**: 2
- **Supported File Format**: CSV
- **Max Dataset History**: 5

---

**Built with ❤️ for chemical equipment data analysis**
