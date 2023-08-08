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