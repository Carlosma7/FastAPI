from database import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey

# SQLAlchemy model for the 'users' table
class Users(Base):
    __tablename__ = 'users'  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique user identifier
    email = Column(String, unique=True)  # User's email (must be unique)
    username = Column(String, unique=True)  # Username (must be unique)
    first_name = Column(String)  # First name of the user
    last_name = Column(String)  # Last name of the user
    password = Column(String)  # Hashed password (should not be stored in plain text)
    is_active = Column(Boolean, default=True)  # Account status (active or not)
    role = Column(String)  # Role for permissions (e.g., 'admin', 'user', etc.)

# SQLAlchemy model for the 'todos' table
class Todos(Base):
    __tablename__ = 'todos'  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique todo identifier
    title = Column(String)  # Short title of the todo item
    description = Column(String)  # Detailed description of the task
    priority = Column(Integer)  # Priority level (1-5)
    complete = Column(Boolean, default=False)  # Completion status
    owner_id = Column(Integer, ForeignKey("users.id"))  # Foreign key linking todo to the user who owns it
