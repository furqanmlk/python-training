class Example:
    def __init__(self):
        self.public_variable = 42
        self._internal_variable = "internal value"
        self.__name_mangled_variable = "name mangled value"

obj = Example()

# Normal Variable
print(obj.public_variable)  # Accessible

# Variable with single underscore
print(obj._internal_variable)  # Accessible but indicates it's internal

# Variable with double underscore
print(obj.__name_mangled_variable)  # Causes AttributeError due to name mangling

print(obj._Example__name_mangled_variable)  # Name mangled variable is accessible this way
