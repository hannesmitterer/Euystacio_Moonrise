# Euystacio Moonrise - Enhanced Web Setup v2.0

This repository contains an enhanced Euystacio system with self-evolving AI kernel, automated deployment tools, and improved frontend-backend integration.

## 🌟 New Features (v2.0)

### Enhanced Euystacio Kernel
- **Adaptive Learning Rate:** Automatically adjusts based on volatility and prediction accuracy
- **Pattern Recognition:** Detects and stores significant sentiment patterns
- **Memory Management:** Intelligent cleanup with configurable limits (default: 500 entries)
- **Self-Evolution:** Tracks prediction errors and continuously improves algorithms
- **Volatility Detection:** Recognizes unstable periods and adapts accordingly

### Automated Deployment
- **Setup Scripts:** Automatic ZIP extraction and environment configuration
- **Deployment Script:** One-command deployment with backend URL configuration
- **Enhanced API:** Comprehensive endpoints with detailed metrics and status

### Improved Frontend
- **Configurable Backend URL:** Easy backend URL updates via UI or config file
- **Enhanced Error Handling:** Retry mechanisms, timeout handling, and user feedback
- **Auto-Discovery:** Automatically finds and connects to available backends
- **Real-time Status:** Live system metrics and connection status
- **Session Management:** Automatic timeout and security features

## 🚀 Quick Start - Production Deployment

### Option 1: Automated Deployment (Recommended)
```bash
# Deploy everything with production backend URL
./deploy.sh --backend-url "https://euystacio-moonrise.onrender.com/"

# Or deploy specific components
./deploy.sh --component backend
./deploy.sh --component frontend
```

### Option 2: Manual Production Setup
```bash
# Extract components
python3 setup.py --component all

# Backend is already configured for production in deployed-backend/
# Frontend is already configured with production URL in deployed-frontend/config.js
```

### Option 3: Direct Production Deployment
1. **Backend**: Deploy `deployed-backend/` to Render.com as `euystacio-moonrise`
2. **Frontend**: Deploy `deployed-frontend/` to GitHub Pages
3. **Configuration**: URLs are pre-configured for production use

## 📁 Production Deployment Structure

The repository is organized for immediate production deployment:

- `deployed-backend/` - **Production-ready backend** for Render.com hosting
  - Configured with `debug=False` for production
  - Includes all necessary files: `app.py`, `euystacio.py`, `requirements.txt`
  - Uses JSON file storage for MVP (upgradeable to database)
- `deployed-frontend/` - **Production-ready frontend** for GitHub Pages hosting  
  - Pre-configured with production backend URL: `https://euystacio-moonrise.onrender.com/`
  - Includes enhanced UI with error handling and auto-discovery
- `DEPLOYMENT.md` - **Comprehensive deployment guide** with step-by-step instructions
- `API.md` - **Complete API documentation** for all endpoints

## 🔧 Production Configuration

### Backend Configuration
The production backend is configured in `deployed-backend/app.py`:
```python
# Production settings
app.run(host="0.0.0.0", port=5000, debug=False)

euystacio_config = {
    'memory_limit': 500,           # Maximum memory entries
    'base_learning_rate': 0.12,    # Base learning rate
    'adaptation_factor': 0.08,     # How quickly to adapt
    'volatility_threshold': 0.25   # Threshold for volatility-based adjustments
}
```

### Frontend Configuration
Production frontend is configured in `deployed-frontend/config.js`:
```javascript
window.EuystacioConfig = {
  backend: {
    url: "https://euystacio-moonrise.onrender.com/",
    fallbackUrls: ["http://localhost:5000"],
    timeout: 10000,
    maxRetries: 3
  },
  // ... additional production settings
};
```

### Storage Configuration

**Current Implementation (MVP)**: JSON File Storage
- Uses `pulse_log.json` for data persistence
- Simple, reliable for MVP deployment and testing
- No database setup or configuration required
- Suitable for moderate usage (hundreds to thousands of pulses)
- **Location**: Stored in the backend directory on the server filesystem
- **Format**: JSON array of pulse objects with timestamps and metadata

**Advantages of JSON Storage**:
- ✅ Zero setup complexity
- ✅ Human-readable data format
- ✅ Easy backup and migration
- ✅ No external dependencies
- ✅ Perfect for prototyping and MVP

**Limitations**:
- ⚠️ Single file may become large over time
- ⚠️ No concurrent write protection
- ⚠️ Limited query capabilities
- ⚠️ Data lost if server storage is reset

**Future Database Upgrade Path**:
For production scale and enhanced features, consider upgrading to:
- **PostgreSQL** (recommended for Render.com) - Full relational database with excellent performance
- **SQLite** - Lightweight option for smaller deployments
- **MongoDB** - NoSQL approach for flexible document storage
- **Redis** - For real-time caching and session management

**Migration Strategy**:
The current JSON structure is designed to be easily migrated to any database system. A future migration script will:
1. Read existing `pulse_log.json` data
2. Create appropriate database schema
3. Import all historical data
4. Update backend to use database instead of JSON files
- Easy migration path planned for future releases

- `deployed-backend/` - Enhanced backend ready for hosting (Render, Railway, etc.)
- `deployed-frontend/` - Enhanced frontend ready for web hosting (GitHub Pages, Netlify, etc.)
- `DEPLOYMENT.md` - Detailed deployment instructions
- `API.md` - Comprehensive API documentation

## 🔧 Configuration

