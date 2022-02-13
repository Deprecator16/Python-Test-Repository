# Bassil Virk
# Print the first n fibonacci number
# 1, 1, 2, 3, 5, 8, 13, 21

num = int(input("Enter a number: "))

first = 1
second = 1


for i in range(num):
    temp = first + second
    second = first
    first = temp
    print(temp)