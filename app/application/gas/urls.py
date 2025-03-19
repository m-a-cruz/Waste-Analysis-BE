from flask import Blueprint
import application.gas.gasRecord as gasRecord
import application.gas.notification as notification
from management.middleware import token_required

gas_bp = Blueprint('gas', __name__, url_prefix='/gas')

@gas_bp.route('/charts', methods=['GET'])
@token_required
def get_gas_chart():
    return gasRecord.fetch_gas_chart()

@gas_bp.route('/notifications', methods=['GET'])
@token_required
def get_notifications():
    return notification.fetch_notif()

@gas_bp.route('/data', methods=['POST'])
def create_gas_records():
    return gasRecord.record_gas_level()

@gas_bp.route('/notification', methods=['POST'])
def create_notification():
    return notification.record_notif_data()