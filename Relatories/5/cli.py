class SimpleCLI:
  """
  A basic CLI for executing commands.
  """

  def __init__(self):
    """
    Initializes with an empty command dictionary.
    """
    self.commands = {}

  def add_command(self, name, function):
    """
    Adds a command to the CLI.
    """
    self.commands[name] = function

  def run(self):
    """
    Starts the CLI loop.
    """
    while True:
      command = input("Enter a command: ")
      if command == "quit":
        print("Goodbye!")
        break
      elif command in self.commands:
        self.commands[command]()
      else:
        print("Invalid command. Try again.")

class BookCLI(SimpleCLI):
  """
  CLI for managing books (CRUD operations).
  """

  def __init__(self, book_model):
    """
    Initializes with the book model and adds commands.
    """
    super().__init__()
    self.book_model = book_model
    self.add_command("create", self.create_book)
    self.add_command("read", self.read_book)
    self.add_command("update", self.update_book)
    self.add_command("delete", self.delete_book)
    self.add_command("quit", self.quit)

  def create_book(self):
    """
    Creates a new book by prompting user input.
    """
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the year: "))
    price = float(input("Enter the price: "))
    self.book_model.create_book(title, author, year, price)

  def read_book(self):
    """
    Displays book details by ID.
    """
    id = input("Enter the id: ")
    book = self.book_model.read_book_by_id(id)
    if book:
      print(f"Title: {book['titulo']}")
      print(f"Author: {book['autor']}")
      print(f"Year: {book['ano']}")
      print(f"Price: {book['preco']}")

  def update_book(self):
    """
    Updates a book by ID with new details.
    """
    id = input("Enter the id: ")
    title = input("Enter the new title: ")
    author = input("Enter the new author: ")
    year = int(input("Enter the new year: "))
    price = float(input("Enter the new price: "))
    self.book_model.update_book(id, title, author, year, price)

  def delete_book(self):
    """
    Deletes a book by ID.
    """
    id = input("Enter the id: ")
    self.book_model.delete_book(id)

  def quit(self):
    """
    Exits the CLI.
    """
    print("Exiting the Book CLI.")
    exit()

  def run(self):
    """
    Starts the CLI with a welcome message and available commands.
    """
    print("Welcome to the book CLI!")
    print("Available commands: create, read, update, delete, quit")
    super().run()
