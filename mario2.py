while True:
    try:
        hoogte = int(input("Voer de gewenste hoogte in: "))
        if hoogte > 0 and hoogte < 8:
            break
        else:
            print("Voer een getal in tussen 1 en 8")
    except:
        print("Dit is geen getal")
