# Et program som finner fødselsår basert på alder.

år = 2024
try:
    alder = int(input("Hvor gammel blir du i år?"))
    fødselsår = år - alder
    print(f"Du er født i {fødselsår}")
except:
    print ("Ugyldig input. Input må være et tall.")

print ("Koden fortsetter..")   

# Håndtering av feil brukes for at koden ikke skal avslutte hvis bruker skriver inn noe feil.


# Et annet eksempel

try:
    tall =int(input("Skriv et tall: "))
except:
    print("FEIL! Input er ikke et tall. 'tall' får verdien 10")
    tall = 10
print(tall) # Hvis bruker ikke skriver inn et tall vil bruker få ut standarsverdi 10 (i stedet for at spiller avslutter)


