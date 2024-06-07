from person import Person

class Politiker(Person):
    def __init__(self, id, fornavn, etternavn, fødselsdato, kjønn, fylke, parti, vara_representant, verdi):
        super().__init__(id, fornavn, etternavn, fødselsdato, kjønn) #ARVER FRA PERSON KLASSEN
        self.fylke = fylke
        self.parti = parti
        self.vara_representant = vara_representant
        self.verdi = verdi
    
    def __repr__(self):
        return f"Politiker({self.fornavn} {self.etternavn}, {self.parti}, {self.fylke}, Verdi: {self.verdi}))"
