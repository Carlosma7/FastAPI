# 📚 Universal Library API – Stage 1

Welcome to the first version of the **Universal Library API**, a basic FastAPI project that simulates a book catalog using in-memory data.

## ✅ Overview

This version defines a RESTful API using FastAPI to manage a list of books stored in a Python list. It supports basic create, read, update, and delete operations through HTTP endpoints.

## 📚 Sample Data

The app initializes with 10 predefined books. Each book contains:

- `title`: Title of the book  
- `author`: Author's name  
- `genre`: Book genre

## ⚙️ Technologies

- Python 3.10+  
- FastAPI  
- Uvicorn

## ▶️ Getting Started

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
````

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API.

## 📌 Limitations

* No database or persistent storage
* No ID field (title is used as identifier)
* No validation or error handling
* No authentication
