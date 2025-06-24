from fastapi import Body, FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app = FastAPI()

# Basic Book class used internally (not Pydantic)
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

# Pydantic model for input validation
class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed, it is created on system', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(gt=-1, lt=6)

    model_config = {
        "example": {
            "title": "A title book",
            "author": "Carlos Morales",
            "description": "A simple description",
            "rating": 5
        }
    }

# List of book instances
BOOKS = [
    Book(1, 'FastApi Tutorial', 'Carlos Morales', 'Learn how to start with FastApi', 5),
    Book(2, '1984', 'George Orwell', 'Dystopian novel', 5),
    Book(3, 'To Kill a Mockingbird', 'Harper Lee', 'Classic Fiction', 3),
    Book(1, 'The Hobbit', 'J.R.R. Tolkien', 'Middle Earth fiction novel', 4)
]

# GET route that returns all books
@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

# Helper function to assign a new unique ID to the book
def assign_new_id(book: Book):
    book.id = len(BOOKS) + 1

# POST route to create a new book
@app.post("/books/create", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest = Body()):
    global BOOKS
    new_book = Book(**book_request.model_dump())
    assign_new_id(new_book)
    BOOKS.append(new_book)

# GET route to fetch a book by its ID
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

# GET route to filter books by rating
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books = []
    for book in BOOKS:
        if book.rating == book_rating:
            books.append(book)
    return books

# PUT route to update a book based on its ID
@app.put("/books/update", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_request: BookRequest = Body()):
    global BOOKS
    book_changed = False
    new_book = Book(**book_request.model_dump())
    for index, book in enumerate(BOOKS):
        if book.id == new_book.id:
            BOOKS[index] = new_book
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

# DELETE route to remove a book by ID
@app.delete("/books/delete/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    global BOOKS
    BOOKS = [book for book in BOOKS if book.id != book_id]
