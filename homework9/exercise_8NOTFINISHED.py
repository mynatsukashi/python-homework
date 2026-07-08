import json as js

class Library:
    def __init__(self):
        try:
            #try to open file
            with open ("library.json", "r") as f:
                self.books_shelf = js.load(f)
                #if file is not found, start with an empty list
        except FileNotFoundError:
            self.books_shelf = []
    
    def add(self, title, author):
        self.title = title
        self.author = author
        self.books_shelf.append(title,author)
        with open("library.json", "w") as f:
            js.dump(self.book_shelf, f)
    
    def show(self):
        return f"{self.title} by {self.author}"
    
print(f"{len()}")