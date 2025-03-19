from flask import Blueprint
import application.auth.auth as auth

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def get_gas_records():
    return auth.register()

@auth_bp.route('/login', methods=['POST'])
def get_gas_chart():
    return auth.login()