# Deployment Instructions for Production

Generated on: Sun Aug 17 07:35:16 UTC 2025

## Backend Deployment (deployed-backend/)

### Production Deployment to Render.com

1. **Create Render Account and New Web Service**
   - Go to [render.com](https://render.com) and create an account
   - Click "New +" → "Web Service"
   - Connect your GitHub repository or upload files manually

2. **Configure the Service**
   - **Name**: `euystacio-moonrise`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Auto-Deploy**: Enable for automatic deployments

3. **Upload Backend Files**
   - Upload all files from the `deployed-backend/` directory:
     - `app.py` (production-ready with debug=False)
     - `euystacio.py`
     - `requirements.txt`
     - `pulse_log.json` (initial empty log)

4. **Environment Variables (Optional)**
   - Set any environment variables if needed for production
   - The app is configured to work with default settings

5. **Deploy and Note URL**
   - Deploy the service
   - Your backend will be available at: `https://euystacio-moonrise.onrender.com/`
   - Test the API endpoints to ensure they're working

### Alternative: Railway/Heroku
1. Create new app with name `euystacio-moonrise`
2. Upload files from `deployed-backend/`
3. Ensure `requirements.txt` is present
4. Deploy with Python buildpack
5. Set start command: `python app.py`

## Frontend Deployment (deployed-frontend/)

### Production Deployment to GitHub Pages

1. **Prepare Repository**
   - Create a new GitHub repository (e.g., `euystacio-frontend`) or use existing one
   - Upload all files from `deployed-frontend/` directory to the repository root:
     - `index.html`
     - `connect.html`
     - `config.js` (with production backend URL)
     - `README.md`

2. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Set source to "Deploy from a branch"
   - Select "main" branch and "/ (root)" folder
   - Save the configuration

3. **Configure Backend URL**
   - The `config.js` is already configured with production URL: `https://euystacio-moonrise.onrender.com/`
   - Verify the backend URL is correct in the configuration
   - GitHub Pages will serve your frontend at: `https://yourusername.github.io/repository-name/`

4. **Test Deployment**
   - Wait for deployment to complete (usually 1-2 minutes)
   - Visit your GitHub Pages URL
   - Verify frontend connects to the production backend

### Alternative: Netlify/Vercel
1. Create new site on Netlify or Vercel
2. Upload files from `deployed-frontend/`
3. Deploy as static site
4. Update backend URL in config.js if needed

## Storage Configuration

### JSON File Storage (Current MVP)
- The system uses JSON files for data persistence (`pulse_log.json`)
- This is suitable for MVP and development purposes
- Files are stored locally on the server filesystem
- **Advantages**: Simple, no database setup required
- **Limitations**: Not suitable for high-scale production, data lost on server restart

### Future Database Upgrade
- For production scale, consider upgrading to:
  - PostgreSQL (recommended for Render.com)
  - SQLite for smaller deployments
  - MongoDB for NoSQL approach
- Database migration can be implemented in future releases

## Configuration

### Production Backend URL
**Frontend Configuration**: `https://euystacio-moonrise.onrender.com/`

The frontend is configured to connect to this production backend URL. Ensure both frontend and backend use this URL consistently.

### Environment Variables
**Backend** (optional production settings):
- `FLASK_ENV=production`
- `DEBUG=False` (already set in code)

## Testing Production Deployment

1. **Backend Testing**
   - Visit: `https://euystacio-moonrise.onrender.com/`
   - Should return API information
   - Test: `https://euystacio-moonrise.onrender.com/status`
   - Should return system status

2. **Frontend Testing**
   - Visit your GitHub Pages URL
   - Login with credentials:
     - Username: `hannesmitterer`
     - Password: `moon-rise`
   - Test sending pulses and viewing the chart
   - Verify data is saved and retrieved correctly

3. **End-to-End Testing**
   - Submit a pulse from frontend
   - Check that it appears in the backend log
   - Verify real-time updates work correctly

## API Endpoints

- **GET** `/` - API information and health check
- **POST** `/pulse` - Send new pulse data
- **GET** `/log` - Retrieve all pulse data
- **GET** `/status` - Get basic system status
- **GET** `/kernel` - Get detailed kernel status
- **GET** `/metrics` - Get performance metrics

## Troubleshooting

### Common Issues
1. **CORS Errors**: Ensure CORS is properly configured in backend
2. **Backend URL**: Verify frontend config.js has correct backend URL
3. **JSON Storage**: Ensure pulse_log.json exists and is writable
4. **Dependencies**: Check requirements.txt is complete and up-to-date
