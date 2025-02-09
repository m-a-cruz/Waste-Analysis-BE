from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
import jwt
import datetime
from database import gas_collection
from middleware import SECRET_KEY

record_bp = Blueprint('record', __name__)


@record_bp.route('/records', methods=['GET'])
def get_gas_records():
    records = list(gas_collection.find())
    return jsonify(records), 200








# For Gas Record from the Sensor
# @record_bp.route('/record', methods=['POST'])
# def record_gas_data():
#     data = request.json
#     gas_collection.insert_one(data)
#     return jsonify({"message": "Gas data recorded successfully"}), 201

