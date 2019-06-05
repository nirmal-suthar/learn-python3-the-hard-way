def list_generator(end, increment = 1, numbers = []):
    i = 0
    while i < end:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)

        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

    return numbers

print(list_generator(6))