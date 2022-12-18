try:
    while True:
        n = int(input("Geef het getal in dat u wilt bekijken: "))
        if n <= 0:
            break
except:
    print("Dit is geen geheel getal en kan dus niet even zijn")
    exit()

if n % 2 == 0:
    print("Het getal is even")
else:
    print("Het getal is oneven")

