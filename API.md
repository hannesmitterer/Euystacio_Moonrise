# Euystacio Backend API Documentation

## Overview

The Euystacio Backend API provides endpoints for managing pulse data and interacting with the enhanced Euystacio kernel, which features self-evolving behavior with adaptive learning.

**Base URL:** `https://your-backend-url.com`  
**API Version:** 2.0  
**Content-Type:** `application/json`

## Authentication

Currently uses simple username/password authentication through the frontend:
- **Username:** `hannesmitterer`
- **Password:** `moon-rise`

## API Endpoints

### GET `/`
**Description:** API information and health check  
**Parameters:** None  
**Response:**
```json
{
  "name": "Euystacio Backend API",
  "version": "2.0",
  "status": "healthy",
  "endpoints": {...},
  "kernel_type": "Enhanced Euystacio v2.0"
}
```

### POST `/pulse`
**Description:** Submit new pulse data to the system  
**Content-Type:** `application/json`

**Request Body:**
```json
{
  "event": "string (required) - Description of the event",
  "sentiment": "float (required) - Sentiment value between -1 and 1",
  "role": "string (optional) - User role (default: 'visitor')",
  "user": "string (optional) - Username (default: 'anonymous')"
}
```

**Response (Success):**
```json
{
  "status": "success",
  "message": "Pulse processed successfully",
  "entry": {
    "timestamp": "2024-01-01T12:00:00Z",
    "event": "Test event",
    "sentiment": 0.5,
    "role": "tutor",
    "user": "hannesmitterer"
  },
  "kernel": {
    "balance_metric": 0.45,
    "learning_rate": 0.12,
    "volatility": 0.15,
    "adaptation_score": 0.8,
    "memory_size": 150,
    "prediction_error": 0.05,
    "average_error": 0.08
  }
}
```

**Response (Error):**
```json
{
  "error": "Error description"
}
```

### GET `/log`
**Description:** Retrieve pulse entries with optional filtering  
**Parameters:**
- `limit` (integer, optional) - Maximum number of entries to return
- `user` (string, optional) - Filter by username
- `role` (string, optional) - Filter by user role

**Response:**
```json
{
  "entries": [
    {
      "timestamp": "2024-01-01T12:00:00Z",
      "event": "Test event",
      "sentiment": 0.5,
      "role": "tutor",
      "user": "hannesmitterer"
    }
  ],
  "total_count": 100,
  "filtered_count": 50
}
```

### GET `/status`
**Description:** Get basic system status  
**Parameters:** None

**Response:**
```json
{
  "status": "healthy",
  "pulse_count": 150,
  "balance_metric": 0.45,
  "learning_rate": 0.12,
  "memory_usage": "150/500",
  "total_inputs": 150
}
```

### GET `/kernel`
**Description:** Get detailed kernel status and configuration  
**Parameters:** None

**Response:**
```json
{
  "balance_metric": 0.45,
  "learning_rate": 0.12,
  "adaptation_score": 0.8,
  "memory_size": 150,
  "total_inputs": 150,
  "average_prediction_error": 0.08,
  "average_volatility": 0.15,
  "pattern_count": 5,
  "recent_patterns": [...],
  "config": {
    "memory_limit": 500,
    "base_learning_rate": 0.12,
    "adaptation_factor": 0.08,
    "volatility_threshold": 0.25
  }
}
```

### GET `/metrics`
**Description:** Get performance metrics and analytics  
**Parameters:** None

**Response:**
```json
{
  "total_pulses": 150,
  "average_sentiment": 0.25,
  "recent_average_sentiment": 0.30,
  "kernel_metrics": {
    "balance_metric": 0.45,
    "learning_rate": 0.12,
    "adaptation_score": 0.8,
    "average_prediction_error": 0.08,
    "average_volatility": 0.15
  },
  "memory_efficiency": {
    "used": 150,
    "limit": 500,
    "usage_percent": 30.0
  }
}
```

## Enhanced Kernel Features

The Euystacio v2.0 kernel includes several advanced features:

### Adaptive Learning
- **Dynamic Learning Rate:** Automatically adjusts based on volatility and prediction accuracy
- **Volatility Detection:** Recognizes periods of instability and adapts accordingly
- **Momentum Calculation:** Considers recent trends in sentiment data

### Memory Management
- **Intelligent Cleanup:** Preserves important memories while managing size limits
- **Pattern Recognition:** Identifies and stores significant sentiment patterns
- **Consolidation:** Merges similar memories to optimize storage

### Self-Evolution
- **Prediction Tracking:** Monitors accuracy and adjusts algorithms
- **Adaptation Score:** Measures how well the system adapts to new patterns
- **Configuration Tuning:** Automatically optimizes parameters based on data characteristics

## Error Codes

- `400` - Bad Request (invalid parameters, missing required fields)
- `404` - Endpoint not found
- `405` - Method not allowed
- `500` - Internal server error

## CORS Support

The API includes CORS headers to support cross-origin requests from web frontends.

## Rate Limiting

Currently no rate limiting is implemented, but consider implementing it for production use.

## Deployment Notes

- Ensure `requirements.txt` includes `Flask-CORS==4.0.0`
- Configure environment variables for production settings
- Consider using a production WSGI server like Gunicorn
- Set up proper logging and monitoring

## Examples

### Submit a Pulse
```bash
curl -X POST https://your-backend-url.com/pulse \
  -H "Content-Type: application/json" \
  -d '{
    "event": "Completed lesson on quantum physics",
    "sentiment": 0.8,
    "role": "tutor",
    "user": "hannesmitterer"
  }'
```

### Get Recent Pulses
```bash
curl "https://your-backend-url.com/log?limit=10&user=hannesmitterer"
```

### Check System Status
```bash
curl https://your-backend-url.com/status
```