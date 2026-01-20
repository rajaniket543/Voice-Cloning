from flask import Flask, jsonify
from flask_cors import CORS
from routes.voice_cloning import voice_clone_bp
from routes.health import health_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(voice_clone_bp, url_prefix="/api/voice-clone")
app.register_blueprint(health_bp)

@app.route("/")
def home():
    return jsonify({
        "service": "Personal Voice Studio Backend",
        "status": "running"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
