# Euystacio Full Package

This archive contains both frontend and backend components.

## Structure

- `backend/euystacio-backend.zip`  
  Flask backend with pulse log and kernel.

- `frontend/euystacio-site.zip`  
  Static + dynamic web interface (for GitHub Pages + Render).

## Setup Steps

1. **Backend (Render)**
   - Upload `euystacio-backend.zip` to Render.
   - Deploy as Python service (`requirements.txt` included).
   - Start command: `python app.py`.

2. **Frontend (GitHub Pages)**
   - Upload `index.html` and `connect.html` from `euystacio-site.zip` to a GitHub repo.
   - Enable GitHub Pages (branch: `main`, folder: `/root`).

3. **Connect**
   - Edit `connect.html` → set `BACKEND_URL` to your Render backend URL.

4. **Login**
   - Username: `hannesmitterer`
   - Password: `moon-rise`

✅ Once done, you’ll have:
- A **static demo site** via GitHub Pages.
- A **dynamic live site** connected to your backend.
