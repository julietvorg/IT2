class Politiker:
    def __init__(self, id, fornavn, etternavn, fødselsdato, kjønn, fylke, parti, vara_representant):
        self.id = id
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fødselsdato = fødselsdato
        self.kjønn = kjønn
        self.fylke = fylke
        self.parti = parti
        self.vara_representant = vara_representant
    
    def __repr__(self):
        return f"Politiker({self.fornavn} {self.etternavn}, {self.parti}, {self.fylke})"
