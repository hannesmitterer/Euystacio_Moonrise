from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import json, os
import jwt
from functools import wraps

from euystacio import Euystacio

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SECRET_KEY'] = 'euystacio-moonrise-secret-key'  # Change this in production
euystacio = Euystacio()

PULSE_LOG_FILE = "pulse_log.json"
USERS_FILE = "users.json"


def load_pulse_log():
    if os.path.exists(PULSE_LOG_FILE):
        with open(PULSE_LOG_FILE, "r") as f:
            return json.load(f)
    return []


def save_pulse_log(log):
    with open(PULSE_LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)


def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')


def verify_token(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['username']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token missing'}), 401
        
        if token.startswith('Bearer '):
            token = token[7:]
        
        username = verify_token(token)
        if not username:
            return jsonify({'message': 'Token invalid or expired'}), 401
        
        return f(username, *args, **kwargs)
    return decorated


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400
    
    users = load_users()
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    
    users[username] = {
        'password': password,  # In production, hash this password
        'role': 'user',
        'created_at': datetime.utcnow().isoformat()
    }
    save_users(users)
    
    token = generate_token(username)
    return jsonify({
        'message': 'User registered successfully',
        'token': token,
        'username': username
    }), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400
    
    users = load_users()
    if username not in users or users[username]['password'] != password:
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = generate_token(username)
    return jsonify({
        'message': 'Login successful',
        'token': token,
        'username': username,
        'role': users[username].get('role', 'user')
    }), 200


@app.route("/pulse", methods=["POST"])
@token_required
def post_pulse(username):
    data = request.get_json()

    event = data.get("event", "Unnamed Pulse")
    sentiment = float(data.get("sentiment", 0))
    event_type = data.get("event_type", "general")
    users = load_users()
    role = users.get(username, {}).get('role', 'user')
    timestamp = datetime.utcnow().isoformat() + "Z"

    new_entry = {
        "timestamp": timestamp,
        "event": event,
        "sentiment": sentiment,
        "role": role,
        "user": username,
        "event_type": event_type,
    }

    pulse_log = load_pulse_log()
    pulse_log.append(new_entry)
    save_pulse_log(pulse_log)

    euystacio.receive_input(event, sentiment)

    return jsonify({
        "status": "ok",
        "balance_metric": euystacio.balance_metric,
        "memory_size": len(euystacio.memory)
    })


@app.route("/status", methods=["GET"])
def get_status():
    return jsonify({
        "status": "ok",
        "balance_metric": euystacio.balance_metric,
        "pulse_count": len(load_pulse_log())
    })


@app.route("/log", methods=["GET"])
def get_log():
    token = request.headers.get('Authorization')
    if token and token.startswith('Bearer '):
        token = token[7:]
        username = verify_token(token)
        if username:
            # Filter by user if authenticated
            pulse_log = load_pulse_log()
            user_pulses = [pulse for pulse in pulse_log if pulse.get('user') == username]
            return jsonify(user_pulses)
    
    # Return all pulses if not authenticated (for demo purposes)
    return jsonify(load_pulse_log())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
