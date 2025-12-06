# 🚀 TaskMaster Core

> **Plataforma de gestión de tareas escalable, modular y containerizada.**

![TaskMaster Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

TaskMaster es una solución **Full-Stack** moderna diseñada para adaptarse a flujos de trabajo administrativos, de soporte técnico y gestión de proyectos. Su arquitectura desacoplada y basada en microservicios permite escalar módulos independientemente.

---

## 🛠 Tech Stack

El proyecto utiliza tecnologías de vanguardia para asegurar rendimiento y escalabilidad:

### Backend & Database
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)

### Frontend
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Axios](https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white)

### Infraestructura
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)

---

## 📦 Instalación y Despliegue

### Requisitos previos
*   🐋 **Docker Desktop** instalado y ejecutándose.
*   🐙 **Git** para control de versiones.

### ⚡ Inicio Rápido (Modo Desarrollo)

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/xcedeno/taskmaster.git
    cd taskmaster
    ```

2.  **Iniciar servicios con Docker Compose:**
    ```bash
    docker-compose up --build
    ```

---

## 📅 Changelog

Detalle de versiones y nuevas funcionalidades implementadas.

| Versión | Fecha | Descripción |
| :--- | :--- | :--- |
| **0.6.0** | 2025-12-06 | **Frontend Auth System:** Login, AuthContext, JWT en Axios, Logout, UI Condicional. |
| **0.5.0** | 2025-12-06 | **Security & Auth:** JWT Backend, Hashing contraseñas, Endpoints protegidos. |
| **0.4.0** | 2025-12-06 | **Frontend Integration:** Axios client, Componentes UI (TaskCard, TaskForm), Service Layer. |
| **0.3.0** | 2025-12-06 | **API Endpoints:** CRUD Usuarios y Tareas, Blueprint Architecture. |
| **0.2.0** | 2025-12-06 | **DB Arch:** SQLAlchemy, Modelos (User, Task), Config Factory. |
| **0.1.0** | 2025-12-06 | **Init:** Estructura inicial Docker, Flask y React+Vite setup. |

---

## 🏁 Estado del Proyecto

Hitos alcanzados para la versión 1.0:

- [x] ✅ **Infraestructura Dockerizada** (Frontend + Backend).
- [x] ✅ **Base de Datos Relacional** con SQLAlchemy.
- [x] ✅ **API RESTful Segura** con JWT.
- [x] ✅ **Frontend Reactivo** con Vite y React Context.
- [x] ✅ **Despliegue Local** exitoso.