








try:
    while(true):
        hoogte = int(input("Geef de hoogte in: "))
        if hoogte < 9 and hoogte > 0:
            break
        else:
            print("Geef een getal in tussen 0 en 8")
except:
    print("Dit is geen getal")

print(f"{hoogte}")