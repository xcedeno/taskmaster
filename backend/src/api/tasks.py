from flask import Blueprint, request, jsonify
from src.extensions import db
from src.models.task import Task
from src.models.user import User
from datetime import datetime

bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

@bp.route('', methods=['GET'])
def get_tasks():
    # En el futuro filtraremos por usuario logueado
    tasks = Task.query.all()
    # Usamos el método to_dict() que creamos en el modelo
    return jsonify([task.to_dict() for task in tasks]), 200

@bp.route('', methods=['POST'])
def create_task():
    data = request.get_json()
    
    # Validaciones
    if not data.get('title') or not data.get('user_id'):
        return jsonify({'error': 'Title and user_id are required'}), 400
        
    # Verificar que el usuario exista
    user = db.session.get(User, data['user_id'])
    if not user:
        return jsonify({'error': 'User not found'}), 404

    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        user_id=data['user_id'],
        priority=data.get('priority', 'Medium'),
        status='Pending',
        due_date=datetime.strptime(data['due_date'], '%Y-%m-%d') if data.get('due_date') else None
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify(new_task.to_dict()), 201