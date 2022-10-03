kontostand = 0

print("Was möchtest du machen?")
print("1 ... Einzahlen")
print("2 ... Abheben")
print("3 ... Kontostand")
print("4 ... Beenden")

while True:
    selection = int(input())
    if selection == 1:
        print("Wie viel möchtest du Einzahlen?")
        einzahlen = int(input())
        kontostand += einzahlen
        print("Sie haben " + str(einzahlen) + "€ eingezahlt!")
    elif selection == 2:
        print("Wie viel möchtest du Abheben?")
        abheben = int(input())
        kontostand -= abheben
        print("Sie haben " + str(abheben) + "€ abgehoben!")
    elif selection == 3:
        print("Dein Kontostand beträgt: " + str(kontostand))
    elif selection == 4:
        break
    else:
        print("Your input was incorrect!")