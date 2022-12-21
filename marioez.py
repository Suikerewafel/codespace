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
for i in range(hoogte):
     print("#")
    for j in range(hoogte - 1):
        print("#")

