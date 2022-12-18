try:
    x = int(input("x: "))
except:
    print("ongeldig")
    exit()
try:
    y = int(input("y: "))
except:
    print("ongeldig")
    exit()
print(f"het resultaat is {x + y}")
