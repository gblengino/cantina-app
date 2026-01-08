🌎 **Read this in:** [English](README.md) | [Español](README.es.md)

# Sistema de Gestión de Cantina

Backend para una aplicación de escritorio destinada a la gestión de una cantina.

Este proyecto se encuentra actualmente en desarrollo y está pensado para comenzar como una **aplicación local** (offline, en una sola máquina), con una arquitectura de backend diseñada para poder adaptarse fácilmente a un futuro sistema **online y multiusuario**.

---

## 🚀 Objetivos del Proyecto

- Gestión de productos y stock
- Registro de ventas y sus ítems
- Autenticación de usuarios y manejo de roles
- Soporte para borrado lógico y auditoría (created_at, is_active)
- Mantener una arquitectura de backend limpia y escalable

---

## 🧱 Tecnologías Utilizadas

- **Python**
- **Flask**
- **SQLAlchemy**
- **Marshmallow**
- **JWT (Flask-JWT-Extended)**
- **SQLite** (inicialmente, para uso local)

---

## 🏗️ Arquitectura

El backend sigue una arquitectura **Service–Repository**:

```
backend/
├── routes/ # Endpoints de la API (Flask Blueprints)
├── services/ # Lógica de negocio y validaciones
├── repositories/ # Capa de acceso a datos
├── models/ # Modelos de SQLAlchemy
├── schemas/ # Esquemas Marshmallow (entrada/salida)
├── constants/ # Constantes y enums (ej. roles)
├── utils/ # Utilidades y helpers compartidos
└── extensions/ # DB, JWT, etc.
```

Esta estructura permite:
- separación clara de responsabilidades
- mayor facilidad para testear
- escalabilidad a futuro

---

## 🔐 Autenticación y Roles

La API utiliza autenticación basada en **JWT**.

Roles previstos:
- `admin`
- `cashier` (gestión de la caja)
- `stock_manager` (gestión de productos y stock)

Los roles se validan a nivel de servicios y se aplican en la capa de rutas.

---

## 🖥️ Frontend (WIP)

El proyecto incluye una aplicación frontend ubicada en el directorio `frontend/`.

- Desarrollada con **React** y **Vite**
- Pensada para ser empaquetada junto al backend utilizando **Electron**
- Actualmente en una etapa temprana de desarrollo y sin integración con la API

El frontend se considera **trabajo en progreso** y su estructura puede cambiar a medida que el proyecto evolucione.

---

## 📦 Estado Actual

✔ Modelos de base de datos  
✔ Esquemas (auth, usuarios, productos, ventas)  
⏳ Servicios  
⏳ Rutas / Endpoints  
⏳ Tests  

---

## 🧪 Notas de Desarrollo

- El proyecto utiliza un flujo de trabajo basado en **feature branches**
- `main` representa un estado estable
- `develop` es la rama de integración
- Las funcionalidades se desarrollan en ramas `feature/*` y se integran mediante Pull Requests

---

## 📌 Mejoras Futuras

- Soporte online / multiusuario
- Control de acceso basado en roles (RBAC)
- Tests automatizados
- Documentación de la API (OpenAPI / Swagger)
- Dockerización

---

## 📄 Licencia

Proyecto de uso educativo y personal.
