# Et program som fortsetter helt til bruker har skrevet riktig input.

år = 2024     # oppretter en variabel år som får verdien 2024

while True: # while-løkke som kjører uansett input
    try: # forsøke å kjøre koden
        alder = int(input("Hvor gammel blir du i år?")) # oppretter variabelen alder som får verdien av det brukeren skriver inn
        break # hopper ut av løkken
    except: # hvis koden ikke funker vil dette skje:
        print("Ugyldig input. Input må være et tall") # printer "Ugyldig input", hvis brukeren har skrevet inn noe annet enn tall

fødselsår = år - alder # finner fødselsår ved å ta året minus alderen brukeren blir i år.
print(f"Du er født i {fødselsår}") # printer året brukeren blir født.

