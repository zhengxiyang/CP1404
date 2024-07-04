import csv

# Constants
FILENAME = 'books.csv'
MENU = "Menu:\nL - List books\nA - Add new book\nM - Mark a book as completed\nQ - Quit\n"

def main():
    print("Reading List 1.0 - by [Your Name]")
    books = load_books(FILENAME)
    while True:
        print(MENU)
        choice = input(">>> ").upper()
        if choice == 'L':
            list_books(books)
        elif choice == 'A':
            add_book(books)
        elif choice == 'M':
            mark_book(books)
        elif choice == 'Q':
            save_books(FILENAME, books)
            print("Books have been saved to", FILENAME)
            break
        else:
            print("Invalid menu choice")

def load_books(filename):
    """Load the list of books from a file"""
    books = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                title, author, pages, is_completed = row
                books.append([title, author, int(pages), is_completed == 'c'])
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with an empty list.")
    return books

def save_books(filename, books):
    """Save the list of books to a file"""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for book in books:
            writer.writerow([book[0], book[1], book[2], 'c' if book[3] else 'r'])

def list_books(books):
    """Display the list of books"""
    if not books:
        print("No books")
        return
    books.sort(key=lambda book: (book[1], book[0]))
    total_pages = 0
    unread_books = 0
    for i, book in enumerate(books):
        mark = '*' if not book[3] else ' '
        print(f"{i + 1}. {mark} {book[0]} by {book[1]} ({book[2]} pages)")
        if not book[3]:
            total_pages += book[2]
            unread_books += 1
    print(f"Total pages for {unread_books} unread books: {total_pages}")

def add_book(books):
    """Add a new book to the list"""
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
    books.append([title, author, int(pages), False])
    print(f"{title} by {author}, ({pages} pages) added to reading list")

def mark_book(books):
    """Mark a book as completed"""
    unread_books = [book for book in books if not book[3]]
    if not unread_books:
        print("No unread books")
        return
    list_books(books)
    try:
        choice = int(input("Enter the number of a book to mark as completed\n>>> ")) - 1
        if choice < 0 or choice >= len(books) or books[choice][3]:
            print("Invalid book number")
        else:
            books[choice][3] = True
            print(f"{books[choice][0]} by {books[choice][1]} marked as completed")
    except ValueError:
        print("Invalid input; enter a number")

if __name__ == '__main__':
    main()
