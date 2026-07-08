# A class that prints nicely
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        # Searched how to quote inside f-string on "Stack Overflow"
        return f"'{self.title.title()}' by {self.author.title()}"
    
book1 = Book("Martin Eden", "Jack London")
book2 = Book("Pride and Prejudice", "Jane Austen")
print(book1)
print(book2)