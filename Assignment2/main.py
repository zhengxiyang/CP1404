from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from bookcollection import BookCollection
from book import Book


class BookApp(App):
    def build(self):
        self.title = "Books to Read - Yangzhengxi 14308833"
        self.collection = BookCollection()
        self.collection.load_books('books.csv')

        main_layout = BoxLayout(orientation="vertical")
        top_layout = BoxLayout(size_hint_y=0.2)
        book_list_layout = GridLayout(cols=1, size_hint_y=None)
        book_list_layout.bind(minimum_height=book_list_layout.setter('height'))

        self.status_label_top = Label(text="Select a sorting method", size_hint_y=0.1)
        self.status_label_bottom = Label(size_hint_y=0.1)

        # Spinner for sorting
        self.spinner = Spinner(text="Sort by...", values=("title", "author", "pages"))
        self.spinner.bind(text=self.sort_books)
        top_layout.add_widget(self.spinner)

        # Input fields and add button
        self.title_input = TextInput(hint_text="Title", multiline=False)
        self.author_input = TextInput(hint_text="Author", multiline=False)
        self.pages_input = TextInput(hint_text="Pages", multiline=False, input_filter='int')
        add_button = Button(text="Add Book", on_press=self.add_book)

        top_layout.add_widget(self.title_input)
        top_layout.add_widget(self.author_input)
        top_layout.add_widget(self.pages_input)
        top_layout.add_widget(add_button)

        # Book list layout
        book_scroll_view = ScrollView(size_hint=(1, None), size=(400, 600))
        book_scroll_view.add_widget(book_list_layout)

        # Status and layout additions
        main_layout.add_widget(top_layout)
        main_layout.add_widget(self.status_label_top)
        main_layout.add_widget(book_scroll_view)
        main_layout.add_widget(self.status_label_bottom)

        # Populate book list
        self.populate_book_list(book_list_layout)

        return main_layout

    def populate_book_list(self, layout):
        """Populate the book list in the GUI."""
        layout.clear_widgets()
        for book in self.collection.books:
            btn = Button(text=f"{book.title} by {book.author} ({book.pages} pages)",
                         background_color=(0, 1, 0, 1) if book.completed else (1, 0, 0, 1),
                         size_hint_y=None, height=40)
            btn.bind(on_press=lambda btn, book=book: self.toggle_book_status(book, layout))
            layout.add_widget(btn)
        self.status_label_top.text = f"{self.collection.get_number_of_unread_pages()} pages left to read."

    def sort_books(self, spinner, text):
        """Sort books based on the selected key."""
        self.collection.sort_books(text)
        self.populate_book_list(self.root.children[2])

    def toggle_book_status(self, book, layout):
        """Toggle the completion status of a book."""
        if book.completed:
            book.mark_unread()
        else:
            book.mark_completed()
        self.populate_book_list(layout)

    def add_book(self, instance):
        """Add a new book from input fields."""
        title = self.title_input.text
        author = self.author_input.text
        try:
            pages = int(self.pages_input.text)
            if pages <= 0:
                self.status_label_bottom.text = "The book must have some pages!"
                return
        except ValueError:
            self.status_label_bottom.text = "Please enter a valid number"
            return

        if not title or not author or not pages:
            self.status_label_bottom.text = "Please complete all fields."
            return

        new_book = Book(title, author, pages)
        self.collection.add_book(new_book)
        self.collection.save_books('books.csv')
        self.populate_book_list(self.root.children[2])
        self.status_label_bottom.text = f"'{title}' by {author} added."
        self.title_input.text = ""
        self.author_input.text = ""
        self.pages_input.text = ""


if __name__ == "__main__":
    BookApp().run()
