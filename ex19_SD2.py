def add(a1,a2):
    print(f"the first number is {a1}")
    print(f"the second number is {a2}")
    print("the sum of these two numbers are {}.\n".format(a1+a2))

print("We can just give the function numbers directly:")
add(20, 30)


print("OR, we can use variables from our script:")
firstNumber = 10
secondNumber = 50

add(firstNumber, secondNumber)


print("We can even do math inside too:")
add(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
add(firstNumber + 100, secondNumber + 1000)