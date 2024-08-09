import csv
from book import Book

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
        """Load books from a CSV file."""
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    title, author, pages, is_completed = row
                    book = Book(title, author, int(pages), is_completed == 'c')
                    self.add_book(book)
        except FileNotFoundError:
            print(f"Warning: {filename} not found. Starting with an empty list.")

    def save_books(self, filename):
        """Save books to a CSV file."""
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for book in self.books:
                writer.writerow([book.title, book.author, book.pages, 'c' if book.completed else 'r'])

    def sort_books(self, key):
        """Sort books by the specified key and then by title."""
        self.books.sort(key=lambda book: getattr(book, key))
