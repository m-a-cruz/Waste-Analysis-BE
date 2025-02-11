from flask import request, jsonify
import datetime
from infrastructure.database import users_collection
import re
import management.cipherprivatekey as cipher
import management.encryptpassword as encrypt

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def register():
    data = request.json
    
    if not data or not all(key in data for key in ["name", "email", "password", "encryption_key"]):
        return jsonify({"error": "Missing required fields"}), 400

    if data["encryption_key"] != cipher.REGISTRATION_KEY:
        return jsonify({"error": "Invalid encryption key"}), 403

    if not is_valid_email(data["email"]):
        return jsonify({"error": "Invalid email format"}), 400

    if len(data["password"]) < 6:
        return jsonify({"error": "Password must be at least 6 characters long"}), 400
    
    if users_collection.find_one({"email": data["email"]}):
        return jsonify({"error": "User already exists"}), 400
    
    user = {"name": data["name"], "email":data["email"], 
            "password": encrypt.hash_password(data["password"]), "created_at": datetime.datetime.utcnow()}
    users_collection.insert_one(user)
    return jsonify({"message": "User registered successfully"}), 201

def login():
    data = request.json
    
    if not data or not all(key in data for key in ["email", "password"]):
        return jsonify({"error": "Missing required fields"}), 400
    
    user = users_collection.find_one({"email": data["email"]})
    
    if not user or not encrypt.check_password(user["password"], data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401
    
    return jsonify({"token": encrypt.generate_token(user["email"])}), 200