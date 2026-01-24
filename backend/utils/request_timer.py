import time
from flask import request

def register_request_timer(app):
    @app.before_request
    def start_timer():
        request.start_time = time.time()

    @app.after_request
    def log_duration(response):
        duration = time.time() - request.start_time
        app.logger.info(f"{request.method} {request.path} - {duration:.3f}s")
        return response
