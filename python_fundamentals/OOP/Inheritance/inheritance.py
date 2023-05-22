class Employee:  # Super Class
    def create_profile(self):
        print("This is profile method")

    def calculateSal(self):
        print("This is calcualteSal method")

    def employeeMethod(self):
        print("I am Employee method")


class MorningEmployee(Employee):  # Sub Class Inheriting Super Class

    def __init__(self, name="Hello"):
        self.name = name

    def set_name(self, new_name):
        self.name = new_name

    def __str__(self):  # It prints value when class object is printed
        return f"Company name: {self.name}"

    def getNoOfEmployee(self):
        print("there is 40 employee")

    def shiftsScheduale(self):
        print("Morning Employee Scheduale")

    def employeeMethod(self):
        super().employeeMethod()
        print("this is few more code added")


morEmployee = MorningEmployee("Jon")
print(morEmployee)

morEmployee.set_name("Mike Bob")
print(morEmployee)
