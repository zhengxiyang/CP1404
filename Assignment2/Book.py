class Book:
    def __init__(self, title, author, pages, completed=False):
        """Initialize a new book with title, author, pages, and completion status."""
        self.title = title
        self.author = author
        self.pages = pages
        self.completed = completed

    def __str__(self):
        """Return a string representation of the book."""
        status = 'completed' if self.completed else 'not completed'
        return f"'{self.title}' by {self.author}, {self.pages} pages, {status}"

    def mark_completed(self):
        """Mark the book as completed."""
        self.completed = True

    def mark_unread(self):
        """Mark the book as unread."""
        self.completed = False

    def is_long(self):
        """Determine if the book is considered long (>= 500 pages)."""
        return self.pages >= 500
