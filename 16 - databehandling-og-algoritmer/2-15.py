print("-- Huskelista --")
 
with open("huskeliste.txt", "r" encoding="utf-8") as fil:
    huskelisten = fil.readlines()
 
brukervalg = ""
while brukervalg != "avslutt":
    for gjøremål in huskelisten:
        print(f"- {gjøremål}")
    print("Skriv nytt gjøremål for å legge til i huskelista, avslutt asvlutter programmer")
    brukervalg = input("> ")
    if brukervalg != "avslutt":
        huskelisten.append(brukervalg)
 
print("Avslutter")    
 
with open("huskeliste.txt", "w" encoding="utf-8") as fil:
    fil.writelines(huskelisten)

