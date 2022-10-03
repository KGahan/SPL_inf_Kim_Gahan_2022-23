import random;

def addTwo(a, b):
    return a+b

print(addTwo(2, 4))

def randomNr():
    random = random.Random()
    return random.randint(10,30)

print(randomNr)

def stringArray():
    strings = ["Günther", "Klaus"]
    return strings[0]

print(stringArray)