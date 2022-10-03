import random;

random = random.Random()
randomnr1 = random.randint(1,100)
randomnr2 = random.randint(1,100)

print(randomnr1)
print(randomnr2)

if(randomnr1 < randomnr2 & randomnr1 < 50):
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")
elif(randomnr1 <30 | randomnr2 < 30):
    print("Eine der beiden ist kleiner als 30")
elif(randomnr1 < 50 & randomnr2 != 50):
    print("Erste Zahl klein, zweite kein 50iger")