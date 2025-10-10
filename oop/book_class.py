# book_class.py

class Book:
    """
    Book class demonstrating magic methods:
      - __init__ (constructor)
      - __del__  (destructor)
      - __str__  (user-friendly string)
      - __repr__ (official string to recreate the object)
    """

    def __init__(self, title, author, year):
        # attributes required by the task
        self.title = title
        self.author = author
        self.year = int(year)

    def __str__(self):
        # "(title) by (author), published in (year)"
        return "{} by {}, published in {}".format(self.title, self.author, self.year)

    def __repr__(self):
        # "Book('title', 'author', year)"
        return "Book('{}', '{}', {})".format(self.title, self.author, self.year)

    def __del__(self):
        # called when the object is deleted; prints the required message
        print("Deleting {}".format(self.title))

