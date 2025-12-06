from src.extensions import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Estados adaptables: Pending, In Progress, Review, Done
    status = db.Column(db.String(20), default='Pending') 
    priority = db.Column(db.String(20), default='Medium') # Low, Medium, High, Urgent
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=True)
    
    # Clave Foránea (Foreign Key)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'status': self.status,
            'assignee': self.assignee.username
        }