# Encapsulation = Data Hiding


class Employee:

    def __init__(self, totalIncome):
        self.__taxValue = 12345  # Variable with __ prefix is private variable
        self.totalIncome = totalIncome

    # Getter and Setter
    def getTaxValue(self):
        return self.__taxValue

    def setTaxValue(self, value):
        if type(value) == int:
            self.__taxValue = value
        else:
            raise ValueError(f'Your Value {value} is not Integer, Please Enter value in integer !')

    def calculateTax(self):
        print(f'Total income x tax value {self.totalIncome * self.taxValue}')


empObj = Employee(100)

empObj.setTaxValue("2")
empObj.getTaxValue()

empObj.calculateTax()
