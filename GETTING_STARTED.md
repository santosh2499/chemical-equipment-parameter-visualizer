# 🚀 Getting Started - Quick Reference

## Prerequisites
- Python 3.8+
- Node.js 14+
- Git

## 📦 Installation (Choose One Method)

### Method 1: Automated Setup (Recommended for Windows)
```powershell
.\setup.ps1
```

### Method 2: Manual Setup

#### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

#### Web Frontend
```bash
cd frontend-web
npm install
```

#### Desktop Frontend
```bash
cd frontend-desktop
pip install -r requirements.txt
```

## ▶️ Running the Application

### Start Backend (Terminal 1)
```bash
cd backend
venv\Scripts\activate
python manage.py runserver
```
→ Backend runs at `http://localhost:8000`

### Start Web App (Terminal 2)
```bash
cd frontend-web
npm start
```
→ Web app opens at `http://localhost:3000`

### Start Desktop App (Terminal 3)
```bash
cd frontend-desktop
python main.py
```
→ Desktop window opens

## 🎯 First Steps

1. **Register**: Create a new account (web or desktop)
2. **Login**: Use your credentials
3. **Upload**: Use `sample_equipment_data.csv`
4. **Visualize**: Click on the dataset to see charts
5. **Download**: Generate and download PDF report

## 📚 Documentation

- **README.md** - Project overview and features
- **QUICKSTART.md** - Detailed setup instructions
- **PROJECT_STRUCTURE.md** - Code organization
- **TESTING_GUIDE.md** - Testing checklist
- **DEMO_SCRIPT.md** - Video recording guide
- **IMPLEMENTATION_SUMMARY.md** - Feature completion status

## 🐛 Common Issues

**Backend won't start?**
→ Activate virtual environment first

**Web app shows connection error?**
→ Ensure backend is running on port 8000

**Desktop app can't connect?**
→ Check backend is running and API_BASE_URL in main.py

**npm install fails?**
→ Delete node_modules and package-lock.json, try again

## 📋 Submission Checklist

- [ ] Test all features (use TESTING_GUIDE.md)
- [ ] Record demo video (use DEMO_SCRIPT.md)
- [ ] Initialize Git: `.\git-init.ps1`
- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Add demo video link to README
- [ ] Add deployment link (optional)
- [ ] Submit repository URL

## 🎥 Demo Video

Record showing:
1. User registration/login
2. CSV upload (both web & desktop)
3. Data visualization
4. PDF report generation
5. Dataset history

## 🌐 GitHub Setup

```bash
# After running git-init.ps1
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

## ✨ Key Features to Demonstrate

✅ Hybrid architecture (web + desktop)
✅ Common Django backend
✅ User authentication
✅ CSV upload & processing
✅ Interactive visualizations
✅ PDF report generation
✅ Dataset history (last 5)
✅ Professional UI/UX

## 📞 Need Help?

Check the documentation files or review the code comments for detailed explanations.

---

**Good luck with your intern screening task! 🎉**
