from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLite database URL - local file named 'todos.db'
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

# Create the database engine
# 'check_same_thread=False' is required only for SQLite to allow usage from different threads
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# Create a session factory bound to the engine
# autocommit=False ensures that transactions must be manually committed
# autoflush=False disables automatic flushing of changes to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions
Base = declarative_base()
