def max(num1, num2):
    if (num1 > num2):
        return num1
    else:
        return num2

number = int(input("Enter a number: "))

ret = max(number, 9)

print(ret)