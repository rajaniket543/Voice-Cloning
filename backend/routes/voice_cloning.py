from flask import Blueprint, request, jsonify
import os
import uuid
from models.tts_engine import TTSEngine

voice_clone_bp = Blueprint("voice_clone", __name__)
tts_engine = TTSEngine()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@voice_clone_bp.route("/register", methods=["POST"])
def register_voice():
    if "audio" not in request.files:
        return jsonify({"error": "Audio file missing"}), 400

    audio = request.files["audio"]
    user_id = request.form.get("user_id")

    if not user_id:
        return jsonify({"error": "user_id required"}), 400

    filename = f"{user_id}_{uuid.uuid4()}.wav"
    path = os.path.join(UPLOAD_DIR, filename)
    audio.save(path)

    return jsonify({
        "success": True,
        "voice_id": path
    })


@voice_clone_bp.route("/synthesize", methods=["POST"])
def synthesize():
    data = request.get_json()
    text = data.get("text")
    voice_id = data.get("voice_id")
    language = data.get("language", "en")

    if not text or not voice_id:
        return jsonify({"error": "text and voice_id required"}), 400

    output = tts_engine.synthesize(text, voice_id, language)

    return jsonify({
        "success": True,
        "audio_path": output
    })
