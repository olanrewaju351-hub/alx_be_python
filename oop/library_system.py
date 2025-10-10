# library_system.py

# Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "{} by {}".format(self.title, self.author)


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)

    def __str__(self):
        return "{} by {}, File Size: {}KB".format(self.title, self.author, self.file_size)


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)

    def __str__(self):
        return "{} by {}, Page Count: {}".format(self.title, self.author, self.page_count)


# Composition Class - Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return

        for book in self.books:
            if isinstance(book, EBook):
                print("EBook: {}".format(str(book)))
            elif isinstance(book, PrintBook):
                print("PrintBook: {}".format(str(book)))
            elif isinstance(book, Book):
                print("Book: {}".format(str(book)))
            else:
                # fallback for unexpected types
                print(str(book))

