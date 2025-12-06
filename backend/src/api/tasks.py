from flask import Blueprint, request, jsonify
from src.extensions import db
from src.models.task import Task
from flask_jwt_extended import jwt_required, get_jwt_identity # Importar JWT tools
from datetime import datetime

bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

@bp.route('', methods=['GET'])
@jwt_required() # <--- ESCUDO PROTECTOR
def get_tasks():
    # Obtener el ID del usuario actual desde el token
    current_user_id = get_jwt_identity()
    
    # Solo traemos las tareas de ESE usuario
    tasks = Task.query.filter_by(user_id=current_user_id).all()
    return jsonify([task.to_dict() for task in tasks]), 200

@bp.route('', methods=['POST'])
@jwt_required() # <--- ESCUDO PROTECTOR
def create_task():
    current_user_id = get_jwt_identity() # Ya no necesitamos que el frontend nos mande el ID
    data = request.get_json()
    
    if not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400
        
    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        user_id=current_user_id, # Usamos el ID del token, es más seguro
        priority=data.get('priority', 'Medium'),
        status='Pending',
        due_date=datetime.strptime(data['due_date'], '%Y-%m-%d') if data.get('due_date') else None
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify(new_task.to_dict()), 201