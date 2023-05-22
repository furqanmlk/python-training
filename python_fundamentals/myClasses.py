
# def printInfo(firstName,lastName):
#     print(f"Employee name is {firstName} {lastName}")
#
# def salCalculate(noHours,title):
#     print(f"Bi Weekly Salaray is {noHours*15}")
#
# e1 = ["Ali1","Khan1","Dev","30"]
# printInfo(e1[0])
# salCalculate(10)
#
# e2 = ["Ali2","Khan2","QA","33"]
# printInfo(e2[0])
# salCalculate(20)
#
# e3 = ["Ali3","Khan3","PM","34"]
# printInfo(e3[0])
# salCalculate(30)
#
# e4 = ["Ali4","Khan4","Dir","35"]
# printInfo(e4[0])
# salCalculate(70)
#
# e5 = ["Ali5","Khan5","DevOps","36"]
# printInfo(e5[0])
# salCalculate(35)
#
# e6 = ["Ali6","Khan6","IT","37"]
# printInfo(e6[0])
# salCalculate(15)

class HR:
    def __init__(self):
        print("I Am outside class")

    def hrMethod(self):
        print("I am HR Method")

class Employee:

    # Class variables
    classVariable = "I am the Class Variable"
    noOfObject = 0

    # Initialize
    def __init__(self, first, last, title, age):
        # Instance variables
        self.firstName = first
        self.lastName = last
        self.title = title
        self.age = age
        self.prHour = 0
        Employee.noOfObject = Employee.noOfObject + 1

    def printInfo(self):
        hr = HR()
        print(f"Employee name is {self.firstName} {self.lastName}")
        self.salCalculate()
        hr.hrMethod()

    # Instance Methods
    def salCalculate(self):
        if(self.title == "PM"):
            self.prHour = 80
        if (self.title == "Dev"):
            self.prHour = 50

        print(f"Employee salary is {50*self.prHour}")



# e1 = Employee("Ali1", "Khan1", "Dev", "30")  # it will initiate __init__ method
# print(e1)
# e1.printInfo()
# e1.salCalculate()
#
# e2 = Employee("Ali2", "Khan2", "QA", "32") # it will initiate __init__ method
# e2.classVariable = "This is updated by e2"
# # e2.printInfo()
# # e2.salCalculate()
#
# e3 = Employee("Ali3", "Khan3", "PM", "33")  # it will initiate __init__ method
# e3.salCalculate()
# e3.printInfo()
#
# e4 = Employee("Ali4","Khan4","DevOps","35") # it will initiate __init__ method
# e4.printInfo()
# e4.salCalculate()


def myMethod(name="Generic"):
    print(f"You passed name = {name}")

myMethod()