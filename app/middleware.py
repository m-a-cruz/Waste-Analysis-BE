from flask import request, jsonify
import jwt
from functools import wraps
import datetime

SECRET_KEY = 'secret'

# Logging Middleware
def log_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(f"[LOG] {request.method} {request.path} - Data: {request.json}")
        return f(*args, **kwargs)
    return decorated_function

#  JWT Authentication Middleware
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"message": "Token is missing"}), 401
        try:
            decoded = jwt.decode(token.split()[1], SECRET_KEY, algorithms=["HS256"])
            request.user = decoded
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token is invalid"}), 401
        return f(*args, **kwargs)
    return decorated

    