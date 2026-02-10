# React Web Frontend

Web application for Chemical Equipment Parameter Visualizer.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Start development server:
```bash
npm start
```

The application will open at `http://localhost:3000`

## Features

- User authentication (login/register)
- CSV file upload
- Interactive data visualization with Chart.js
- Dataset history management
- PDF report generation
- Responsive design

## Build for Production

```bash
npm run build
```

The production build will be in the `build/` directory.

## Environment Variables

Create a `.env` file in the root directory:

```
REACT_APP_API_URL=http://localhost:8000
```

## Technologies

- React 18
- Chart.js for data visualization
- Axios for API calls
- React Router for navigation
