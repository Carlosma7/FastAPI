# ⚡ FastAPI – Project-Based Walkthrough

This repository contains a step-by-step FastAPI project designed to demonstrate how to build a secure, modular, and database-backed REST API from scratch.

The project evolves through four incremental stages:

1. **Stage 1** – Basic CRUD over an in-memory list of books.
2. **Stage 2** – Input validation with Pydantic and typed models.
3. **Stage 3** – Database integration with SQLAlchemy and SQLite.
4. **Stage 4** – User authentication (OAuth2 + JWT), hashed passwords, and role-based access control.

## ⚙️ Stack

- FastAPI  
- Pydantic  
- SQLAlchemy + SQLite  
- OAuth2 + JWT (python-jose)  
- Passlib (bcrypt)  
- Uvicorn

## ▶️ Run the App

```bash
pip install -r requirements.txt
uvicorn main:app --reload
````

## 📌 Highlights

* Progressive structure: from raw lists to fully authenticated endpoints
* Modular route separation (`auth`, `todos`, `admin`)
* Real database models and persistence
* Token-based authentication with user roles

## 📤 Extra

I explained this project and the core ideas behind FastAPI in this [LinkedIn post](https://www.linkedin.com/posts/carlos-morales-aguilera_fastapi-python-backend-activity-7343347775960449024-A5aX?utm_source=share&utm_medium=member_desktop&rcm=ACoAACGfzmkB2FzOzdh4Zn8oi45frTzj4p6PzH4) using slides and examples.
