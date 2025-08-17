from flask import Flask, request, jsonify
from datetime import datetime
import json, os

from euystacio import Euystacio

app = Flask(__name__)
euystacio = Euystacio()

PULSE_LOG_FILE = "pulse_log.json"


def load_pulse_log():
    if os.path.exists(PULSE_LOG_FILE):
        with open(PULSE_LOG_FILE, "r") as f:
            return json.load(f)
    return []


def save_pulse_log(log):
    with open(PULSE_LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)


@app.route("/pulse", methods=["POST"])
def post_pulse():
    data = request.get_json()

    event = data.get("event", "Unnamed Pulse")
    sentiment = float(data.get("sentiment", 0))
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
    return jsonify(load_pulse_log())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
