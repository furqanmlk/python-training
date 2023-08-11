FILE_PATH = "python_fundamentals/Read_Write_File/my_file.txt"
# file = open("python_fundamentals/Read_Write_File/my_file.txt")
# contents = file.read()
# print(contents)

# Using with
with open(FILE_PATH) as file:
    print(file.read()) # Same output as above

# mode=w will replace whole file with new text, will create if does not exist
with open(FILE_PATH,mode='w') as file:
    file.write("This is new line")

with open(FILE_PATH,mode='a') as file:
    file.write("\nThis is second line")

# Reading from a File:
# You can read the contents of a file using methods like read(), 
# readline(), or readlines().

content = file.read()  # Read the entire file content
line = file.readline()  # Read one line
lines = file.readlines()  # Read all lines and return as a list

    

