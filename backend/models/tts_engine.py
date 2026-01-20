class TTSEngine:
    def __init__(self):
        self.ready = True

    def is_ready(self):
        return self.ready

    def extract_voice_embedding(self, audio_path, user_id):
        return audio_path

    def synthesize(self, text, voice_id):
        return voice_id
