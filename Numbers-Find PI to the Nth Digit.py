import math

# print(len(str(math.pi))) checking the limit on pi

digitLength = int(input("How many numbers of Pi would you like to have? "))
if digitLength > 16:
    print("Limit is 16 digits, Please input a number that is 16 or lower")
else:
    pie = str(math.pi)

    piString = ""

    for digit in range(digitLength+1):
        piString += str(pie[digit])

    print("Pi to the number of " + str(digitLength) + " is " + str(piString))
