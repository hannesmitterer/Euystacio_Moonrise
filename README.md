# Euystacio Dynamic Pulse Logging System

A full-stack application for dynamic pulse logging with JWT authentication and 3D visualization.

## Features Implemented ✅

### Backend (Flask API)
- **CORS Support**: Added flask-cors for cross-origin requests
- **JWT Authentication**: Secure token-based authentication system
- **User Management**: Registration and login endpoints with in-memory storage
- **Protected Endpoints**: Pulse submission requires authentication
- **Per-User Data**: Pulse logs are filtered by authenticated user

### API Endpoints

#### Authentication
- `POST /register` - Create new user account
  ```json
  {"username": "string", "password": "string"}
  ```
- `POST /login` - Authenticate user and get JWT token
  ```json
  {"username": "string", "password": "string"}
  ```

#### Pulse Management
- `POST /pulse` - Submit pulse data (requires authentication)
  ```json
  {"event": "string", "sentiment": number, "event_type": "string"}
  ```
- `GET /log` - Get pulse history (filtered by user if authenticated)
- `GET /status` - System status and metrics

### Frontend (HTML/JavaScript)
- **Authentication UI**: Login and registration forms with tab switching
- **Real API Integration**: Removed hardcoded credentials, uses backend endpoints
- **JWT Token Management**: Stores tokens in localStorage and includes in requests
- **3D Visualization**: Custom canvas-based 3D chart showing:
  - Time sequence on X-axis
  - Sentiment values on Y-axis  
  - User role depth on Z-axis
  - Color-coded sentiment (green=positive, red=negative)
- **Error Handling**: User feedback for network errors and validation
- **Session Persistence**: Automatic login on page refresh if token exists

## Dependencies

### Backend
```
Flask==2.3.2
PyJWT==2.8.0
flask-cors==4.0.0
```

### Frontend
- Custom canvas-based 3D visualization (no external dependencies)
- Native JavaScript (ES6+)

## Setup Instructions

### 1. Backend Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```
Server runs on `http://localhost:5000`

### 2. Frontend Setup
```bash
# Serve the HTML file (for development)
python -m http.server 8000
```
Frontend available at `http://localhost:8000/connect.html`

### 3. Production Deployment

#### Backend (Render)
1. Upload backend code to Render
2. Set start command: `python app.py`
3. Update `BACKEND_URL` in `connect.html` to your Render URL

#### Frontend (GitHub Pages)
1. Upload `connect.html` to GitHub repository
2. Enable GitHub Pages
3. Update `BACKEND_URL` in the HTML file

## Usage

1. **Registration**: Create a new account using the register tab
2. **Login**: Authenticate with username/password to get JWT token
3. **Submit Pulses**: Send pulse data with event name, sentiment (-1 to 1), and optional event type
4. **View Visualization**: Real-time 3D chart updates every 15 seconds
5. **Logout**: Clear session and return to login screen

## Data Storage

- **Users**: Stored in `users.json` (in-memory for MVP)
- **Pulses**: Stored in `pulse_log.json` with per-user filtering
- **Sessions**: JWT tokens with 24-hour expiration

## Security Features

- JWT token authentication with expiration
- CORS protection
- Input validation
- Protected API endpoints
- Session management

## 3D Visualization Features

The custom 3D chart displays:
- **X-axis**: Time sequence of pulses
- **Y-axis**: Sentiment values (-1 to 1)
- **Z-axis**: User role depth (visual separation)
- **Colors**: Green for positive sentiment, red for negative
- **Event Types**: Labeled on the chart
- **Interactive**: Grid background with legends

## Testing

All core functionality has been tested:
- ✅ User registration and login
- ✅ JWT token generation and validation
- ✅ Protected pulse submission
- ✅ User-specific data filtering
- ✅ 3D visualization rendering
- ✅ CORS support
- ✅ Error handling

## Future Enhancements

- Database persistence (PostgreSQL/MongoDB)
- Password hashing (bcrypt)
- Role-based access control
- Real-time updates (WebSockets)
- Advanced 3D interactions
- Data export functionality

---

## Legacy Setup (Original)

This package also contains both **static** and **dynamic** versions of the original Euystacio web interface.

### Files
- `index.html` → Static demo version (works on GitHub Pages)
- `connect.html` → Dynamic version with new authentication system
- Legacy credentials: Username: **hannesmitterer**, Password: **moon-rise** (hardcoded, now replaced with dynamic auth)
