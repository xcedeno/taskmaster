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

### [0.3.0] - 2025-12-06 
#### Added
- **API Endpoints:**
  - `POST /api/users`: Registro de usuarios.
  - `GET /api/users`: Listado de usuarios.
  - `POST /api/tasks`: Creación de tareas con validación de relaciones.
  - `GET /api/tasks`: Listado general de tareas con serialización JSON.
- **Architecture:** Implementación modular con Flask Blueprints (`src/api/`).

### [0.4.0] - 2025-12-06
#### Added
- **Frontend Integration:** Implementación de cliente HTTP con `axios`.
- **UI Components:**
  - `TaskCard`: Renderizado visual de tareas.
  - `TaskForm`: Formulario para creación de tareas.
- **Service Layer:** Configuración centralizada de API en `src/services/api.js`.

### [0.5.0] - 2025-12-06
#### Added
- **Security & Auth:**
  - Implementación de JWT (JSON Web Tokens) con `flask-jwt-extended`.
  - Hashing de contraseñas usando `Werkzeug` (scrypt).
  - Endpoints protegidos (`@jwt_required`) para creación y lectura de tareas.
- **API Endpoints:**
  - `POST /api/auth/login`: Autenticación y generación de tokens.
  - Actualización de `POST /api/users`: Ahora guarda contraseñas encriptadas.

  ### [0.6.0] - 2025-12-06
#### Added
- **Frontend Auth System:**
  - `AuthContext`: Estado global para manejo de sesión de usuario.
  - `LoginPage`: Interfaz de usuario para inicio de sesión.
  - Persistencia de sesión mediante `localStorage`.
- **API Integration:**
  - **Axios Interceptor:** Inyección automática del Token JWT en los headers de cada petición.
  - Manejo de errores 401 (Logout automático).
- **UX/UI:**
  - Renderizado condicional (Dashboard vs. Login).
  - Botón de Logout funcional.

---
## 🏁 Hitos del Proyecto 1 (TaskMaster)
- [x] Infraestructura Dockerizada (Frontend + Backend).
- [x] Base de Datos Relacional con SQLAlchemy.
- [x] API RESTful segura con JWT.
- [x] Frontend Reactivo con Vite y React Context.
- [x] Despliegue en entorno local exitoso.