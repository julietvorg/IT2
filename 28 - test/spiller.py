class Spiller:
    def __init__(self, navn):
        self.navn = navn
        self.portefølje = []

    def kjøp_politiker(self, politiker):
        self.portefølje.append(politiker)
        print(f"{self.navn} kjøpte {politiker.fornavn} {politiker.etternavn}")

    def selg_politiker(self, politiker):
        if politiker in self.portefølje:
            self.portefølje.remove(politiker)
            print(f"{self.navn} solgte {politiker.fornavn} {politiker.etternavn}")
        else:
            print(f"{politiker.fornavn} {politiker.etternavn} er ikke i porteføljen")

    def __repr__(self):
        return f"Spiller({self.navn}, Portefølje: {self.portefølje})"

