# Testing Guide

## Manual Testing Checklist

### Backend API Testing

#### 1. Authentication Tests

**Register User**:
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "password_confirm": "testpass123"
  }'
```

Expected: 201 Created with user data

**Login**:
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }' \
  -c cookies.txt
```

Expected: 200 OK with user data and session cookie

**Get Current User**:
```bash
curl -X GET http://localhost:8000/api/auth/user/ \
  -b cookies.txt
```

Expected: 200 OK with user data

**Logout**:
```bash
curl -X POST http://localhost:8000/api/auth/logout/ \
  -b cookies.txt
```

Expected: 200 OK

#### 2. Dataset Tests

**Upload CSV**:
```bash
curl -X POST http://localhost:8000/api/datasets/upload/ \
  -b cookies.txt \
  -F "file=@sample_equipment_data.csv" \
  -F "name=Test Dataset"
```

Expected: 201 Created with dataset data

**List Datasets**:
```bash
curl -X GET http://localhost:8000/api/datasets/ \
  -b cookies.txt
```

Expected: 200 OK with array of datasets

**Get Dataset Details**:
```bash
curl -X GET http://localhost:8000/api/datasets/1/ \
  -b cookies.txt
```

Expected: 200 OK with full dataset including equipment

**Get Summary**:
```bash
curl -X GET http://localhost:8000/api/datasets/1/summary/ \
  -b cookies.txt
```

Expected: 200 OK with statistics and type distribution

**Download Report**:
```bash
curl -X GET http://localhost:8000/api/datasets/1/report/ \
  -b cookies.txt \
  -o report.pdf
```

Expected: 200 OK with PDF file

### Web Frontend Testing

#### 1. Authentication Flow

- [ ] Navigate to http://localhost:3000
- [ ] Click "Register here"
- [ ] Fill in registration form
- [ ] Submit and verify redirect to login
- [ ] Login with credentials
- [ ] Verify redirect to dashboard
- [ ] Verify navbar shows username
- [ ] Click logout
- [ ] Verify redirect to login

#### 2. Upload Flow

- [ ] Login
- [ ] Click "Upload New Dataset" or navigate to /upload
- [ ] Enter dataset name
- [ ] Click browse or drag-and-drop CSV file
- [ ] Verify file name appears
- [ ] Click "Upload Dataset"
- [ ] Verify success message
- [ ] Verify redirect to dataset detail page

#### 3. Dashboard

- [ ] Verify statistics cards display correctly
- [ ] Verify dataset list shows all datasets
- [ ] Click on a dataset card
- [ ] Verify navigation to detail page

#### 4. Dataset Detail

- [ ] Verify statistics cards show correct values
- [ ] Verify equipment type distribution bar chart renders
- [ ] Verify pie chart renders
- [ ] Verify parameter comparison chart renders
- [ ] Verify equipment data table displays all records
- [ ] Click "Download PDF Report"
- [ ] Verify PDF downloads successfully
- [ ] Open PDF and verify contents

#### 5. Responsive Design

- [ ] Resize browser window
- [ ] Verify layout adapts to mobile size
- [ ] Test on actual mobile device (optional)

### Desktop Frontend Testing

#### 1. Launch and Login

- [ ] Run `python main.py`
- [ ] Verify login window appears
- [ ] Enter credentials
- [ ] Click "Login"
- [ ] Verify main window opens

#### 2. Registration

- [ ] Click "Register New Account"
- [ ] Fill in registration form
- [ ] Click "Register"
- [ ] Verify success message
- [ ] Close registration window
- [ ] Login with new credentials

#### 3. Dashboard Tab

- [ ] Verify dataset list displays
- [ ] Click "Refresh Datasets"
- [ ] Verify list updates
- [ ] Click on a dataset
- [ ] Verify switch to Visualization tab

#### 4. Upload Tab

- [ ] Click "Upload Dataset" tab
- [ ] Click "Browse..."
- [ ] Select CSV file
- [ ] Verify file path displays
- [ ] Enter dataset name
- [ ] Click "Upload Dataset"
- [ ] Verify success message
- [ ] Verify switch to Dashboard tab
- [ ] Verify new dataset appears in list

#### 5. Visualization Tab

- [ ] Select a dataset from Dashboard
- [ ] Verify dataset info displays
- [ ] Verify pie chart renders
- [ ] Verify multi-bar chart renders
- [ ] Click "Download PDF Report"
- [ ] Choose save location
- [ ] Verify success message
- [ ] Open PDF and verify contents

#### 6. Logout

- [ ] Click "Logout"
- [ ] Confirm logout dialog
- [ ] Verify return to login window

## Integration Testing

### Test Scenario 1: Complete User Journey (Web)

1. Register new user
2. Login
3. Upload sample CSV
4. View visualizations
5. Download PDF report
6. Upload second dataset
7. Verify both datasets appear
8. Logout

### Test Scenario 2: Complete User Journey (Desktop)

1. Register new user
2. Login
3. Upload sample CSV
4. View visualizations
5. Download PDF report
6. Upload second dataset
7. Verify both datasets appear
8. Logout

### Test Scenario 3: Cross-Platform Consistency

1. Login on web
2. Upload dataset
3. Logout
4. Login on desktop with same credentials
5. Verify dataset appears
6. Upload another dataset on desktop
7. Logout
8. Login on web
9. Verify both datasets appear

### Test Scenario 4: Dataset Limit

1. Login
2. Upload 6 datasets
3. Verify only last 5 are kept
4. Verify oldest dataset is deleted

## Error Handling Tests

### Backend

- [ ] Upload invalid CSV format
- [ ] Upload CSV with missing columns
- [ ] Upload file larger than 5MB
- [ ] Login with wrong credentials
- [ ] Register with existing username
- [ ] Access protected endpoint without authentication

### Web Frontend

- [ ] Submit empty login form
- [ ] Submit registration with mismatched passwords
- [ ] Upload without selecting file
- [ ] Try to access protected routes without login

### Desktop Frontend

- [ ] Submit empty login form
- [ ] Submit registration with mismatched passwords
- [ ] Upload without selecting file
- [ ] Try operations when backend is offline

## Performance Tests

- [ ] Upload large CSV (1000+ rows)
- [ ] Render charts with large datasets
- [ ] Multiple simultaneous uploads
- [ ] Rapid navigation between pages

## Browser Compatibility (Web)

- [ ] Chrome
- [ ] Firefox
- [ ] Edge
- [ ] Safari (if available)

## Expected Results Summary

### Successful Operations

✅ User can register and login
✅ User can upload CSV files
✅ Data is parsed and stored correctly
✅ Statistics are calculated accurately
✅ Charts render properly
✅ PDF reports generate successfully
✅ Only last 5 datasets are kept
✅ Both web and desktop access same data
✅ Logout works correctly

### Error Handling

✅ Invalid credentials show error message
✅ Invalid CSV shows error message
✅ Unauthorized access is blocked
✅ Form validation prevents invalid submissions

## Bug Reporting Template

If you find a bug, please report it with:

```
**Bug Description**: 
[Clear description of the issue]

**Steps to Reproduce**:
1. 
2. 
3. 

**Expected Behavior**:
[What should happen]

**Actual Behavior**:
[What actually happens]

**Environment**:
- OS: 
- Browser (if web): 
- Python version: 
- Node version (if web): 

**Screenshots**:
[If applicable]

**Error Messages**:
[Any error messages or logs]
```

## Automated Testing (Future Enhancement)

Consider adding:
- Unit tests for models and serializers
- Integration tests for API endpoints
- Frontend component tests with Jest
- End-to-end tests with Selenium/Playwright
