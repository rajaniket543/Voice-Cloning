import os

ALLOWED_EXTENSIONS = {"wav", "mp3", "m4a"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
