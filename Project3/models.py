from database import Base
from sqlalchemy import Boolean, Column, Integer, String

# SQLAlchemy model for the 'todos' table
class Todos(Base):
    __tablename__ = 'todos'  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for each todo
    title = Column(String)  # Title of the todo item
    description = Column(String)  # Detailed description of the task
    priority = Column(Integer)  # Priority level (e.g., 1 to 5)
    complete = Column(Boolean, default=False)  # Completion status (False by default)
