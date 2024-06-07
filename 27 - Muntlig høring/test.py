try:
    alder = int(input("Hvor gammel er du?"))
    fødselsår = 2024 - alder
    print(f"Du er født i {fødselsår}")
except:
    print("Ugyldig input")