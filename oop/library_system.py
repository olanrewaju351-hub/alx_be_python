# library_system.py

# Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super(EBook, self).__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author} - File size: {self.file_size}KB"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super(PrintBook, self).__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} - {self.page_count} pages"


# Composition Class - Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(book)
