from fastapi import Body, FastAPI

app = FastAPI()

# Few books in dict
BOOKS = [
  {
    "title": "1984",
    "author": "George Orwell",
    "genre": "Dystopian"
  },
  {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Classic Fiction"
  },
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Classic Fiction"
  },
  {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "genre": "Fantasy"
  },
  {
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "genre": "Romance"
  },
  {
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "genre": "Coming-of-Age"
  },
  {
    "title": "Brave New World",
    "author": "Aldous Huxley",
    "genre": "Science Fiction"
  },
  {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "genre": "Adventure/Fantasy"
  },
  {
    "title": "Sapiens: A Brief History of Humankind",
    "author": "Yuval Noah Harari",
    "genre": "Non-fiction"
  },
  {
    "title": "The Name of the Wind",
    "author": "Patrick Rothfuss",
    "genre": "Fantasy"
  }
]

# Get route with standard message
@app.get("/hello")
async def salutation():
    return { "message": "Hi! Welcome to the universal library!"}

# Get route that returns books
@app.get("/books")
async def read_all_books():
    return BOOKS

# Get route with book title
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return False

# Get route based on a genre
@app.get("/books/")
async def read_book_by_genre(genre: str):
    return [book for book in BOOKS if book.get('genre').casefold() == genre.casefold()]

# Post route to create books
@app.post("/books/create")
async def create_book(new_book=Body()):
    global BOOKS
    BOOKS.append(new_book)

# Put route to update a book
@app.put("/books/update")
async def update_book(new_book=Body()):
    global BOOKS
    for book in BOOKS:
        if book.get('title').casefold() == new_book.get('title').casefold():
            book = new_book

# Delete route
@app.delete("/books/delete/{book_title}")
async def delete_book(book_title: str):
    global BOOKS
    BOOKS = [book for book in BOOKS if book.get('title') != book_title]
