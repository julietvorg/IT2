class Parti:
    def __init__(self, id, navn):
        self.id = id
        self.navn = navn
        self.politikere = []  # Liste over politikere i partiet
    
    def legg_til_politiker(self, politiker):
        self.politikere.append(politiker)
        print(f"{politiker.fornavn} {politiker.etternavn} ble lagt til i partiet {self.navn}.")
    
    def __repr__(self):
        return f"Parti({self.navn}, Politikere: {len(self.politikere)})"

