lass Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "{} by {}".format(self.title, self.author)


class EBook(Book):
    def __init__(self, title, author, file_size_mb):
        super().__init__(title, author)
