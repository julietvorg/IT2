class Elev:
    """
    En klasse for elever på VGS

    Attributter
        navn(str): navnet til eleven
        alder(int): alderen til eleven
        klasse(str): bokstavklassen til eleven (eks: STG)
        fag(list[str]): en liste med fagene eleven tar

    Metoder
        legg_til_fag(fag: str): legger et fag til i faglisten
        fjern_fag(fag: str): fjerner et fag fra faglisten
        vis_info(): printer info om eleven
    """
    def __init__(self, navn: str, alder: int, klasse: str) -> None:
        self.navn: str = navn
        self.alder: int = alder
        self.klasse: str = klasse
        self.fag: list[str] = []
    def legg_til_fag(self, fag: str):
        self.fag.append(fag)
    
    def fjern_fag(self, fag: str):
        self.fag.remove(fag)
    
    def vis_info(self):
        print(f"{self.navn} ({self.alder})")

meg_selv = Elev("Thor", 33, "STG")

