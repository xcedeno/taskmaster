from flask import Blueprint, request, jsonify
from src.extensions import db
from src.models.user import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    # Verificamos si el usuario existe y si la contraseña coincide con el hash
    if user and check_password_hash(user.password_hash, password):
        # Creamos el token (identity es lo que guardamos dentro del token, usualmente el ID)
        access_token = create_access_token(identity=str(user.id))
        return jsonify(access_token=access_token, user={"id": user.id, "username": user.username}), 200

    return jsonify({"error": "Bad username or password"}), 401