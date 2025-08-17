# Production Deployment Checklist

This checklist ensures proper deployment of the Euystacio Moonrise system to production.

## Pre-Deployment Verification

### Backend Checklist
- [ ] `deployed-backend/app.py` has `debug=False`
- [ ] `deployed-backend/requirements.txt` is complete
- [ ] `deployed-backend/euystacio.py` exists
- [ ] `deployed-backend/pulse_log.json` exists (or will be created)
- [ ] All backend files are present and functional

### Frontend Checklist  
- [ ] `deployed-frontend/config.js` has correct backend URL: `https://euystacio-moonrise.onrender.com/`
- [ ] `deployed-frontend/index.html` exists
- [ ] `deployed-frontend/connect.html` exists
- [ ] Frontend configuration is consistent across files

### Documentation Checklist
- [ ] `DEPLOYMENT.md` has detailed deployment instructions
- [ ] `README.md` reflects production deployment steps
- [ ] Storage configuration is documented
- [ ] API endpoints are documented

## Backend Deployment (Render.com)

### Step 1: Create Render Service
- [ ] Go to [render.com](https://render.com)
- [ ] Create account or log in
- [ ] Click "New +" → "Web Service"
- [ ] Name: `euystacio-moonrise`

### Step 2: Configure Service
- [ ] Environment: Python 3
- [ ] Build Command: `pip install -r requirements.txt`  
- [ ] Start Command: `python app.py`
- [ ] Auto-Deploy: Enabled

### Step 3: Upload Files
- [ ] Upload all files from `deployed-backend/` directory
- [ ] Verify all files are present in Render dashboard

### Step 4: Deploy and Test
- [ ] Deploy the service
- [ ] Wait for deployment to complete
- [ ] Test endpoint: `https://euystacio-moonrise.onrender.com/`
- [ ] Test status: `https://euystacio-moonrise.onrender.com/status`
- [ ] Verify API responds correctly

## Frontend Deployment (GitHub Pages)

### Step 1: Prepare Repository
- [ ] Create new GitHub repository (e.g., `euystacio-frontend`)
- [ ] Upload all files from `deployed-frontend/` to repository root
- [ ] Ensure `config.js` has correct backend URL

### Step 2: Enable GitHub Pages
- [ ] Go to repository Settings → Pages
- [ ] Source: "Deploy from a branch"
- [ ] Branch: "main", Folder: "/ (root)"
- [ ] Save configuration

### Step 3: Test Deployment
- [ ] Wait for GitHub Pages deployment (1-2 minutes)
- [ ] Visit GitHub Pages URL
- [ ] Test login with credentials: `hannesmitterer` / `moon-rise`
- [ ] Test sending a pulse
- [ ] Verify data appears in backend

## Post-Deployment Verification

### End-to-End Testing
- [ ] Frontend loads correctly
- [ ] Backend API is accessible
- [ ] Authentication works
- [ ] Pulse submission works
- [ ] Data persistence works
- [ ] Real-time updates work

### Performance Testing
- [ ] Frontend loads quickly
- [ ] API responses are fast
- [ ] No CORS errors in browser console
- [ ] No JavaScript errors in browser console

### Documentation Verification
- [ ] All URLs in documentation are correct
- [ ] Instructions are clear and accurate
- [ ] Troubleshooting section covers common issues

## Environment Variables (Optional)

### Production Environment Variables
Backend (Render.com):
- [ ] `FLASK_ENV=production` (optional)
- [ ] Custom configuration variables if needed

Frontend (GitHub Pages):
- [ ] No environment variables needed
- [ ] Configuration is in `config.js`

## Monitoring and Maintenance

### Health Checks
- [ ] Set up monitoring for backend uptime
- [ ] Monitor API response times
- [ ] Check storage file size growth

### Regular Maintenance
- [ ] Monitor pulse log file size
- [ ] Plan database migration when needed
- [ ] Keep dependencies updated

## Rollback Plan

### If Deployment Fails
- [ ] Verify all files are correctly uploaded
- [ ] Check build logs for errors
- [ ] Verify configuration settings
- [ ] Test locally first

### Emergency Procedures
- [ ] Keep backup of working configuration
- [ ] Document any custom changes
- [ ] Have rollback procedure ready

## Success Criteria

Deployment is successful when:
- [ ] Backend responds at `https://euystacio-moonrise.onrender.com/`
- [ ] Frontend loads at GitHub Pages URL
- [ ] Users can log in and submit pulses
- [ ] Data is properly stored and retrieved
- [ ] No critical errors in logs

---

**Note**: This system uses JSON file storage for MVP. For production scale, consider upgrading to PostgreSQL or another database solution.