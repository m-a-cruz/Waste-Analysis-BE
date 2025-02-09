from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
import jwt
import datetime
from database import users_collection
from middleware import SECRET_KEY
import re
import os

bcrypt = Bcrypt()
auth_bp = Blueprint('auth', __name__)

# Encryption key required for user registration
# Store this in an environment variable in production
REGISTRATION_KEY = "my_secure_registration_key"

# Email validation function
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Register User
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    
    if not data or not all(key in data for key in ["name", "email", "password", "encryption_key"]):
        return jsonify({"error": "Missing required fields"}), 400

    if data["encryption_key"] != REGISTRATION_KEY:
        return jsonify({"error": "Invalid encryption key"}), 403

    if not is_valid_email(data["email"]):
        return jsonify({"error": "Invalid email format"}), 400

    if len(data["password"]) < 6:
        return jsonify({"error": "Password must be at least 6 characters long"}), 400

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    
    if users_collection.find_one({"email": data["email"]}):
        return jsonify({"error": "User already exists"}), 400
    
    user = {"name": data["name"], "email":data["email"], "password": hashed_password, "created_at": datetime.datetime.utcnow()}
    users_collection.insert_one(user)
    return jsonify({"message": "User registered successfully"}), 201

# Login User
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    
    if not data or not all(key in data for key in ["email", "password"]):
        return jsonify({"error": "Missing required fields"}), 400
    
    user = users_collection.find_one({"email": data["email"]})
    
    if not user or not bcrypt.check_password_hash(user["password"], data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401
    
    token = jwt.encode({"email": user["email"], "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token}), 200