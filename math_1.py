card_number = int(input("Geef uw kaartnummer in: ")) # cijfer moet 16 nummers zijn
last_number = card_number % 10
sum_2 = sum(map(int, card_number[0::2]))
print(sum_2)

