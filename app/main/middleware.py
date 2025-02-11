from flask import request, jsonify
import jwt
from functools import wraps
import management.encryptpassword as encrypt

def log_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(f"[LOG] {request.method} {request.path} - Data: {request.json}")
        return f(*args, **kwargs)
    return decorated_function

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"message": "Token is missing"}), 401
        try:
            # decoded = jwt.decode(token.split()[1], cipher.SECRET_KEY, algorithms=["HS256"])
            request.user = encrypt.decode_token(token)
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token is invalid"}), 401
        return f(*args, **kwargs)
    return decorated