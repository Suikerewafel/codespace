scores = []

while True:
    aantal = int(input("vul het aantal scores in dat u wilt ingeven: "))
    try:
       if aantal > 0:
            break
        else:
            print("vul een getal groter dan 0 in")
    except:
        print("Vul een getal groter dan 0 in")

for i in range(aantal):
    score = int(input("Score: "))
    scores.append(score)
