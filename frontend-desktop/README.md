# PyQt5 Desktop Frontend

Desktop application for Chemical Equipment Parameter Visualizer.

## Setup

1. Create virtual environment (optional, can use backend's venv):
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

4. Run the application:
```bash
python main.py
```

## Features

- User authentication (login/register)
- CSV file upload
- Data visualization with Matplotlib
- Dataset history management
- PDF report download
- Native desktop interface

## Requirements

- Python 3.8+
- PyQt5
- Matplotlib
- Pandas
- Requests

## Configuration

The application connects to the Django backend at `http://localhost:8000` by default.

To change the API URL, edit the `API_BASE_URL` variable in `main.py`.

## Technologies

- PyQt5 for GUI
- Matplotlib for data visualization
- Pandas for data processing
- Requests for API calls
