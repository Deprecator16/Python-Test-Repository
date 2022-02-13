def largest(a, b):
    print(a, b)
    if (a > b):
        return a
    else:
        return b

# A = (base * height) / 2
def areaOfTriangle(base, height):
    return (base * height) / 2

b = int(input())
h = int(input())

print( areaOfTriangle(b, h) )


# num1 = 4
# num2 = 7
# x = largest(num2, num1)
# y = largest(9, -3)

# print("Largest number: ", x)
# print("Largest number: ", y)