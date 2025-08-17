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

## 🚀 Quick Start

### Option 1: Automated Deployment (Recommended)
```bash
# Deploy everything with custom backend URL
./deploy.sh --backend-url "https://your-backend.onrender.com"

# Or deploy specific components
./deploy.sh --component backend
./deploy.sh --component frontend
```

### Option 2: Manual Setup
```bash
# Extract components
python3 setup.py --component all

# Update backend URL in frontend
# Edit deployed-frontend/config.js or use the UI
```

## 📁 Deployment Structure

After running the deployment script, you'll have:

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
- `DEPLOYMENT.md` - Generated deployment instructions
- `config.js` - Frontend configuration options
- Inline code documentation for all enhanced features

## 🤝 Contributing

This enhanced version maintains backward compatibility while adding significant new capabilities. Feel free to extend the kernel algorithms, add new API endpoints, or improve the frontend experience.

---

✨ **Euystacio v2.0** - Self-evolving AI with intelligent deployment and robust integration
