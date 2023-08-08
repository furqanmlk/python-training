# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints

from abc import ABC, abstractmethod

# Abstract base classes can be a very useful tool for enforcing a set of constraints 
# among the subclass of your parent class

class GraphicShape(ABC):
    # Inheriting from ABC indicates that this is an abstract base class
    def __init__(self):
        super().__init__()

    # declaring a method as abstract requires a subclass to implement it
    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self): # Without implementing this method, there will be an error
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self): # Without implementing this method, there will be an error
        return self.side * self.side


# Abstract classes can't be instantiated themselves
# g = GraphicShape() # this will error

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
