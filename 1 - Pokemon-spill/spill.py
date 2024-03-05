import os
import platform
import json
from pokemon import Pokemon
from trener import Trener
 
def rens_terminal():
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

with open("pokemon.json", "r", encoding="utf-8") as fil:
    data = json.load (fil)
    pokemoner_data = data

pokemoner = []

for pokemon_data in pokemoner_data:
    ny_pokemon = Pokemon(pokemon_data)
    pokemoner.append(ny_pokemon)
 
while True:
    rens_terminal()
    print("-- Pokemon --")  
    print("1: Se pokemonoversikt")
    print("2: Se treneroversikt")
    print("3: Lag trener")
    print("4: Avslutt")
    brukervalg = input(">")

    if brukervalg == "1":
        print("-- Pokemonoversikt --")
        for pokemon in pokemoner:
            print(pokemon)
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "2":
        print("-- Treneroversikt --")
        print("Liste over alle trenere:")
        for trener in trenere_liste:
            print(trener)
    elif brukervalg == "3":
        print("Legg til trener")
        navn = input("Hva er navnet på treneren?")
        ny_trener = Trener(navn)
        trenere_liste.append(ny_trener)
        print(f"{navn} har blitt lagt til som trener med en tom liste av Pokémon.")
    elif brukervalg == "4":
        print("Avslutter")
        break 
    else:
        print("Ugyldig valg")
        input("Trykk enter for å gå tilbake til hovedmenyen")

print("Takk for nå")






