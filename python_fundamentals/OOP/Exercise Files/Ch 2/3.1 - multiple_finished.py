# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(B, A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name) # name attribute is duplicate in both patent classes


# create the class and call showname()
c = C()

# __mro__ prints method resolution order
# that is first it's Class C, then it's Class B because that comes first in the order, 
# then Class A because that's next, and then the Object class 
# which is the implicit superclass for all objects in Python
print(C.__mro__) # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

c.showprops() # class B name will be printed, as it is interited first when definiting class C (line 19)
