import random;
random = random.Random()
endless = True
ownScore = 0
compScore = 0

print("Was möchtest du machen?")
print("1 ... würfeln")
print("2 ... Gegner Würfeln lassen")
print("3 ... Auflösen")

while endless:
    selection = int(input())
    if selection == 1:
        print("Du bist dran ...")
        sum = 0
        for i in range(0,6):
            wuerfel = random.randint(1,6)
            ownScore += wuerfel
        print("Du hast " + str(ownScore) + " gewürfelt.")
    elif selection == 2:
        print("Dein Gegner würfelt gerade ...")
        sum = 0
        for i in range(0,6):
            wuerfel = random.randint(1,6)
            compScore += wuerfel
        print("Dein Gegner hat " + str(compScore) + " gewürfelt.")
    elif selection == 3:
        if ownScore > compScore:
            print("Du hast gewonnen")
            break
        elif ownScore < compScore:
            print("Du hast verloren")
            break
        else:
            print("Ihr habt ein unentschieden!")
            break
    else:
        print("falsche Eingabe!")
        break
   