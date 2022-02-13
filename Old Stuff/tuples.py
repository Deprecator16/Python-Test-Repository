def max(num1, num2, num3):
    largest = 0
    secondLargest = 0
    thirdLargest = 0
    if num1 > num2 and num1 > num3:
        largest = num1
    
    return (largest, secondLargest, thirdLargest)

ret = max(1, 28, 3)

# (28, 2, 1)