class Person:
    # Definerer en ny klasse kalt 'Person'
    
    def __init__(self, id, fornavn, etternavn, fødselsdato, kjønn):
        # Initialiserer Person-objektet med attributtene id, fornavn, etternavn, fødselsdato og kjønn
        self.id = id
        # Setter attributtet 'id' til verdien som gis ved opprettelsen av objektet
        self.fornavn = fornavn
        # Setter attributtet 'fornavn' til verdien som gis ved opprettelsen av objektet
        self.etternavn = etternavn
        # Setter attributtet 'etternavn' til verdien som gis ved opprettelsen av objektet
        self.fødselsdato = fødselsdato
        # Setter attributtet 'fødselsdato' til verdien som gis ved opprettelsen av objektet
        self.kjønn = kjønn
        # Setter attributtet 'kjønn' til verdien som gis ved opprettelsen av objektet
    
    def __repr__(self):
        # Definerer metoden __repr__ som returnerer en strengrepresentasjon av objektet
        return f"Person({self.fornavn} {self.etternavn}, Fødselsdato: {self.fødselsdato}, Kjønn: {self.kjønn})"
        # Returnerer en streng som representerer objektet i et lesbart format
