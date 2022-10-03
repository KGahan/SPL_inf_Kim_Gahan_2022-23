import random;

random = random.Random()
randomnr1 = random.randint(1,100)

print(randomnr1)

if(randomnr1 < 20):
    print("Mini")
elif(randomnr1 <= 50):
    print("Medium")
elif(randomnr1 > 50):
    print("Large")