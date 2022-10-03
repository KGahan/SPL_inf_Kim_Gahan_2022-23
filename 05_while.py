import random;

random = random.Random()
randomnr = 0
sum = 0

while(randomnr != 15 | randomnr != 25):
    randomnr = random.randint(10,30)
    sum += randomnr

print(sum)