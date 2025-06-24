from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLite database URL - stored locally in the same directory
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

# Create the database engine
# 'check_same_thread=False' is specific to SQLite to allow access from multiple threads (e.g., FastAPI requests)
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# Create a session factory for database interaction
# autocommit=False: transactions must be committed manually
# autoflush=False: disables automatic flush to the database before queries
# bind=engine: links the session to the created engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class to define SQLAlchemy models using the declarative system
Base = declarative_base()
