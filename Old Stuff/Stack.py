# s = "I want to reverse this string."


class Stack:
    def __init__(self):
        self.size = 0
        self.li = []
    
    def push(self, data):
        self.li.append(data)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.li.pop()
    
    def getSize(self):
        return self.size

stack = Stack()

stack.push(1)
stack.push('hello')

print(stack.pop())
print(stack.pop())



# for i in range(len(s)):
#     stack.append(s[i])

# print(stack)

# reversedString = ""

# for i in range(len(stack)):
#     reversedString = reversedString + stack.pop()

# print(reversedString)