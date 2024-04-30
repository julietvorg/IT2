from sang import Sang

class Spilleliste():
    def __init__(self, navn: str) -> None:
        self.navn: str = navn
        self.sanger: list[Sang] = []
    
    def legg_til_sang(self, sang: Sang) -> None:
        self.sanger.append(sang)
    
    def lengde(self) -> int:
        return len(self.sanger)

    def spill_alle(self) -> None:
        for sang in self.sanger:
            sang.spill()
    
    def tittel_i_liste(self, tittel: str) -> bool:
        for sang in self.sanger:
            if sang.sjekk_tittel(tittel):
                return True
        return False
    
    def artistliste(self, artist: str) -> list[Sang]:
        artistliste = []
        for sang in self.sanger:
            if sang.sjekk_artist(artist):
                artistliste.append(sang)
        return artistliste

if __name__ == "__main__":
    min_liste = Spilleliste("Norske favoritter 2023")
    min_liste.legg_til_sang(Sang("Evig Ferie", "Oslo vet, Pt.2"))
    min_liste.legg_til_sang(Sang("Evig Ferie", "Seint i går"))
    min_liste.legg_til_sang(Sang("Fieh", "Supergud"))
    min_liste.legg_til_sang(Sang("Slomosa", "There is Nothing New Under the Sun"))
    min_liste.legg_til_sang(Sang("Bo Milli", "Making Friends"))

    print(min_liste.lengde()) # -> 5
    min_liste.spill_alle()
    print(min_liste.tittel_i_liste("Supergud")) # -> True
    print(min_liste.tittel_i_liste("EARFQUAKE")) # -> False
    print(min_liste.artistliste("Evig Ferie")) # -> [<__main__.Sang object at 0x000002BF52981100>, <__main__.Sang object at 0x000002BF529813A0>]
