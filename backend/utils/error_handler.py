import os

# filepath: /Users/aniket/Documents/GitHub/Voice-Cloning/backend/utils/error_handler.py
class AudioProcessingError(Exception):
    """Custom exception for audio processing errors"""
    pass

def handle_audio_error(func):
    """Decorator to handle audio processing errors"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            raise AudioProcessingError(f"Audio file not found: {args[0] if args else 'unknown'}")
        except Exception as e:
            raise AudioProcessingError(f"Audio processing failed: {str(e)}")
    return wrapper

def validate_audio_file(path):
    """Validate if audio file exists and is readable"""
    if not os.path.exists(path):
        raise AudioProcessingError(f"File does not exist: {path}")
    if not os.path.isfile(path):
        raise AudioProcessingError(f"Path is not a file: {path}")
    return True