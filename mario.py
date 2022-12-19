def main():
    height = get_height()
    for i in range(height):
        for j in range(height):
            print("#", end = "")
    print()

def get_height():
    while True:
        try:
            n = int(input("height: "))
            if n > 0 and n <= 8:
                break
            else:
                print("vul een geheel getal in tussen 1 en 8")
        except:
            print("vul een geheel getal in tussen 1 en 9")
    return n

main ()
