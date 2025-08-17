from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json, os

from euystacio import Euystacio

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Initialize enhanced Euystacio with custom configuration
euystacio_config = {
    'memory_limit': 500,
    'base_learning_rate': 0.12,
    'adaptation_factor': 0.08,
    'volatility_threshold': 0.25
}
euystacio = Euystacio(config=euystacio_config)

PULSE_LOG_FILE = "pulse_log.json"


def load_pulse_log():
    """Load pulse log from file."""
    if os.path.exists(PULSE_LOG_FILE):
        with open(PULSE_LOG_FILE, "r") as f:
            return json.load(f)
    return []


def save_pulse_log(log):
    """Save pulse log to file."""
    with open(PULSE_LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)


@app.route("/", methods=["GET"])
def api_info():
    """API information and health check."""
    return jsonify({
        "name": "Euystacio Backend API",
        "version": "2.0",
        "status": "healthy",
        "endpoints": {
            "POST /pulse": "Submit new pulse data",
            "GET /log": "Retrieve all pulse entries", 
            "GET /status": "Get system status",
            "GET /kernel": "Get detailed kernel status",
            "GET /metrics": "Get performance metrics",
            "GET /": "This API information"
        },
        "kernel_type": "Enhanced Euystacio v2.0"
    })


@app.route("/pulse", methods=["POST"])
def post_pulse():
    """Submit new pulse data to the system."""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400

        event = data.get("event", "Unnamed Pulse")
        sentiment = data.get("sentiment")
        
        if sentiment is None:
            return jsonify({"error": "Sentiment value required"}), 400
            
        try:
            sentiment = float(sentiment)
            if not -1 <= sentiment <= 1:
                return jsonify({"error": "Sentiment must be between -1 and 1"}), 400
        except (ValueError, TypeError):
            return jsonify({"error": "Invalid sentiment value"}), 400

        role = data.get("role", "visitor")
        user = data.get("user", "anonymous")
        timestamp = datetime.utcnow().isoformat() + "Z"

        new_entry = {
            "timestamp": timestamp,
            "event": event,
            "sentiment": sentiment,
            "role": role,
            "user": user,
        }

        # Save to pulse log
        pulse_log = load_pulse_log()
        pulse_log.append(new_entry)
        save_pulse_log(pulse_log)

        # Process with enhanced Euystacio kernel
        kernel_response = euystacio.receive_input(event, sentiment)

        return jsonify({
            "status": "success",
            "message": "Pulse processed successfully",
            "entry": new_entry,
            "kernel": kernel_response
        })
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


@app.route("/status", methods=["GET"])
def get_status():
    """Get basic system status."""
    try:
        pulse_count = len(load_pulse_log())
        kernel_status = euystacio.get_status()
        
        return jsonify({
            "status": "healthy",
            "pulse_count": pulse_count,
            "balance_metric": kernel_status['balance_metric'],
            "learning_rate": kernel_status['learning_rate'],
            "memory_usage": f"{kernel_status['memory_size']}/{kernel_status['config']['memory_limit']}",
            "total_inputs": kernel_status['total_inputs']
        })
        
    except Exception as e:
        return jsonify({"error": f"Status check failed: {str(e)}"}), 500


@app.route("/kernel", methods=["GET"])
def get_kernel_status():
    """Get detailed kernel status and metrics."""
    try:
        return jsonify(euystacio.get_status())
        
    except Exception as e:
        return jsonify({"error": f"Kernel status failed: {str(e)}"}), 500


@app.route("/metrics", methods=["GET"])
def get_metrics():
    """Get performance metrics and analytics."""
    try:
        pulse_log = load_pulse_log()
        kernel_status = euystacio.get_status()
        
        # Calculate additional metrics
        if pulse_log:
            sentiments = [entry['sentiment'] for entry in pulse_log]
            avg_sentiment = sum(sentiments) / len(sentiments)
            recent_sentiments = sentiments[-10:] if len(sentiments) >= 10 else sentiments
            recent_avg = sum(recent_sentiments) / len(recent_sentiments) if recent_sentiments else 0
        else:
            avg_sentiment = 0
            recent_avg = 0
        
        return jsonify({
            "total_pulses": len(pulse_log),
            "average_sentiment": round(avg_sentiment, 3),
            "recent_average_sentiment": round(recent_avg, 3),
            "kernel_metrics": {
                "balance_metric": kernel_status['balance_metric'],
                "learning_rate": kernel_status['learning_rate'],
                "adaptation_score": kernel_status['adaptation_score'],
                "average_prediction_error": kernel_status['average_prediction_error'],
                "average_volatility": kernel_status['average_volatility']
            },
            "memory_efficiency": {
                "used": kernel_status['memory_size'],
                "limit": kernel_status['config']['memory_limit'],
                "usage_percent": round(100 * kernel_status['memory_size'] / kernel_status['config']['memory_limit'], 1)
            }
        })
        
    except Exception as e:
        return jsonify({"error": f"Metrics calculation failed: {str(e)}"}), 500


@app.route("/log", methods=["GET"])
def get_log():
    """Retrieve all pulse entries with optional filtering."""
    try:
        pulse_log = load_pulse_log()
        
        # Optional query parameters for filtering
        limit = request.args.get('limit', type=int)
        user_filter = request.args.get('user')
        role_filter = request.args.get('role')
        
        # Apply filters
        filtered_log = pulse_log
        
        if user_filter:
            filtered_log = [entry for entry in filtered_log if entry.get('user') == user_filter]
            
        if role_filter:
            filtered_log = [entry for entry in filtered_log if entry.get('role') == role_filter]
            
        if limit and limit > 0:
            filtered_log = filtered_log[-limit:]
        
        return jsonify({
            "entries": filtered_log,
            "total_count": len(pulse_log),
            "filtered_count": len(filtered_log)
        })
        
    except Exception as e:
        return jsonify({"error": f"Log retrieval failed: {str(e)}"}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Endpoint not found", "available_endpoints": [
        "GET /", "POST /pulse", "GET /log", "GET /status", "GET /kernel", "GET /metrics"
    ]}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors."""
    return jsonify({"error": "Method not allowed"}), 405


if __name__ == "__main__":
    # Production configuration - disable debug mode
    app.run(host="0.0.0.0", port=5000, debug=False)
