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

# Print pyramide.
for rij in range(hoogte):
    for links_spatie in range(hoogte-(hoogte-1),0,-1):
        print("", end = "")
    for links_blokje in range(hoogte-links_spatie):
        print("#")
    print("\n")


