from flask import Blueprint
import application.gas.gasRecord as gasRecord
from main.middleware import token_required

gas_bp = Blueprint('gas', __name__, url_prefix='/gas')

@gas_bp.route('/records', methods=['GET'])
@token_required
def get_gas_records():
    return gasRecord.fetch_gas_records()

@gas_bp.route('/charts', methods=['GET'])
@token_required
def get_gas_chart():
    return gasRecord.fetch_gas_chart()