from fastapi import FastAPI
from models import Base
from database import engine
from routers import auth, todos, admin

# Create the FastAPI app instance
app = FastAPI()

# Create all database tables based on the models if they don't already exist
Base.metadata.create_all(bind=engine)

# Include routers for different parts of the application
app.include_router(auth.router)   # Authentication and user-related routes
app.include_router(todos.router)  # CRUD operations for todos
app.include_router(admin.router)  # Admin-only routes and logic
