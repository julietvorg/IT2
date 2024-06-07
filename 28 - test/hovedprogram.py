import json
from politiker import Politiker
from parti import Parti

def last_inn_politikere(filnavn):
    try:
        with open(filnavn, "r", encoding="utf-8") as fil:
            data = json.load(fil)
    except Exception as e:
        print(f"Feil ved lasting av JSON-fil: {e}")
        return []

    politikere = []
    try:
        for item in data['representanter_oversikt']['representanter_liste']['representant']:
            parti = Parti(item['parti']['id'], item['parti']['navn'])
            politiker = Politiker(
                id=item['id'],
                fornavn=item['fornavn'],
                etternavn=item['etternavn'],
                fødselsdato=item['foedselsdato'],
                kjønn=item['kjoenn'],
                fylke=item['fylke']['navn'],
                parti=parti,
                vara_representant=item['vara_representant']
            )
            politikere.append(politiker)
    except Exception as e:
        print(f"Feil ved opprettelse av politikere: {e}")

    return politikere

if __name__ == "__main__":
    politikere = last_inn_politikere("stortinget.json")
    for politiker in politikere:
        print(politiker)
