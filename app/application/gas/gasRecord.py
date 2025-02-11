from flask import jsonify,Response
from bson import json_util
from infrastructure.database import gas_collection
from main.middleware import token_required

def fetch_gas_records():
    records = list(gas_collection.find())
    response = Response(json_util.dumps(records), mimetype='application/json')
    return response, 200

def fetch_gas_chart():
    gas_chart = {"CHART_URI": "https://charts.mongodb.com/charts-trashtalk-friltrw/embed/charts?id=e38f11b2-1149-45ae-97c0-e6895319f030&maxDataAge=3600&theme=dark&autoRefresh=true"}
    return jsonify(gas_chart), 200






























# For Gas Record from the Sensor
# @record_bp.route('/record', methods=['POST'])
# def record_gas_data():
#     data = request.json
#     gas_collection.insert_one(data)
#     return jsonify({"message": "Gas data recorded successfully"}), 201

