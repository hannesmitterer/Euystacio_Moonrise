# Euystacio Web Setup

This package contains both **static** and **dynamic** versions of the Euystacio web interface.

## Files

- `index.html` → Static demo version (works on GitHub Pages)
- `connect.html` → Dynamic version (connects to Flask backend on Render)
- `README.md` → This guide

## Setup Instructions

### 1. Static Site (GitHub Pages)
1. Create a GitHub repo (e.g., `euystacio-site`).
2. Upload `index.html` and `connect.html`.
3. In repo settings, enable **GitHub Pages** (branch: `main`, folder: `/root`).
4. Access at `https://<username>.github.io/euystacio-site`.

- `index.html` shows a login form (demo) + sample pulse graph.
- Link inside goes to `connect.html`.

### 2. Dynamic Site (Render)
1. Deploy backend (`euystacio-backend.zip`) on Render.
   - Python, `requirements.txt`
   - Start command: `python app.py`
2. In `connect.html`, ensure:
   ```js
   const BACKEND_URL = "https://<your-backend>.onrender.com";
   ```
   Replace `<your-backend>` with actual Render URL.

3. Open `connect.html` (via GitHub Pages) to interact with live backend.

### 3. Login Credentials
- Username: **hannesmitterer**
- Password: **moon-rise**

Only tutors with this login can send live pulses.

---
✅ You now have a **static GitHub Pages front-end** and a **dynamic Render back-end**.
