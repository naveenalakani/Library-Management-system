class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def lend_book(self, book_title, member):
        for book in self.books:
            if book.title == book_title and book.is_available:
                book.is_available = False
                member.borrow_book(book)
                print(f"Book '{book}' lent to {member.name}.")
                return
        print(f"Book '{book_title}' is not available.")

    def return_book(self, book_title, member):
        for book in member.borrowed_books:
            if book.title == book_title:
                book.is_available = True
                member.return_book(book)
                print(f"Book '{book}' returned to the library by {member.name}.")
                return
        print(f"Book '{book_title}' was not borrowed by {member.name}.")

    def view_books(self):
        print("Available books in the library:")
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"{book} - {status}")

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

# Example Usage
library = Library()

# Adding books to the library
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Viewing available books
library.view_books()

# Creating a member
member = Member("Alice")

# Lending a book to the member
library.lend_book("1984", member)

# Viewing available books after lending
library.view_books()

# Returning a book to the library
library.return_book("1984", member)

# Viewing available books after returning
library.view_books()
