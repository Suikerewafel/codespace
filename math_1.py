card_number = (input("Geef uw kaartnummer in: ")) # cijfer moet 16 nummers zijn
every_2 = sum(map(int, card_number[0::2]))
print(every_2)



