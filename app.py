from flask import Flask, jsonify
import time

app = Flask(__name__)

start_time = time.time()

@app.route("/")
def home():
    return "Hello DevOps! App is running"

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/metrics")
def metrics():
    uptime = time.time() - start_time
    return f"app_uptime_seconds {uptime}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
