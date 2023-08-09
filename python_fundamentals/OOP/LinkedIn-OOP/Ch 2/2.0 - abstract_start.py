# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints


class GraphicShape:
    def __init__(self):
        super().__init__()

    def calcArea(self): # I want this method to be forcefully implemented by subclasses
        pass


class Circle(GraphicShape): # This subclass has not implemented calcArea()
    def __init__(self, radius):
        self.radius = radius


class Square(GraphicShape): # This subclass has not implemented calcArea()
    def __init__(self, side):
        self.side = side


g = GraphicShape() # I want this Parent class NOT to be initialized

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())

# TO SOLVE, ALL ABOVE ISSUE, PARENT CALSS HAS BE ABSTRACT CLASS