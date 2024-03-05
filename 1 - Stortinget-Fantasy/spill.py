import os
import sys
from politiker import Politiker
import json
from fantasiparti import Fantasiparti


def rens_terminal():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

with open("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load (fil)
    politikere_data = data ["dagensrepresentanter_liste"]

politikere = []
for politiker_ordbok in politikere_data:
    ny_politiker = Politiker(politiker_ordbok)
    politikere.append(ny_politiker)

print("-- Velkommen til Stortinget-fantasy --")

print()
print("Du må stifte er parti for å spille.")
print("Hva skal partiet ditt hete?")
partinavn = input ("> ")
print("Hva heter du?")
spillernavn = input("> ")
spillerparti = Fantasiparti(partinavn, spillernavn)
print(f"Gratulerer! Det nye partiet {partinavn} ble stiftet med partilederen {spillernavn}!")
input("Trykk enter for å starte spillet")

while True:
    rens_terminal()
    print("-- Stortinget-fantasy --")
    print("1: Vis politikeroversikt")
    print("2: Mitt parti")
    print("3: Avslutt")
    brukervalg = input(">")
    
    if brukervalg == "1":
        print("-- Politikeroversikt --")
        for politiker in politikere:
            print(politiker)
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "2":
        print("Mitt parti")
    elif brukervalg == "3":
        print("Avslutter..")
        break 
    else:
        print("Ugyldig valg")
        input("Trykk enter for å gå tilbake til hovedmenyen")

print("Takk for nå")