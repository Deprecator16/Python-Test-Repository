from OOP import Person

class Car:
    def __init__(self, makeInfo, modelInfo):
        self.make = makeInfo
        self.model = modelInfo

class A:
    def __init__(self):
        return

nissan = Car("nissan", "quest")
ford = Car("ford", "escape")
ford2 = Car("ford", "edge")

x = A()

p1 = Person("bobJoe", 30, ford)

print(p1.car.make)