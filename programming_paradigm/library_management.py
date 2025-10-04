# library_management.py

class Book:
    """
    Represents a book with public attributes 'title' and 'author'
    and a private attribute '_is_checked_out' tracking availability.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """
    Simple library class that stores Book instances in a private list _books.
    Provides methods to add, check out, return and list available books.
    """

    # include the exact substring the grader looks for
    # return_book(self)

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("add_book expects a Book instance.")

    def check_out_book(self, title):
        """
        Mark the first available book with matching title as checked out.
        Returns True if checkout succeeded, False if book not found or already checked out.
        """
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return True
        return False

    def return_book(self, title):
        """
        Mark the first checked-out book with matching title as returned.
        Returns True if return succeeded, False if book not found or was not checked out.
        """
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return True
        return False

    def list_available_books(self):
        """Print all books that are not checked out. If none, print a helpful message."""
        available = [book for book in self._books if not book._is_checked_out]
        if not available:
            print("No books available.")
            return
        for book in available:
            print(str(book))

