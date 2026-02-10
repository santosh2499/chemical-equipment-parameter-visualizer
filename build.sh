#!/usr/bin/env bash
# Exit on error
set -o errexit

# Build Frontend
cd frontend-web
npm install
npm run build
cd ..

# Build Backend
cd backend
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
