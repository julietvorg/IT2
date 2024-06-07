import json  # Importerer json-modulen for å kunne håndtere JSON-filer
from politiker import Politiker  # Importerer Politiker-klassen fra politiker-modulen
from parti import Parti  # Importerer Parti-klassen fra parti-modulen

def last_inn_politikere(filnavn):  # Definerer funksjonen last_inn_politikere som tar filnavn som parameter
    try:
        with open(filnavn, "r", encoding="utf-8") as fil:  # Åpner filen i lesemodus 
            data = json.load(fil)  # Laster innholdet i filen som JSON
    except Exception as e:  # Håndterer eventuelle unntak som oppstår ved filåpning eller JSON-parsing
        print(f"Feil ved lasting av JSON-fil: {e}")  # Skriver ut en feilmelding hvis det oppstår et unntak
        return []  # Returnerer en tom liste hvis det oppstår en feil

    politikere = []  # Initialiserer en tom liste for å lagre politikere
    try:
        for item in data['representanter_oversikt']['representanter_liste']['representant']:  # Itererer gjennom listen av representanter i JSON-dataen
            parti = Parti(item['parti']['id'], item['parti']['navn'])  # Oppretter et Parti-objekt med id og navn fra JSON-dataen
            try:
                verdi = item['verdi']  # Forsøker å hente verdi-attributtet fra JSON-dataen
            except KeyError:  # Håndterer unntak hvis verdi-attributtet ikke finnes
                print("Politikeren mangler verdiattributt. Standardverdi brukes.")  # Skriver ut en melding hvis verdi mangler
                verdi = 1000  # Setter standardverdi til 1000 hvis verdi mangler
            politiker = Politiker(  # Oppretter et Politiker-objekt med data fra JSON
                id=item['id'],
                fornavn=item['fornavn'],
                etternavn=item['etternavn'],
                fødselsdato=item['foedselsdato'],
                kjønn=item['kjoenn'],
                fylke=item['fylke']['navn'],
                parti=parti,
                vara_representant=item['vara_representant'],
                verdi=verdi  # Legger til verdiattributtet til Politiker-objektet
            )
            politikere.append(politiker)  # Legger det opprettede Politiker-objektet til i politikere-listen
    except Exception as e:  # Håndterer eventuelle unntak som oppstår under opprettelsen av Politiker-objektene
        print(f"Feil ved opprettelse av politikere: {e}")  # Skriver ut en feilmelding hvis det oppstår et unntak

    return politikere  # Returnerer listen med politikere

if __name__ == "__main__":  # Sjekker om scriptet kjøres som hovedprogram
    politikere = last_inn_politikere("stortinget.json")  # Kaller last_inn_politikere-funksjonen med filnavnet "stortinget.json"
    for politiker in politikere:  # Itererer gjennom listen av politikere
        print(politiker)  # Skriver ut hver politiker i listen
