# 🚀 TaskMaster Core

> Plataforma de gestión de tareas escalable, modular y containerizada.

TaskMaster es una solución Full-Stack diseñada para adaptarse a flujos de trabajo administrativos, de soporte técnico y gestión de proyectos. Su arquitectura desacoplada permite escalar módulos independientemente.

## 🛠 Tech Stack

- **Backend:** Python 3.11, Flask (App Factory Pattern), SQLAlchemy.
- **Frontend:** React 18, Vite, TailwindCSS (Propuesta), Axios.
- **Database:** PostgreSQL (Production), SQLite (Dev/Testing).
- **Infraestructura:** Docker & Docker Compose.

## 📦 Instalación y Despliegue

### Requisitos previos
- Docker Desktop instalado.
- Git.

### Inicio Rápido (Modo Desarrollo)

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/xcedeno/taskmaster.git](https://github.com/xcedeno/taskmaster.git)
   cd taskmaster

### Cambios
    ### [0.1.0] - 2025-12-06
#### Added
- **Infraestructura Docker:** Configuración inicial de `docker-compose` para orquestar servicios.
- **Backend Service:** Configuración de Flask con `flask-cors` y Dockerfile basado en Python 3.11-slim. Habilitado endpoint `/api/health` para pruebas de conectividad.
- **Frontend Service:** Inicialización de proyecto React + Vite con Dockerfile basado en Node 20-alpine. Configuración de `vite.config.js` para soporte de Hot Reloading en contenedores.

### [0.2.0] - 2025-12-06
#### Added
- **Database Architecture:** Implementación de SQLAlchemy y Flask-Migrate.
- **Data Models:**
  - `User`: Soporte para roles y autenticación.
  - `Task`: Soporte para prioridades, estados y asignación.
- **Config:** Sistema de configuración centralizado (`config.py`) y patrón Application Factory.