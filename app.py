from flask import Flask, jsonify, render_template, request, Response
from datetime import datetime
import csv, io
from src.fault_detection import classify_status
from src.sensor_simulator import generate_reading

app = Flask(__name__)
history = []
MAX_HISTORY = 250

def make_record(mode="AUTO"):
    reading = generate_reading(mode)
    status, message = classify_status(reading.get("current"), reading.get("temperature"))
    record = {"id": len(history) + 1, "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
              "current": reading.get("current"), "temperature": reading.get("temperature"),
              "status": status, "message": message}
    history.append(record)
    if len(history) > MAX_HISTORY: del history[:-MAX_HISTORY]
    return record

@app.get("/")
def index(): return render_template("index.html")

@app.get("/api/status")
def api_status():
    latest = history[-1] if history else None
    counts = {key: sum(1 for item in history if item["status"] == key) for key in ["NORMAL", "WARNING", "CRITICAL", "SENSOR FAULT"]}
    return jsonify({"latest": latest, "history": history[-50:], "counts": counts})

@app.post("/api/readings")
def api_readings():
    payload = request.get_json(silent=True) or {}
    mode = str(payload.get("mode", "AUTO")).upper()
    if mode not in {"AUTO", "NORMAL", "WARNING", "CRITICAL", "SENSOR FAULT"}:
        return jsonify({"error": "Unsupported simulation mode"}), 400
    return jsonify(make_record(mode))

@app.post("/api/clear")
def api_clear():
    history.clear()
    return jsonify({"ok": True})

@app.get("/api/export.csv")
def export_csv():
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["id", "timestamp", "current", "temperature", "status", "message"])
    writer.writeheader(); writer.writerows(history)
    return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition": "attachment; filename=electrical-monitor-history.csv"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
