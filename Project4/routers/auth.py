from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from models import Base, Users
from passlib.context import CryptContext
from database import engine, SessionLocal
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

# Secret key and algorithm used for JWT token encoding/decoding
SECRET_KEY = '1824b18rv8139fh891fh088ch10chcuadncnuicdnw14139489'
ALGORITHM = 'HS256'

# Create an auth router with prefix and tags
router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

# Bcrypt password context for hashing and verifying passwords
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# OAuth2 scheme that expects a token via the Authorization header
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

# Ensure all tables are created based on models
Base.metadata.create_all(bind=engine)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Annotated type for DB dependency
db_dependency = Annotated[Session, Depends(get_db)]

# Request body model for user creation
class CreateUserRequest(BaseModel):
    username: str = Field(min_length=4, max_length=16)
    email: str = Field(min_length=5, max_length=30)
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    password: str
    role: str

# Pydantic model for JWT response
class Token(BaseModel):
    access_token: str
    token_type: str

# Auth function to validate user credentials
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user

# JWT token creation function
def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

# Dependency to get the current user from token
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        role: str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials.')
        return {'username': username, 'user_id': user_id, 'user_role': role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials.')

# POST route to register a new user
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        username=create_user_request.username,
        email=create_user_request.email,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        password=bcrypt_context.hash(create_user_request.password),  # Store hashed password
        is_active=True
    )
    db.add(create_user_model)
    db.commit()

# POST route to authenticate user and return a JWT token
@router.post("/token", response_model=Token)
async def login_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials.')
    
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}
