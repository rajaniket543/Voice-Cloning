from flask import Blueprint, jsonify
import torch

model_status_bp = Blueprint("model_status", __name__)

@model_status_bp.route("/models/status", methods=["GET"])
def model_status():
    return jsonify({
        "model": "XTTS v2",
        "device": "GPU" if torch.cuda.is_available() else "CPU",
        "ready": True
    })
