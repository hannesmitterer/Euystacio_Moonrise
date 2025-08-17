# Euystacio Moonrise - Deployment Guide

Euystacio is a dynamic sentiment tracking system with a Flask backend and static frontend. This guide provides comprehensive instructions for deploying both components.

## Project Structure

```
Euystacio_Moonrise/
├── euystacio-backend/          # Flask backend for Render deployment
│   ├── app.py                  # Main Flask application
│   ├── euystacio.py           # Core sentiment processing logic
│   ├── requirements.txt       # Python dependencies
│   ├── render.yaml           # Render deployment configuration
│   ├── pulse_log.json        # Data persistence file
│   └── Dockerfile            # Container deployment option
├── euystacio-site/            # Frontend for GitHub Pages
│   ├── index.html            # Static demo version
│   └── connect.html          # Dynamic version (connects to backend)
└── README.md                 # This deployment guide
```

## Backend Deployment (Render)

### Quick Deploy
1. **Create a Render account** at [render.com](https://render.com)
2. **Connect your GitHub repository** to Render
3. **Create a new Web Service** with these settings:
   - **Repository**: `hannesmitterer/Euystacio_Moonrise`
   - **Root Directory**: `euystacio-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Service Name**: `euystacio-moonrise`

### Manual Deploy
If you prefer manual deployment:

1. **Prepare the backend files**:
   ```bash
   cd euystacio-backend
   zip -r euystacio-backend.zip .
   ```

2. **Upload to Render**:
   - Go to Render Dashboard
   - Create New → Web Service
   - Upload your zip file
   - Configure as described above

3. **Environment Variables** (optional):
   - `FLASK_ENV`: `production`

### Docker Deployment (Alternative)
If you prefer containerized deployment:

```bash
cd euystacio-backend
docker build -t euystacio-backend .
docker run -p 5000:5000 euystacio-backend
```

### Backend Features
- **POST /pulse**: Submit new sentiment data
- **GET /status**: Check system status and metrics
- **GET /log**: Retrieve complete pulse history
- **CORS enabled** for frontend integration
- **Persistent data storage** in `pulse_log.json`

## Frontend Deployment (GitHub Pages)

### Option 1: Deploy from /euystacio-site Directory

1. **Enable GitHub Pages**:
   - Go to your repository settings
   - Navigate to "Pages" section
   - Source: Deploy from a branch
   - Branch: `main`
   - Folder: `/euystacio-site`
   - Save settings

2. **Access your site** at:
   ```
   https://hannesmitterer.github.io/Euystacio_Moonrise/
   ```

### Option 2: Create Separate Repository

1. **Create a new repository** (e.g., `euystacio-frontend`)
2. **Copy frontend files**:
   ```bash
   cp euystacio-site/* /path/to/new/repo/
   ```
3. **Enable GitHub Pages** as above
4. **Access at**: `https://hannesmitterer.github.io/euystacio-frontend/`

### Frontend Files
- **index.html**: Static demo with sample data and login simulation
- **connect.html**: Dynamic version that connects to the live backend API

## Configuration

### Backend URL Configuration
The frontend is configured to connect to: `https://euystacio-moonrise.onrender.com`

If you need to change this URL:
1. Edit `connect.html`
2. Update the `BACKEND_URL` constant:
   ```javascript
   const BACKEND_URL = "https://your-backend-url.onrender.com";
   ```

### Authentication
**Login Credentials** (for pulse submission):
- **Username**: `hannesmitterer`
- **Password**: `moon-rise`

## Testing Your Deployment

### 1. Test Backend
Visit your Render URL and append `/status`:
```
https://euystacio-moonrise.onrender.com/status
```
Expected response:
```json
{
  "status": "ok",
  "balance_metric": 0.0,
  "pulse_count": 0
}
```

### 2. Test Frontend
1. **Static Demo**: Visit your GitHub Pages URL to see the demo
2. **Dynamic Connection**: Click "Go to Dynamic Live Version" 
3. **Submit Pulse**: Login and try submitting a test pulse

### 3. Test Integration
1. Open browser developer tools
2. Navigate to the dynamic version
3. Submit a pulse and check the network tab for successful API calls

## Troubleshooting

### Backend Issues
- **Cold starts**: Render free tier has cold starts - first request may take 30+ seconds
- **CORS errors**: Backend includes CORS headers for all origins
- **File persistence**: `pulse_log.json` persists data across requests

### Frontend Issues
- **HTTPS requirement**: GitHub Pages serves over HTTPS, ensure backend URL uses HTTPS
- **Cache issues**: Clear browser cache if changes don't appear
- **API connectivity**: Check browser console for error messages

### Common Deploy Issues
- **Wrong root directory**: Ensure Render points to `euystacio-backend/` 
- **Missing dependencies**: Verify `requirements.txt` is present and correct
- **Port conflicts**: Backend runs on port 5000 by default

## Development

### Local Development
1. **Backend**:
   ```bash
   cd euystacio-backend
   pip install -r requirements.txt
   python app.py
   ```
   Backend runs at: http://localhost:5000

2. **Frontend**:
   ```bash
   cd euystacio-site
   # Serve with any local server, e.g.:
   python -m http.server 8000
   ```
   Frontend runs at: http://localhost:8000

3. **Update frontend for local testing**:
   Temporarily change `BACKEND_URL` in `connect.html` to `http://localhost:5000`

## URLs Summary

- **Backend API**: https://euystacio-moonrise.onrender.com
- **Frontend Demo**: https://hannesmitterer.github.io/Euystacio_Moonrise/
- **GitHub Repository**: https://github.com/hannesmitterer/Euystacio_Moonrise

---

✅ **You now have a complete Euystacio deployment with a Render backend and GitHub Pages frontend!**
