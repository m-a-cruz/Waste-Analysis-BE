from flask import Flask, jsonify, request
from flask_cors import CORS
from application.auth.urls import auth_bp
from application.forgot.urls import reset_bp
from application.gas.urls import gas_bp
from management.middleware import log_request, token_required

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.before_request
def before_request():
    log_request(request)
    
@app.route("/protected", methods=["GET"])
@token_required
def protected_route():
    return jsonify({"message": f"Welcome user!"}), 200

app.register_blueprint(auth_bp)
app.register_blueprint(reset_bp)
app.register_blueprint(gas_bp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)