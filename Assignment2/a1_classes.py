from book import Book
from bookcollection import BookCollection

FILENAME = 'books.csv'
MENU = "Menu:\nL - List books\nA - Add new book\nM - Mark a book as completed\nQ - Quit\n"


def main():
    """Main function for the console program."""
    print("Reading List 1.0 - by Yangzhengxi 14308833")
    collection = BookCollection()
    collection.load_books(FILENAME)

    while True:
        print(MENU)
        choice = input(">>> ").upper()
        if choice == 'L':
            list_books(collection)
        elif choice == 'A':
            add_book(collection)
        elif choice == 'M':
            mark_book(collection)
        elif choice == 'Q':
            collection.save_books(FILENAME)
            print("Books have been saved to", FILENAME)
            break
        else:
            print("Invalid menu choice")


def list_books(collection):
    """Display the list of books."""
    books = collection.books
    if not books:
        print("No books")
        return
    books.sort(key=lambda book: (book.author, book.title))
    total_pages = 0
    unread_books = 0
    for i, book in enumerate(books):
        mark = '*' if not book.completed else ' '
        print(f"{i + 1}. {mark} {book.title} by {book.author} ({book.pages} pages)")
        if not book.completed:
            total_pages += book.pages
            unread_books += 1
    print(f"Total pages for {unread_books} unread books: {total_pages}")


def add_book(collection):
    """Add a new book to the collection."""
    title = input("Title: ").strip()
    while not title:
        print("Input cannot be blank")
        title = input("Title: ").strip()
    author = input("Author: ").strip()
    while not author:
        print("Input cannot be blank")
        author = input("Author: ").strip()
    pages = input("Pages: ").strip()
    while not pages.isdigit() or int(pages) <= 0:
        print("Invalid input; enter a valid number")
        pages = input("Pages: ").strip()

    new_book = Book(title, author, int(pages))
    collection.add_book(new_book)
    print(f"{title} by {author}, ({pages} pages) added to reading list")


def mark_book(collection):
    """Mark a book as completed."""
    unread_books = [book for book in collection.books if not book.completed]
    if not unread_books:
        print("No unread books")
        return
    list_books(collection)
    try:
        choice = int(input("Enter the number of a book to mark as completed\n>>> ")) - 1
        if choice < 0 or choice >= len(collection.books) or collection.books[choice].completed:
            print("Invalid book number")
        else:
            collection.books[choice].mark_completed()
            print(f"{collection.books[choice].title} by {collection.books[choice].author} marked as completed")
    except ValueError:
        print("Invalid input; enter a number")


if __name__ == '__main__':
    main()
