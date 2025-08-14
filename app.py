from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# Allow only your Firebase Hosting origins
CORS(app, resources={r"/*": {"origins": [
    "https://test-7a2b2.web.app",
    "https://test-7a2b2.firebaseapp.com"
]}})

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask on DigitalOcean!"})

@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify({"you_sent": data})

