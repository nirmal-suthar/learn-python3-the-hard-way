# inport argv from the sys module
from sys import argv

# unpacking argument from the argument variable
script, filename = argv

# open a file
txt = open(filename)

# print the filename
print(f"Here's your file {filename}:")
# print the content of the filename
print(txt.read())

# close a file
close()

print("Type the filename again:")
# input a file name as file_again
file_again = input("$ ")

# open a file
txt_again = open(file_again)

# print the content of the filename
print(txt_again.read())

# close a file
close()