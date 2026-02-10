# Quick Start Guide

## 🚀 Quick Start (Recommended)

### Option 1: Automated Setup (Windows)

Run the setup script:
```powershell
.\setup.ps1
```

### Option 2: Manual Setup

#### 1. Backend Setup

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend will run at: `http://localhost:8000`

#### 2. Web Frontend Setup

Open a new terminal:

```bash
cd frontend-web
npm install
npm start
```

Web app will open at: `http://localhost:3000`

#### 3. Desktop Frontend Setup

```bash
cd frontend-desktop

# Windows
..\backend\venv\Scripts\activate

# Linux/Mac
source ../backend/venv/bin/activate

pip install -r requirements.txt
python main.py
```

## 📝 Testing the Application

### 1. Create an Account

- **Web**: Navigate to `http://localhost:3000` and click "Register"
- **Desktop**: Click "Register New Account" button

### 2. Upload Sample Data

Use the provided `sample_equipment_data.csv` file:

- **Web**: Click "Upload" → Browse → Select file → Upload
- **Desktop**: Go to "Upload Dataset" tab → Browse → Select file → Upload

### 3. View Visualizations

- **Web**: Click on a dataset card to view charts and data
- **Desktop**: Click on a dataset in the list to see visualizations

### 4. Generate PDF Report

- **Web**: Click "Download PDF Report" button on dataset detail page
- **Desktop**: Click "Download PDF Report" button in visualization tab

## 🔧 Troubleshooting

### Backend Issues

**Problem**: `django-admin` not found
- **Solution**: Make sure virtual environment is activated

**Problem**: Database errors
- **Solution**: Run `python manage.py migrate`

**Problem**: CORS errors
- **Solution**: Check that `CORS_ALLOWED_ORIGINS` in `settings.py` includes your frontend URL

### Web Frontend Issues

**Problem**: API connection failed
- **Solution**: Ensure backend is running at `http://localhost:8000`

**Problem**: npm install fails
- **Solution**: Delete `node_modules` and `package-lock.json`, then run `npm install` again

### Desktop Frontend Issues

**Problem**: PyQt5 import error
- **Solution**: Install PyQt5: `pip install PyQt5`

**Problem**: Connection refused
- **Solution**: Ensure backend is running and `API_BASE_URL` in `main.py` is correct

## 📊 Sample Data Format

Your CSV file must have these columns:

```csv
Equipment Name,Type,Flowrate,Pressure,Temperature
Reactor-A1,Reactor,150.5,25.3,85.2
Heat Exchanger-B2,Heat Exchanger,200.8,15.7,120.5
```

## 🎯 Features Checklist

- ✅ User Authentication (Register/Login)
- ✅ CSV Upload
- ✅ Data Visualization (Charts)
- ✅ Statistical Analysis
- ✅ History Management (Last 5 datasets)
- ✅ PDF Report Generation
- ✅ Web Application (React + Chart.js)
- ✅ Desktop Application (PyQt5 + Matplotlib)
- ✅ Common Django Backend
- ✅ SQLite Database

## 🌐 API Endpoints

- `POST /api/auth/register/` - Register user
- `POST /api/auth/login/` - Login
- `POST /api/auth/logout/` - Logout
- `GET /api/auth/user/` - Get current user
- `POST /api/datasets/upload/` - Upload CSV
- `GET /api/datasets/` - List datasets
- `GET /api/datasets/{id}/` - Get dataset details
- `GET /api/datasets/{id}/summary/` - Get summary statistics
- `GET /api/datasets/{id}/report/` - Download PDF report

## 📹 Demo Video

Record a 2-3 minute demo showing:
1. User registration/login
2. CSV file upload
3. Data visualization (both web and desktop)
4. PDF report generation
5. Dataset history

## 🚀 Deployment (Optional)

### Backend (Heroku/Railway/Render)

1. Add `gunicorn` to requirements.txt
2. Create `Procfile`: `web: gunicorn equipment_visualizer.wsgi`
3. Set environment variables
4. Deploy

### Frontend (Vercel/Netlify)

1. Build: `npm run build`
2. Deploy `build` folder
3. Update API URL in environment variables

## 📧 Support

For issues or questions, please refer to the main README.md or create an issue on GitHub.
