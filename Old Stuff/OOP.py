# Object Oriented Programming (OOP)

class Person:
    def __init__(self, nameInfo, ageInfo, carObject):
        self.name = nameInfo
        self.age = ageInfo
        self.car = carObject

class BusinessPerson(Person):
    def __init__(self, nameInfo, ageInfo, carObject, busName):
        self.businessName = busName

p1 = Person("bob", 4)
p2 = Person("bob2", 8)

# bassilvirk@outlook.com