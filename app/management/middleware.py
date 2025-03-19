from flask import request, jsonify
import jwt
from functools import wraps
import management.encryptpassword as encrypt

def log_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        data = request.json if request.is_json else None
        print(f"[LOG] {request.method} {request.path} - Data: {data}")
        return f(*args, **kwargs)
    return decorated_function


# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.headers.get("Authorization")

#         if not token:
#             return jsonify({"message": "Token is missing"}), 401
        
#         # Check if token follows "Bearer <token>" format
#         if "Bearer" in token:
#             token = token.split()[1]
        
#         try:
#             # Decode the token using a secret key and validate algorithm
#             decoded = jwt.decode(token, encrypt.SECRET_KEY, algorithms=["HS256"])
#             request.user = decoded  # Save decoded user data in request
#         except jwt.ExpiredSignatureError:
#             return jsonify({"message": "Token expired!"}), 401
#         except jwt.InvalidTokenError:
#             return jsonify({"message": "Token is invalid"}), 401
        
#         return f(*args, **kwargs)
#     return decorated


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