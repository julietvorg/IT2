import random

def enkelt_regnestykke():
    # Generer to tilfeldige tall mellom 1 og 10
    tall1 = random.randint(1, 10)
    tall2 = random.randint(1, 10)

    # Velg en tilfeldig operasjon
    operasjon = random.choice(['+', '-', '*'])

    # Lag regnestykket som en streng
    regnestykke = f"{tall1} {operasjon} {tall2}"

    # Evaluer regnestykket for å få svaret
    svar = eval(regnestykke)

    # Spør spilleren om svaret
    bruker_svar = input(f"Hva er {regnestykke}? ")

    # Sjekk om svaret er riktig
    if bruker_svar.isdigit() and int(bruker_svar) == svar:
        print("Riktig svar! Du har tjent 1000 kr.")
        return 1000
    else:
        print("Feil svar. Bedre lykke neste gang.")
        return 0
