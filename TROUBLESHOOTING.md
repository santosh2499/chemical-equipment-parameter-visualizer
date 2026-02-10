# Upload Troubleshooting Guide

## Issue: "Upload failed. Please try again."

### Quick Fixes

#### 1. Restart Backend Server
The backend needs to be restarted after the CORS configuration changes.

```bash
# Stop the current server (Ctrl+C in the terminal)
# Then restart:
cd backend
venv\Scripts\activate
python manage.py runserver
```

#### 2. Clear Browser Cache
- Press `Ctrl + Shift + Delete`
- Clear cookies and cached files
- Refresh the page (`Ctrl + F5`)

#### 3. Check Backend is Running
- Backend should be at `http://localhost:8000`
- Visit `http://localhost:8000/admin/` to verify

#### 4. Verify File Format
- File must be `.csv`
- Must have columns: `Equipment Name`, `Type`, `Flowrate`, `Pressure`, `Temperature`
- File size must be less than 5MB

### Desktop App Issue: Matplotlib Error

**Problem**: Desktop app fails with matplotlib/PIL error

**Solution**: Use the backend's virtual environment

#### Option 1: Use the run script
```bash
cd frontend-desktop
.\run.ps1
```

#### Option 2: Manual activation
```bash
cd frontend-desktop
..\backend\venv\Scripts\activate
python main.py
```

#### Option 3: Install in backend venv
```bash
cd backend
venv\Scripts\activate
pip install -r ..\frontend-desktop\requirements.txt
cd ..\frontend-desktop
python main.py
```

### Common Upload Errors

#### Error: "Missing required columns"
**Fix**: Ensure CSV has exact column names (case-sensitive):
- Equipment Name
- Type
- Flowrate
- Pressure
- Temperature

#### Error: "File size must be less than 5MB"
**Fix**: Reduce the number of rows in your CSV file

#### Error: "Only CSV files are allowed"
**Fix**: Ensure file extension is `.csv`, not `.txt` or `.xlsx`

#### Error: "Please select a file"
**Fix**: Click browse or drag-and-drop a file before uploading

#### Error: "Login failed" or "Unauthorized"
**Fix**: 
1. Register a new account first
2. Login with correct credentials
3. Check that cookies are enabled in browser

### Network Errors

#### Error: "Network Error" or "Connection refused"
**Fix**:
1. Ensure backend is running on port 8000
2. Check firewall settings
3. Try `http://127.0.0.1:8000` instead of `localhost`

#### Error: "CORS error"
**Fix**: Backend settings have been updated. Restart the backend server.

### Browser Console Debugging

1. Open browser console (F12)
2. Go to "Network" tab
3. Try uploading again
4. Look for failed requests (red)
5. Click on the failed request to see details

### Testing Upload Manually

#### Using curl (Backend test):
```bash
# First login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"youruser\",\"password\":\"yourpass\"}" \
  -c cookies.txt

# Then upload
curl -X POST http://localhost:8000/api/datasets/upload/ \
  -b cookies.txt \
  -F "file=@sample_equipment_data.csv" \
  -F "name=Test Dataset"
```

### Step-by-Step Upload Process

1. **Start Backend**:
   ```bash
   cd backend
   venv\Scripts\activate
   python manage.py runserver
   ```

2. **Start Web Frontend**:
   ```bash
   cd frontend-web
   npm start
   ```

3. **Register/Login**:
   - Go to `http://localhost:3000`
   - Click "Register here"
   - Fill form and submit
   - Login with credentials

4. **Upload File**:
   - Click "Upload New Dataset"
   - Enter dataset name
   - Click browse or drag file
   - Click "Upload Dataset"

### If Still Not Working

1. **Check Backend Logs**:
   - Look at the terminal running `python manage.py runserver`
   - Check for error messages

2. **Check Browser Console**:
   - Press F12
   - Look for JavaScript errors
   - Check Network tab for failed requests

3. **Verify Database**:
   ```bash
   cd backend
   venv\Scripts\activate
   python manage.py shell
   ```
   ```python
   from django.contrib.auth.models import User
   print(User.objects.all())  # Should show your user
   ```

4. **Try Desktop App**:
   - If web upload fails, try desktop app
   - Desktop app uses same backend

### Success Indicators

✅ Backend shows: "POST /api/datasets/upload/ 201"
✅ Web shows: "File uploaded successfully!"
✅ Redirects to dataset detail page
✅ Charts display correctly

### Still Having Issues?

1. Check `TESTING_GUIDE.md` for comprehensive tests
2. Review `IMPLEMENTATION_SUMMARY.md` for feature status
3. Ensure all dependencies are installed
4. Try creating a new virtual environment
5. Check Python version (3.8+ required)
6. Check Node version (14+ required)

## Quick Checklist

- [ ] Backend is running on port 8000
- [ ] Web frontend is running on port 3000
- [ ] User is registered and logged in
- [ ] CSV file has correct format
- [ ] File size is less than 5MB
- [ ] Browser cookies are enabled
- [ ] CORS settings are updated
- [ ] Backend server was restarted after CORS changes
