from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "1.0.0")
COLOR = os.getenv("APP_COLOR", "blue")


@app.route("/")
def home():
    return jsonify({
        "application": "DevOps Production Demo",
        "version": VERSION,
        "deployment_color": COLOR,
        "hostname": socket.gethostname(),
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": VERSION
    }), 200


@app.route("/ready")
def ready():
    return jsonify({
        "status": "ready"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
