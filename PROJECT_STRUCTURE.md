# Project Structure

```
chemical-equipment-visualizer/
│
├── README.md                          # Main project documentation
├── QUICKSTART.md                      # Quick start guide
├── DEMO_SCRIPT.md                     # Demo video script
├── .gitignore                         # Git ignore file
├── setup.ps1                          # Windows setup script
├── sample_equipment_data.csv          # Sample CSV data for testing
│
├── backend/                           # Django Backend
│   ├── equipment_visualizer/          # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py               # Django settings
│   │   ├── urls.py                   # Main URL configuration
│   │   ├── wsgi.py                   # WSGI configuration
│   │   └── asgi.py                   # ASGI configuration
│   │
│   ├── api/                          # Django REST API app
│   │   ├── __init__.py
│   │   ├── models.py                 # Database models (Dataset, EquipmentData)
│   │   ├── serializers.py            # DRF serializers
│   │   ├── views.py                  # API views and endpoints
│   │   ├── urls.py                   # API URL routing
│   │   ├── admin.py                  # Django admin configuration
│   │   ├── apps.py                   # App configuration
│   │   └── utils.py                  # Utility functions (CSV processing, PDF generation)
│   │
│   ├── manage.py                     # Django management script
│   ├── requirements.txt              # Python dependencies
│   ├── README.md                     # Backend documentation
│   ├── db.sqlite3                    # SQLite database (created after migration)
│   └── venv/                         # Virtual environment (created during setup)
│
├── frontend-web/                     # React Web Frontend
│   ├── public/
│   │   └── index.html                # HTML template
│   │
│   ├── src/
│   │   ├── components/               # React components
│   │   │   ├── Login.js             # Login component
│   │   │   ├── Register.js          # Registration component
│   │   │   ├── Dashboard.js         # Dashboard component
│   │   │   ├── Upload.js            # Upload component
│   │   │   ├── DatasetDetail.js     # Dataset detail with charts
│   │   │   └── Navbar.js            # Navigation bar
│   │   │
│   │   ├── services/
│   │   │   └── api.js               # API service layer
│   │   │
│   │   ├── App.js                   # Main App component
│   │   ├── App.css                  # App styles
│   │   ├── index.js                 # React entry point
│   │   └── index.css                # Global styles
│   │
│   ├── package.json                  # npm dependencies
│   ├── README.md                     # Web frontend documentation
│   └── node_modules/                 # npm packages (created during setup)
│
└── frontend-desktop/                 # PyQt5 Desktop Frontend
    ├── main.py                       # Main desktop application
    ├── requirements.txt              # Python dependencies
    └── README.md                     # Desktop frontend documentation
```

## Key Components

### Backend (Django)

**Models**:
- `Dataset`: Stores uploaded datasets with metadata and statistics
- `EquipmentData`: Stores individual equipment records

**API Endpoints**:
- Authentication: `/api/auth/register/`, `/api/auth/login/`, `/api/auth/logout/`
- Datasets: `/api/datasets/`, `/api/datasets/{id}/`, `/api/datasets/upload/`
- Reports: `/api/datasets/{id}/summary/`, `/api/datasets/{id}/report/`

**Features**:
- User authentication with session management
- CSV file upload and parsing with Pandas
- Automatic calculation of statistics
- PDF report generation with ReportLab
- Automatic cleanup (keeps last 5 datasets per user)

### Frontend Web (React)

**Components**:
- `Login/Register`: User authentication
- `Dashboard`: Dataset list and statistics
- `Upload`: CSV file upload with drag-and-drop
- `DatasetDetail`: Visualizations with Chart.js
- `Navbar`: Navigation and user info

**Features**:
- React Router for navigation
- Axios for API calls
- Chart.js for interactive charts (Bar, Pie, Line)
- Responsive design
- Modern UI with animations

### Frontend Desktop (PyQt5)

**Classes**:
- `APIClient`: Backend communication
- `LoginWindow`: Login interface
- `RegisterWindow`: Registration interface
- `MainWindow`: Main application window
- `ChartWidget`: Matplotlib chart container

**Features**:
- Native desktop interface
- Matplotlib for data visualization
- Tab-based navigation
- File dialogs for upload/download
- Session management

## Data Flow

1. **User Registration/Login**:
   - User → Frontend → Backend API → Database
   - Backend returns session cookie

2. **CSV Upload**:
   - User selects file → Frontend → Backend API
   - Backend processes with Pandas
   - Saves to Database
   - Returns dataset info

3. **Visualization**:
   - Frontend requests dataset → Backend API
   - Backend returns data with statistics
   - Frontend renders charts (Chart.js or Matplotlib)

4. **PDF Report**:
   - Frontend requests report → Backend API
   - Backend generates PDF with ReportLab
   - Returns PDF file
   - Frontend downloads file

## Database Schema

### Dataset Table
- id (Primary Key)
- user_id (Foreign Key to User)
- name (CharField)
- file (FileField)
- uploaded_at (DateTimeField)
- total_count (IntegerField)
- avg_flowrate (FloatField)
- avg_pressure (FloatField)
- avg_temperature (FloatField)
- equipment_types (JSONField)

### EquipmentData Table
- id (Primary Key)
- dataset_id (Foreign Key to Dataset)
- equipment_name (CharField)
- equipment_type (CharField)
- flowrate (FloatField)
- pressure (FloatField)
- temperature (FloatField)

## Technologies Used

### Backend
- Django 4.2.9
- Django REST Framework 3.14.0
- Pandas 2.1.4
- ReportLab 4.0.8
- SQLite (Database)

### Web Frontend
- React 18.2.0
- Chart.js 4.4.1
- Axios 1.6.5
- React Router 6.21.3

### Desktop Frontend
- PyQt5 5.15.10
- Matplotlib 3.8.2
- Pandas 2.1.4
- Requests 2.31.0

## Security Features

- Password hashing with Django's built-in system
- CSRF protection
- Session-based authentication
- File upload validation
- SQL injection protection (Django ORM)
- XSS protection

## Performance Optimizations

- Database indexing on foreign keys
- Pagination for large datasets
- Lazy loading of equipment data
- Efficient bulk operations
- Chart data limiting (first 10 items for detailed views)
