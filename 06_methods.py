import random;

def addTwo(a, b):
    return a+b

print(addTwo(2, 4))

def randomNr():
    _random = random.Random()
    __random = random.randint(100,200)
    return __random

print(str(randomNr()))

def stringArray():
    strings = ["Günther", "Klaus"]
    return strings[0]

print(stringArray())