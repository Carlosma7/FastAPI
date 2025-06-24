# 📚 Universal Library API – Stage 3

This version introduces full database integration using SQLAlchemy with a SQLite backend.

## ✅ Overview

The app now persists data using a relational database. SQLAlchemy is used for ORM-based model definitions, and all operations are executed through a database session. The previous in-memory structure has been completely replaced.

## 🔄 Changes from Stage 2

- Integrated **SQLite** using SQLAlchemy for data persistence.
- Added a database connection and session setup (`engine`, `SessionLocal`, `Base`).
- Defined the `Todos` table using a declarative SQLAlchemy model.
- All CRUD operations now interact with the database instead of memory.
- Added proper session management via dependency injection (`Depends(get_db)`).
- Improved reliability and scalability of data operations.

## 🧱 Data Model

Each todo item includes:

- `id`: Unique identifier (auto-incremented)
- `title`: Short text (string)
- `description`: Longer text (string)
- `priority`: Integer from 1 to 5
- `complete`: Boolean flag

## ⚙️ Technologies

- Python 3.10+  
- FastAPI  
- Pydantic  
- SQLAlchemy  
- SQLite  
- Uvicorn

## ▶️ Getting Started

```bash
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
````

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API.

## 📌 Limitations

* No user authentication or access control
* No relationship support or multi-table queries
* Database schema is auto-generated without migrations
