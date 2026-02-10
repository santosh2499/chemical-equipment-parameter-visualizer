# How to Run the Desktop Application

## The Problem

The desktop app is trying to use your system Python (Anaconda) which has a broken matplotlib installation. You need to use the backend's virtual environment instead.

## Solution 1: Use the Backend Virtual Environment

### Step 1: Install Desktop Dependencies in Backend Venv

```powershell
cd backend
.\venv\Scripts\activate
pip install PyQt5 matplotlib requests
```

### Step 2: Run Desktop App from Backend Venv

```powershell
# Stay in backend directory with venv activated
cd ..\frontend-desktop
python main.py
```

## Solution 2: Use the Run Script (Recommended)

I created a script for you:

```powershell
cd frontend-desktop
.\run.ps1
```

## Solution 3: Create Separate Venv for Desktop (Alternative)

If you want a separate environment:

```powershell
cd frontend-desktop
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Current Status

✅ Backend is running (port 8000)
✅ Web frontend is running (port 3000)
⏳ Desktop app dependencies are installing...

## Once Installation Completes

Run from backend directory:
```powershell
cd backend
.\venv\Scripts\activate
cd ..\frontend-desktop
python main.py
```

Or use the simpler approach:
```powershell
cd frontend-desktop
..\backend\venv\Scripts\python.exe main.py
```

## Why This Happens

- Your system Python (Anaconda) has conflicting package versions
- The backend venv has clean, compatible versions
- Desktop app needs PyQt5, matplotlib, and requests
- These are now being installed in the backend venv

## After Desktop App Starts

You should see:
1. A login window (but you can close it since we removed auth)
2. Or directly the main window
3. You can upload datasets and view visualizations

## Note

Since we removed authentication, you might need to update the desktop app to skip the login screen. Let me know if you want me to do that!
