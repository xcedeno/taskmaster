import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-super-secreta-dev'
    # Configuración JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'otra-clave-super-secreta-jwt'
    # Usamos SQLite por defecto para desarrollo rápido, pero listo para Postgres
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'taskmaster.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False