from flask import Blueprint, request, jsonify
from src.extensions import db
from src.models.user import User
from werkzeug.security import generate_password_hash


# Definimos el Blueprint
bp = Blueprint('users', __name__, url_prefix='/api/users')

@bp.route('', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # Validación básica
    if not data.get('username') or not data.get('email'):
        return jsonify({'error': 'Username and email are required'}), 400
    
    # Verificar si ya existe
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'User already exists'}), 400

    # Hash de la contraseña
    hashed_password = generate_password_hash(data['password'])

    # Crear usuario
    new_user = User(
        username=data['username'],
        email=data['email'],
        password_hash=hashed_password,
        role=data.get('role', 'user')
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({
        'message': 'User created successfully',
        'user': {'id': new_user.id, 'username': new_user.username}
    }), 201

@bp.route('', methods=['GET'])
def get_users():
    users = User.query.all()
    results = [{'id': u.id, 'username': u.username, 'role': u.role} for u in users]
    return jsonify(results), 200