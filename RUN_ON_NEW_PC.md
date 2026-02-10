# 🚀 How to Run Project on a New PC

This guide covers everything you need to set up and run the Chemical Equipment Visualizer on a completely new computer.

## 1️⃣ Prerequisites (Install First)

Before you begin, ensure you have the following installed:

1.  **Python (3.8 or higher)**
    *   [Download Python](https://www.python.org/downloads/)
    *   ⚠️ **IMPORTANT:** In the installer, check the box **"Add Python to PATH"** before clicking Install.
2.  **Node.js (LTS Version)**
    *   [Download Node.js](https://nodejs.org/)
    *   Install the "LTS" version (Recommended for Most Users).
3.  **Git** (Optional, if cloning from GitHub)
    *   [Download Git](https://git-scm.com/downloads)

### Verify Installation
Open a terminal (Command Prompt or PowerShell) and run:
```powershell
python --version
node --version
npm --version
```
If these commands return versions, you are ready!

---

## 2️⃣ Get the Project

### Option A: Clone from GitHub
```bash
git clone <YOUR_REPOSITORY_URL>
cd chemical-equipment-visualizer
```

### Option B: Download ZIP
1.  Download the project ZIP file.
2.  Extract it to a folder (e.g., Desktop).
3.  Open the folder in VS Code or Terminal.

---

## 3️⃣ Automated Setup (Windows Users)

We have a script that does everything for you.

1.  Open **PowerShell** as Administrator (optional, but avoids permission issues) or just a regular terminal in the project folder.
2.  Run the setup script:
    ```powershell
    .\setup.ps1
    ```
    *   *Note: If you get a security error, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first.*
3.  Follow the prompts. You will be asked to create a **Superuser** (Admin account) for the backend. Remember the username and password!

---

## 4️⃣ Manual Setup (Mac/Linux or Manual Windows)

If the script doesn't work or you are on Mac/Linux, follow these steps one by one.

### Step A: Backend (Django)
```bash
cd backend
python -m venv venv

# Windows:
.\venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Create your admin login
```

### Step B: Web Frontend (React)
Open a **new terminal** in the project root:
```bash
cd frontend-web
npm install
```

### Step C: Desktop Frontend (PyQt5)
Open a **new terminal** in the project root:
```bash
cd frontend-desktop
pip install -r requirements.txt
```

---

## 5️⃣ Running the Application

You need to run **3 components** simultaneously. Open 3 separate terminal tabs/windows.

### Terminal 1: Backend Server
```powershell
cd backend
.\venv\Scripts\activate
python manage.py runserver
```
*   Server starts at: `http://localhost:8000`
*   Keep this running!

### Terminal 2: Web Application
```powershell
cd frontend-web
npm start
```
*   Opens in your browser at: `http://localhost:3000`

### Terminal 3: Desktop Application
```powershell
cd frontend-desktop
python main.py
```
*   Launches the desktop window.

---

## 6️⃣ How to Use

1.  **Login**: Use the credentials you created during the `createsuperuser` step.
2.  **Upload**: Navigate to "Upload Dataset" and select `sample_equipment_data.csv` (found in the project root).
3.  **Visualize**: Check the Dashboard to see your data visualized.

---

## 🛠 Troubleshooting

**Error: "Python is not recognized"**
*   Reinstall Python and make sure to check "Add to PATH".

**Error: "Module not found: Django" or "PIL"**
*   Make sure you activated the virtual environment (`.\venv\Scripts\activate`) before running python commands.

**Error: "npm is not recognized"**
*   Restart your terminal after installing Node.js.

**Error: "Script is not signed" (PowerShell)**
*   Run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
