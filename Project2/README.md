# 📚 Universal Library API – Stage 2

This version introduces structured data modeling and request validation to improve reliability and type safety.

## ✅ Overview

The app now uses a `Book` class for internal objects and a Pydantic `BookRequest` model to validate request data. Endpoints are more robust, with typed parameters, validation rules, and error handling.

## 🔄 Changes from Stage 1

- Replaced raw dicts with a `Book` class for internal storage.
- Added `BookRequest` (Pydantic) to validate input data with constraints.
- Introduced `id` as a unique identifier for book lookup and deletion.
- Added query filtering by rating with automatic validation.
- Added HTTP status codes and structured error handling with `HTTPException`.

## 📚 Sample Data

The app starts with 4 predefined books. Each includes:

- `id`, `title`, `author`, `description`, `rating`

## ⚙️ Technologies

- Python 3.10+  
- FastAPI  
- Pydantic  
- Uvicorn

## ▶️ Getting Started

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
````

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API.

## 📌 Limitations

* In-memory storage (no persistence)
* Potential for duplicate `id` values
* No authentication or user accounts
