# 📚 Universal Library API – Stage 4

This version introduces user management and role-based access control using authentication and authorization mechanisms.

## ✅ Overview

The app now supports user registration, secure authentication via JWT tokens, and permission-based routing for regular users and admins. Todos are now linked to users, and endpoints enforce ownership and roles.

## 🔄 Changes from Stage 3

- Introduced `Users` model with fields like `username`, `email`, `role`, and `password`.
- Implemented secure password hashing with **bcrypt**.
- Enabled authentication using **OAuth2 with JWT tokens**.
- Added role-based access:
  - Regular users can only manage their own todos.
  - Admins can view and delete all todos.
- Connected each todo to its owner using a `ForeignKey`.
- Modularized routes with `auth`, `todos`, and `admin` routers.
- Added token-based user context (`get_current_user`) to all protected routes.

## 👥 User Roles

- **User**: Can create, read, update, and delete only their own todos.
- **Admin**: Can list and delete any todo from all users via `/admin` routes.

## 🧱 Data Models

- `Users`:  
  `id`, `email`, `username`, `first_name`, `last_name`, `password`, `is_active`, `role`
- `Todos`:  
  `id`, `title`, `description`, `priority`, `complete`, `owner_id (FK)`

## ⚙️ Technologies

- Python 3.10+  
- FastAPI  
- Pydantic  
- SQLAlchemy  
- SQLite  
- Passlib (bcrypt)  
- Python-JOSE (JWT)  
- Uvicorn

## ▶️ Getting Started

```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose
uvicorn main:app --reload
````

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API.

## 🔧 Possible Improvements

* Add token refresh and logout functionality
* Include email confirmation and password recovery
* Implement pagination and advanced filtering for admin views
* Use Alembic for schema migrations
* Add unit tests and role-based testing
* Support environment-based configuration and `.env` loading
* Improve error handling and input feedback
