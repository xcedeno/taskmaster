from src.extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128)) # Guardaremos hash, nunca texto plano
    role = db.Column(db.String(20), default='user') # admin, support, user
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación: Un usuario tiene muchas tareas
    tasks = db.relationship('Task', backref='assignee', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'