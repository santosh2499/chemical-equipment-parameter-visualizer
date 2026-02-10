# Django Backend

This is the Django REST API backend for the Chemical Equipment Parameter Visualizer.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
```

2. Activate virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Start server:
```bash
python manage.py runserver
```

## API Endpoints

- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login
- `POST /api/auth/logout/` - Logout
- `POST /api/upload/` - Upload CSV file
- `GET /api/datasets/` - List all datasets (last 5)
- `GET /api/datasets/{id}/` - Get dataset details
- `GET /api/datasets/{id}/summary/` - Get dataset summary
- `GET /api/datasets/{id}/report/` - Generate PDF report

## Admin Panel

Access at `http://localhost:8000/admin/` with superuser credentials.
