class Book():
    def __init__(self,title,description,author,pages,price):
        self.title=title
        self.description=description
        self.author=author
        self.pages=pages
        self.price=price

book1=Book("Title1","Description1","Author1",23,39.00)

print(book1)
print(book1.title)