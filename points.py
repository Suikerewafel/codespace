
points = int(input("hoeveel punten heb je verloren?"))
mypoints = int(5)

if points > mypoints:
    print("winner winner chicken dinner")
elif points < mypoints:
    print("loser!")
else:
    print("we are brothers")
