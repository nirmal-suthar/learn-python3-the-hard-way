from sys import argv

script, firstName, lastName = argv

middleName = input("Enter your middle name: ")

print("Your full name is %s %s %s." % (firstName, middleName, lastName))