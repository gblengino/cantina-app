🌎 **Read this in:** [English](README.md) | [Español](README.es.md)

# Cantina Management System

Backend for a desktop-based cantina management application.

This project is currently under development and is intended to start as a **local application** (offline, single-machine), with a backend architecture designed to be easily adapted to a future **online / multi-user system**.

---

## 🚀 Project Goals

- Manage products and stock
- Register sales and sale items
- Handle user authentication and roles
- Support logical deletion and auditing (created_at, is_active)
- Maintain a clean, scalable backend architecture

---

## 🧱 Tech Stack

- **Python**
- **Flask**
- **SQLAlchemy**
- **Marshmallow**
- **JWT (Flask-JWT-Extended)**
- **SQLite** (initially, for local usage)

---

## 🏗️ Architecture

The backend follows a **Service–Repository** architecture:

```
backend/
├── routes/ # API endpoints (Flask Blueprints)
├── services/ # Business logic and validations
├── repositories/ # Database access layer
├── models/ # SQLAlchemy models
├── schemas/ # Marshmallow schemas (input/output)
├── constants/ # Enums and constants (e.g. roles)
├── utils/ # Helpers and shared utilities
└── extensions/ # DB, JWT, etc.
```


This structure allows:
- clear separation of concerns
- easier testing
- future scalability

---

## 🔐 Authentication & Roles

The API uses **JWT-based authentication**.

Planned roles include:
- `admin`
- `cashier`
- `stock_manager` (product and stock management only)

Roles are validated at the service level and enforced at the route layer.

---

## 📦 Current Status

✔ Database models  
✔ Schemas (auth, users, products, sales)  
⏳ Services (in progress)  
⏳ Routes / API endpoints  
⏳ Tests  

---

## 🧪 Development Notes

- The project is developed using a **feature-branch workflow**
- `main` represents a stable state
- `develop` is the integration branch
- Features are developed in `feature/*` branches and merged via Pull Requests

---

## 📌 Future Improvements

- Online / multi-user support
- Role-based access control (RBAC)
- Automated tests
- API documentation (OpenAPI / Swagger)
- Dockerization

---

## 🖥️ Frontend (WIP)

The project includes a frontend application located in the `frontend/` directory.

- Built with **React** and **Vite**
- Intended to be packaged together with the backend using **Electron**
- Currently under early development and not yet integrated with the backend API

The frontend is considered a work in progress and its structure may change as the project evolves.

---

## 📄 License

This project is for educational and personal use.

