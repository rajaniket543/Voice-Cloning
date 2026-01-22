import librosa

def get_audio_duration(path):
    try:
        return librosa.get_duration(filename=path)
    except:
        return 0
