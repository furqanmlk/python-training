# Polymorphism ---> Many Forms

class Employee:

    def printTiming(self):
        print("Employee Main timing 09 to 5")

    def method01(self):
        pass

    def method02(self):
        pass

    def method03(self):
        pass


class Employee01(Employee):

    def printTiming(self):
        print("Employee Afternoon timing 12 to 8")


class Employee02(Employee):

    def printTiming(self):
        print("Employee Evening timing 80 to 08")


e01 = Employee01()
e01.printTiming()  # It will take form Employee01 class

e02 = Employee02()
e02.printTiming()  # It will take form Employee02 class
