from database import Database
from bookModel import BookModel
from cli import BookCLI

# Initializes the Database instance.
db = Database(database="local", collection="books")

# Initializes the BookModel instance with the Database instance.
bookModel = BookModel(database=db)

bookCLI = BookCLI(bookModel)
bookCLI.run()
