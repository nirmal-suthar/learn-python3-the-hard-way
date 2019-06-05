from sys import argv

script, filename = argv

print(f"We're going to read {filename}.")

print("Opening the file...")
target = open(filename)

print("Reading the content of the file...")
print(target.read())

print("And finally, we close it.")
target.close()

