# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, authorfname, authorlname):
        self.title = title
        self.price = price

        # We can move these two attributes to its own class
        self.authorfname = authorfname 
        self.authorlname = authorlname

        self.chapters = []

       # We can move name and pages to its own class
    def addchapter(self, name, pages):
        self.chapters.append((name, pages))

# TODO: Create Auther class with fname and lname arrtibute

# TODO: Create Chaper class with name and pagecount attributes

b1 = Book("War and Peace", 39.0, "Leo", "Tolstoy")

b1.addchapter("Chapter 1", 125)
b1.addchapter("Chapter 2", 97)
b1.addchapter("Chapter 3", 143)

print(b1.title)
