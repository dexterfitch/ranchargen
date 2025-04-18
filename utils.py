import os
from flask import request, jsonify # type: ignore
from functools import wraps

ADMIN_TOKEN = os.environ["ADMIN_TOKEN"]

def require_admin_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("x-admin-token")
        if token != ADMIN_TOKEN:
            return jsonify({"error": "Unauthorized"}), 403
        return f(*args, **kwargs)
    return decorated_function