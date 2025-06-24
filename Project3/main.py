from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Body, FastAPI, Depends, HTTPException, Path
from models import Base, Todos
from database import engine, SessionLocal
from starlette import status
from pydantic import BaseModel, Field

app = FastAPI()

# Create all tables based on models if they don't exist
Base.metadata.create_all(bind=engine)

# Dependency to get a DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Type alias for database dependency injection
db_dependency = Annotated[Session, Depends(get_db)]

# Pydantic model for validating todo request bodies
class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)  # Priority must be between 1 and 5
    complete: bool  # Whether the todo is completed or not

    model_config = {
        "example": {
            "title": "Feed dog",
            "description": "Is already hungry!",
            "priority": 4,
            "complete": False
        }
    }

# GET route to return all todos from the database
@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()

# GET route to return a specific todo by ID
@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found')

# POST route to create a new todo
@app.post("/todo/create", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest = Body()):
    new_todo = Todos(**todo_request.model_dump())
    db.add(new_todo)
    db.commit()

# PUT route to update an existing todo
@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, todo_request: TodoRequest = Body(), todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    
    # Update the todo fields with the request data
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    
    db.add(todo_model)
    db.commit()

# DELETE route to remove a todo by ID
@app.delete("/todos/delete/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
