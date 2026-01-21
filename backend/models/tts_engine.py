from TTS.api import TTS
import torch
import os
from datetime import datetime

class TTSEngine:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_name = "tts_models/multilingual/multi-dataset/xtts_v2"

        self.tts = TTS(self.model_name, gpu=self.device == "cuda")

        os.makedirs("voice_embeddings", exist_ok=True)
        os.makedirs("generated_audio", exist_ok=True)

    def extract_voice_embedding(self, audio_path, voice_id):
        # XTTS uses reference audio directly, no explicit embedding step
        return audio_path

    def synthesize(self, text, speaker_wav, language="en"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"generated_audio/speech_{timestamp}.wav"

        self.tts.tts_to_file(
            text=text,
            speaker_wav=speaker_wav,
            language=language,
            file_path=output_path
        )

        return output_path
