import json

class BookCollection:
    def __init__(self):
        """Initialize an empty book collection."""
        self.books = []

    def add_book(self, book):
        """Add a single Book object to the collection."""
        self.books.append(book)

    def get_number_of_unread_pages(self):
        """Return the total number of pages in unread books."""
        return sum(book.pages for book in self.books if not book.completed)

    def get_number_of_completed_pages(self):
        """Return the total number of pages in completed books."""
        return sum(book.pages for book in self.books if book.completed)

    def load_books(self, filename):
        """Load books from a JSON file."""
        with open(filename, 'r') as file:
            books_data = json.load(file)
            self.books = [Book(**data) for data in books_data]

    def save_books(self, filename):
        """Save books to a JSON file."""
        with open(filename, 'w') as file:
            books_data = [book.__dict__ for book in self.books]
            json.dump(books_data, file)

    def sort_books(self, key):
        """Sort books by the specified key and then by title."""
        self.books.sort(key=lambda book: getattr(book, key))
