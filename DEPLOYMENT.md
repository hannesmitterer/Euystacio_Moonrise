# Deployment Instructions

Generated on: Sun Aug 17 07:35:16 UTC 2025

## Backend Deployment (deployed-backend/)

### Option 1: Render
1. Create a new Web Service on Render
2. Upload all files from `deployed-backend/` directory
3. Set start command: `python app.py`
4. Deploy and note the URL

### Option 2: Railway/Heroku
1. Create new app
2. Upload files from `deployed-backend/`
3. Ensure `requirements.txt` is present
4. Deploy with Python buildpack

## Frontend Deployment (deployed-frontend/)

### Option 1: GitHub Pages
1. Create a new repository or use existing one
2. Upload files from `deployed-frontend/` to repository
3. Enable GitHub Pages in repository settings
4. Set source to main branch, root folder

### Option 2: Netlify/Vercel
1. Create new site
2. Upload files from `deployed-frontend/`
3. Deploy static site

## Configuration

Backend URL in frontend: https://my-enhanced-backend.onrender.com

## Testing
1. Visit your frontend URL
2. Login with:
   - Username: hannesmitterer
   - Password: moon-rise
3. Test sending pulses and viewing the chart

## API Endpoints
- POST /pulse - Send new pulse data
- GET /log - Retrieve all pulse data
- GET /status - Get system status
