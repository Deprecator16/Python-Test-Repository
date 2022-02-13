def makeSureInputIsBetweenZeroAndTen():
    num = -1
    isInvalid = True

    while (isInvalid):
        num = int(input("Input a number: "))

        if (num < 0 or num > 10):
            print("Number entered was not between 0 and 10. Please try again.")
        else:
            isInvalid = False
    
    return num

# Make a program which gets the factorial of a number between 0 and 10
# Ex. 8! = 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8

number = makeSureInputIsBetweenZeroAndTen()
factorial = 1

for i in range(number):
    factorial = factorial * (i + 1)

print(factorial)

num1 = makeSureInputIsBetweenZeroAndTen()
num2 = makeSureInputIsBetweenZeroAndTen()

print(num1 + num2)

num3 = input()
