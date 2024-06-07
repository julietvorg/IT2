from spiller import Spiller
from hovedprogram import last_inn_politikere
from hjelpefunksjoner import enkelt_regnestykke

def hovedmeny():
    print("Velkommen til Stortinget-Fantasy!")
    fornavn = input("Skriv inn fornavnet ditt: ")
    etternavn = input("Skriv inn etternavnet ditt: ")
    id = input("Skriv inn ID-en din: ")
    fødselsdato = input("Skriv inn fødselsdatoen din (ÅÅÅÅ-MM-DD): ")
    kjønn = input("Skriv inn kjønnet ditt: ")
    spiller = Spiller(id,fornavn, etternavn, fødselsdato, kjønn)
    politikere = last_inn_politikere("stortinget.json")

    if not politikere:
        print("Ingen politikere lastet inn, avslutter spillet.")
        return

    while True:
        print("\nHva vil du gjøre?")
        print("1. Se alle politikere")
        print("2. Kjøp en politiker")
        print("3. Selg en politiker")
        print("4. Se portefølje")
        print("5. Gjør et regnestykke for å tjene penger")
        print("6. Opprett et parti")
        print("7. Se ditt parti")
        print("8. Avslutt")
        
        valg = input("Skriv inn ditt valg (1-8): ")
        
        if valg == "1":
            for politiker in politikere:
                print(politiker)
        elif valg == "2":
            id = input("Skriv inn ID til politikeren du vil kjøpe: ")
            politiker = next((p for p in politikere if p.id == id), None)
            if politiker:
                spiller.kjøp_politiker(politiker)
            else:
                print("Fant ikke politikeren")
        elif valg == "3":
            id = input("Skriv inn ID til politikeren du vil selge: ")
            politiker = next((p for p in spiller.portefølje if p.id == id), None)
            if politiker:
                spiller.selg_politiker(politiker)
            else:
                print("Du eier ikke denne politikeren")
        elif valg == "4":
            print(spiller)
        elif valg == "5":
            # Tjen penger fra regnestykket
            tjent_beløp = enkelt_regnestykke()  
            # Øk spillerens kapital med beløpet de tjener fra regnestykket
            spiller.kapital += tjent_beløp
        elif valg == "6":
            parti_id = input("Skriv inn en ID for partiet ditt: ")
            parti_navn = input("Skriv inn et navn for partiet ditt: ")
            spiller.opprett_parti(parti_id, parti_navn)
        elif valg == "7":
            if spiller.parti:
                print(spiller.parti)
            else:
                print("Du har ikke opprettet et parti ennå.")
            
        elif valg == "8":
            print("Takk for at du spilte!")
            break
        else:
            print("Ugyldig valg, prøv igjen.")

        


if __name__ == "__main__":
    hovedmeny()

