
poeng = 0

print ("Velkommen til Quiz")
print ("Hva er hovedstaden i Danmark?")
print("Svaralternativer: A: Oslo, B: København, C: Amsterdam")
svar = input("Ditt svar: ")
if svar == "B":
    print("Riktig")
    poeng += 1
    print ("Nå har du", poeng, "poeng")
else:
    print ("Feil svar")
    print ("Når har du", poeng, "poeng")