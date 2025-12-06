from flask import Flask
from flask_cors import CORS
from src.config import Config
from src.extensions import db, migrate

# Importamos los modelos para que Flask-Migrate los detecte
from src.models.user import User
from src.models.task import Task

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar extensiones
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar Blueprints (Rutas) - Lo haremos en el Sprint 3
    from src.api import users, tasks
    app.register_blueprint(users.bp)
    app.register_blueprint(tasks.bp)

    @app.route('/api/health')
    def health_check():
        return {"status": "ok", "db": "connected"}

    return app