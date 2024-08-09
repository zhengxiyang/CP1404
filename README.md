# CP1404
# CP1404 Assignment 2 – Books to Read 2.0

### Author: Yangzhengxi  
### Student ID: 14308833

## Project Overview

This project is a book management system developed in Python. It consists of both a console-based application and a graphical user interface (GUI) application using the Kivy framework. The program allows users to manage a reading list by adding books, marking them as completed, and sorting them by different attributes.

The primary goals of this project were to:
- Practice using Python classes to create reusable data types.
- Implement a GUI application using Kivy.
- Utilize exception handling, file handling (CSV), and basic GUI components.

## Features

- **Book Class**: Represents a single book with attributes for the title, author, pages, and completion status.
- **BookCollection Class**: Manages a collection of books, providing functionality to add, sort, and save books.
- **Console Program**: A text-based interface that allows users to list, add, and mark books as completed.
- **GUI Program**: A graphical interface that provides more intuitive interaction with the book collection, including sorting, adding books, and toggling completion status.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your machine.
- The Kivy library installed (for the GUI). You can install it using pip:
  ```bash
  pip install kivy

## Project Reflection

### What did you learn?
Throughout this project, I gained a deeper understanding of object-oriented programming in Python. Implementing the `Book` and `BookCollection` classes helped me appreciate the importance of modularity and code reuse. I also learned how to effectively use the Kivy framework to create a graphical user interface, which was a new experience for me. The process of integrating the GUI with the underlying data model was particularly enlightening, as it reinforced the concept of separating logic from presentation.

### What challenges did you face?
One of the main challenges I faced was ensuring that the console program and the GUI program both utilized the same data model effectively. Initially, I struggled with handling the user input validation and error checking in both the console and GUI environments, especially when dealing with edge cases. Another challenge was working with the Kivy framework, as it was my first time using it. Understanding how to dynamically update the GUI based on user interactions required some trial and error.

### How did you improve your coding practices?
This project helped me improve my coding practices significantly. I became more disciplined with writing clean, well-documented code, particularly by using docstrings and inline comments. I also learned the importance of version control, as I used Git to manage my project's development. Regular commits with meaningful messages helped me keep track of my progress and made it easier to backtrack when necessary.

### What would you do differently next time?
If I were to start this project again, I would spend more time planning the overall structure before diving into the coding. Although I was able to complete the project, a more thorough design phase might have helped me avoid some of the challenges I encountered later on. Additionally, I would like to explore more advanced features in Kivy, such as animations or more complex layouts, to make the GUI even more user-friendly and engaging. Finally, I would consider adding a feature to categorize books by genre or allow for more advanced filtering options.
