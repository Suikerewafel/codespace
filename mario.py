while True:
    n = int(input("height: "))
    if n > 0 or n <= 8:
        break
    else:
        print("vul een geheel getal in tussen 1 en 8")

for i in range(n):
    print("#")
