try:
    x = int(input("x: "))
except ValueError:
    print("ongeldig")
    exit()
try:
    y = int(input("y: "))
except ValueError:
    print("ongeldig")
    exit()
print(f"het resultaat is {x + y}")
