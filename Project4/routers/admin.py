from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from models import Base, Todos
from database import engine, SessionLocal
from starlette import status
from .auth import get_current_user

# Create a router with '/admin' prefix and 'admin' tag
router = APIRouter(
    prefix='/admin',
    tags=['admin']
)

# Ensure all tables are created (typically done once in main.py)
Base.metadata.create_all(bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Typed dependencies for injection
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

# GET route to retrieve all todos (admin-only access)
@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed.')
    return db.query(Todos).all()

# DELETE route to delete a specific todo by ID (admin-only access)
@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed.')
    
    # Check if the todo item exists
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')

    # Delete the todo item
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
