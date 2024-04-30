import json

# Funksjon for å lese datasettet fra en JSON-fil
def les_dataset(filnavn):
    with open(filnavn, "r") as fil:
        dataset = json.load(fil)
    return dataset

# Funksjon for å finne de ti brukerne med flest Twitter-følgere
def finn_top_10_følgere(dataset):
    return sorted(dataset, key=lambda x: x["followers"], reverse=True)[:10]

# Funksjon for å regne ut og presentere antall tweets, antall følgere og følgere/følger-ratio for de ti brukerne med flest følgere
def presentere_top_10_info(dataset):
    top_10 = finn_top_10_følgere(dataset)
    print("Top 10 brukere med flest Twitter-følgere:")
    for bruker in top_10:
        print("Bruker:", bruker["username"])
        print("Antall tweets:", bruker["tweets"])
        print("Antall følgere:", bruker["followers"])
        print("Følgere/Følger-ratio:", bruker["followers"] / bruker["following"])
        print()

# Navnet på JSON-filen som inneholder datasettet
json_filnavn = "twitter_data.json"

# Leser datasettet fra JSON-filen
dataset = les_dataset(json_filnavn)

# Kjører funksjonen for å presentere informasjonen
presentere_top_10_info(dataset)