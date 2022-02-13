class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def increaseAge(self):
        self.age = self.age + 1
    
    def printInfo(self):
        print("This person's info is: ")
        print(self.name)
        print(self.age)
        print(self.gender)


bob = Person("bob", 21, "male")
joe = Person("bob", 21, "male")
bobJoe = Person("bobJoe", 31, "male")

bob.printInfo()
joe.printInfo()