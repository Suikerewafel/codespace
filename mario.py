def main():
    height = get_height()
    for i in range(height):
        print("#")

def get_height():
    while True:
        n = int(input("height: "))
        if n > 0 and n <= 8:
            break
        else:
            print("vul een geheel getal in tussen 1 en 8")
    return n

main ()
