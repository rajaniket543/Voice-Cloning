# 🎙️ Personal Voice Studio

Personal Voice Studio is a full-stack voice cloning application that allows users to record their voice and generate realistic speech from text using zero-shot voice cloning.

The project combines a Flutter mobile frontend, a Flask-based Python backend, and Coqui XTTS v2, a state-of-the-art multilingual text-to-speech model.

---

## ✨ Features

- Record short voice samples (no training required)
- Zero-shot voice cloning using XTTS v2
- Convert text to speech in the user’s own voice
- Multi-language speech synthesis
- Adjustable speech speed
- Clean mobile UI built with Flutter
- REST API backend with Flask
- Ready for cloud deployment (Render / Railway / AWS)

---

## 🧱 Architecture Overview

Flutter Mobile App → Flask REST API → XTTS v2 → Generated Audio Output

Frontend handles recording, text input, and playback.  
Backend processes audio, extracts speaker embeddings, and runs speech synthesis.

---

## 🛠️ Tech Stack

Frontend:
- Flutter (Dart)
- record
- audioplayers
- provider
- http

Backend:
- Python 3.9+
- Flask + Flask-CORS
- Coqui TTS (XTTS v2)
- PyTorch
- librosa, numpy

Infrastructure:
- REST-based architecture
- GPU-supported inference (recommended)
- Firebase-ready for audio storage (optional)

---

## 📁 Project Structure

personal-voice-studio/
├── backend/                 # Flask + XTTS backend
│   ├── app.py
│   ├── models/
│   ├── routes/
│   ├── utils/
│   └── README.md
│
├── frontend/
│   └── personal_voice_studio/
│       ├── lib/
│       ├── android/
│       ├── ios/
│       └── README.md
│
├── .gitignore
└── README.md

---

## 🚀 Getting Started

Backend setup:

cd backend  
python -m venv venv  
source venv/bin/activate   # Windows: venv\Scripts\activate  
pip install -r requirements.txt  

Create a .env file based on .env.example, then run:

python app.py  

Backend runs at:  
http://localhost:5000

---

Frontend setup:

cd frontend/personal_voice_studio  
flutter pub get  
flutter run  

Ensure the backend URL is correctly configured in the Flutter app.

---

## 🔐 Security Notes

- Model weights are not included in the repository
- Audio files and generated outputs are ignored via .gitignore
- Environment variables are managed using .env (never committed)
- Intended for educational and research use

---

## ⚠️ Limitations

- GPU is strongly recommended for real-time synthesis
- Long text synthesis may be slow on CPU
- No authentication or rate limiting implemented

---

## 🔮 Future Enhancements

- User authentication (JWT / Firebase Auth)
- Emotion-based speech synthesis
- Real-time streaming audio generation
- Usage analytics and quality metrics
- Full cloud storage integration

---

## 📌 Disclaimer

This project demonstrates voice cloning technology.  
User consent and ethical use are mandatory when working with voice data.

---

## 👤 Author

Built by Anu  
Computer Science Student  
Focused on backend systems, ML integration, and scalable architectures.
