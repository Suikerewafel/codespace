# Ask user input.
while True:
    try:
        hoogte = int(input("Geef de hoogte in: "))
        if hoogte < 9 and hoogte > 0:
            break
        else:
            print("Geef een getal in tussen 0 en 8")
    except:
        print("Dit is geen getal")

# Print pyramide
for rij in range(hoogte):
    for i in range(hoogte-rij-1, 0, -1):
        print(" ", end = "")
    for j in range(rij+1):
        print("#", end = "")
    for h in range(hoogte):
        print("    ", end = "")
    for k in range(rij+1):
        print("#", end = "")
    print("\n", end = "")


