from parti import Parti
from person import Person


class Spiller(Person):
    def __init__(self, id, fornavn, etternavn, fødselsdato, kjønn, startkapital=2000):
        super().__init__(id, fornavn, etternavn, fødselsdato, kjønn)
        self.portefølje = []
        self.kapital = startkapital
        self.parti = None  # Spillerens eget parti
    
    def opprett_parti(self, parti_id, parti_navn):
        if not self.parti:
            self.parti = Parti(parti_id, parti_navn)
            print(f"{self.fornavn} {self.etternavn} har opprettet partiet {parti_navn}.")
        else:
            print(f"{self.fornavn} {self.etternavn} har allerede opprettet et parti.")


    def kjøp_politiker(self, politiker):
        if self.kapital >= politiker.verdi:
            self.portefølje.append(politiker)
            self.kapital -= politiker.verdi
            if self.parti:
                self.parti.legg_til_politiker(politiker)
                print(f"{politiker.fornavn} {politiker.etternavn} ble lagt til i partiet {self.parti.navn}.")
            else:
                print("Spilleren har ikke opprettet et parti ennå.")
            print(f"{self.fornavn} {self.etternavn} kjøpte {politiker.fornavn} {politiker.etternavn} for {politiker.verdi} kr.")
        else:
            print("Du har ikke nok kapital til å kjøpe denne politikeren.")


    def selg_politiker(self, politiker):
        if politiker in self.portefølje:
            self.portefølje.remove(politiker)
            self.kapital += politiker.verdi
            if self.parti:
                self.parti.politikere.remove(politiker)
            print(f"{self.fornavn} {self.etternavn} solgte {politiker.fornavn} {politiker.etternavn} for {politiker.verdi} kr.")
        else:
            print(f"{politiker.fornavn} {politiker.etternavn} er ikke i porteføljen")

    def __repr__(self):
        politiker_info = ", ".join([f"{politiker.fornavn} {politiker.etternavn}" for politiker in self.portefølje])
        if self.parti:
            parti_info = f"Parti: {self.parti.navn} (Politikere: {len(self.parti.politikere)})"
        else:
            parti_info = "Ingen parti opprettet ennå."
        return f"Spiller({super().__repr__()}, Kapital: {self.kapital} kr, Portefølje: [{politiker_info}], {parti_info})"