### Backend Configuration
The enhanced kernel supports configuration via the `euystacio_config` in `app.py`:
```python
euystacio_config = {
    'memory_limit': 500,           # Maximum memory entries
    'base_learning_rate': 0.12,    # Base learning rate
    'adaptation_factor': 0.08,     # How quickly to adapt
    'volatility_threshold': 0.25   # Threshold for volatility-based adjustments
}
```

### Frontend Configuration
Configure the frontend via `config.js`:
```javascript
window.EuystacioConfig = {
  backend: {
    url: "https://your-backend.onrender.com",
    fallbackUrls: ["http://localhost:5000"],
    timeout: 10000,
    maxRetries: 3
  },
  // ... more options
};
```

## 📊 API Endpoints

The enhanced backend provides comprehensive API endpoints:

- `GET /` - API information and health check
- `POST /pulse` - Submit new pulse data (enhanced with kernel metrics)
- `GET /log` - Retrieve pulse entries (with filtering support)
- `GET /status` - Basic system status
- `GET /kernel` - Detailed kernel status and configuration
- `GET /metrics` - Performance metrics and analytics

See `API.md` for complete documentation.

## 🔐 Authentication

- **Username:** `hannesmitterer`
- **Password:** `moon-rise`
- **Session Timeout:** 15 minutes (configurable)

## 🧠 Enhanced Kernel Features

### Adaptive Learning
- Learning rate adjusts based on recent prediction accuracy
- Higher volatility increases learning rate for faster adaptation
- Stable periods reduce learning rate for consistency

### Memory Management
- Intelligent memory limits with important memory preservation
- Pattern-based memory consolidation
- Automatic cleanup of redundant entries

### Pattern Recognition
- Detects sentiment trends and cycles
- Stores significant patterns for future reference
- Adaptation score tracks system learning progress

### Performance Metrics
- Prediction error tracking
- Volatility analysis
- Memory efficiency monitoring
- Real-time adaptation scoring

## 📈 Monitoring

The system provides comprehensive monitoring:

- **Connection Status:** Real-time backend connectivity
- **System Metrics:** Memory usage, learning rate, adaptation score
- **Performance Data:** Prediction accuracy, volatility trends
- **Error Tracking:** Automatic retry and failure reporting

## 🔄 Migration from v1.0

If you have an existing Euystacio deployment:

1. Backup your current `pulse_log.json`
2. Run the deployment script to create enhanced versions
3. Copy your pulse log to the new `deployed-backend/` directory
4. Deploy the enhanced backend and frontend

The enhanced kernel is backward compatible with existing pulse data.

## 🛠️ Development

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Start backend
python3 app.py

# Open connect-enhanced.html in browser for testing
```

### Testing the Enhanced Kernel
```python
from euystacio import Euystacio

# Create enhanced kernel with custom config
config = {'memory_limit': 100, 'base_learning_rate': 0.15}
kernel = Euystacio(config=config)

# Test with various inputs
result = kernel.receive_input("test event", 0.5)
print("Kernel response:", result)
print("Full status:", kernel.get_status())
```

## 📖 Documentation

- `API.md` - Complete API documentation
- `DEPLOYMENT.md` - Comprehensive production deployment guide
- `PRODUCTION_CHECKLIST.md` - Step-by-step deployment checklist
- `config.js` - Frontend configuration options
- `validate_deployment.sh` - Deployment validation script
- `github-actions-template.yml` - GitHub Actions workflow template
- Inline code documentation for all enhanced features

## 🤖 Deployment Automation

### Validation Tools
```bash
# Validate production readiness
./validate_deployment.sh

# Manual configuration check
python3 /tmp/verify_config.py
```

### GitHub Actions Integration
Use the provided `github-actions-template.yml` to set up automatic frontend deployment:
1. Copy the template to `.github/workflows/deploy.yml` in your frontend repository
2. Customize the workflow for your specific needs
3. Enable GitHub Pages in repository settings
4. Push changes to trigger automatic deployment

### Scripts and Tools
- **`deploy.sh`** - Original deployment script with backend URL configuration
- **`validate_deployment.sh`** - Comprehensive validation of production readiness
- **`PRODUCTION_CHECKLIST.md`** - Detailed checklist for manual deployment
- **Configuration verification** - Automated consistency checks

## 🚀 Quick Production Deployment

For immediate production deployment:

1. **Validate Configuration:**
   ```bash
   ./validate_deployment.sh
   ```

2. **Deploy Backend to Render.com:**
   - Upload `deployed-backend/` directory
   - Set service name: `euystacio-moonrise`
   - Use start command: `python app.py`

3. **Deploy Frontend to GitHub Pages:**
   - Upload `deployed-frontend/` directory to repository
   - Enable GitHub Pages
   - Frontend will connect to: `https://euystacio-moonrise.onrender.com/`

4. **Test Deployment:**
   - Visit frontend URL
   - Test login: `hannesmitterer` / `moon-rise`
   - Verify pulse submission and data persistence

## 🤝 Contributing

This enhanced version maintains backward compatibility while adding significant new capabilities. Feel free to extend the kernel algorithms, add new API endpoints, or improve the frontend experience.

## 📋 Production Notes

### Storage
- **Current**: JSON file storage suitable for MVP
- **Future**: Database upgrade path documented for scaling
- **Backup**: Simple file-based backup for JSON storage

### Security
- **Authentication**: Basic username/password for demo
- **CORS**: Properly configured for cross-origin requests
- **Production**: Debug mode disabled in production build

### Monitoring
- **Health Checks**: Built-in status endpoints
- **Metrics**: Comprehensive performance monitoring
- **Logging**: JSON-based logging for easy analysis

---

✨ **Euystacio v2.0** - Production-ready self-evolving AI with intelligent deployment and robust integration
