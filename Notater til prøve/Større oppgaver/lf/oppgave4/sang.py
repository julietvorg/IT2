class Sang():
    def __init__(self, artist: str, tittel: str) -> None:
        self.artist: str = artist
        self.tittel: str = tittel
        self.avspillinger: int = 0
    
    def spill(self):
        print(f"Spiller: {self.tittel} - {self.artist}")
        self.avspillinger += 1
    
    def sjekk_tittel(self, tittel: str) -> bool:
        return tittel == self.tittel
    
    def sjekk_artist(self, artist: str) -> bool:
        return artist == self.artist
    
    # Bonus:
    def __repr__(self) -> str:
        return f"Sang ({self.artist} - {self.tittel})"

if __name__ == "__main__":
    sang1 = Sang("tigerstate", "Look In Her Eyes")
    sang1.spill()
    print(sang1.avspillinger)
    print(sang1.sjekk_tittel("Look In Her Eyes"))
    print(sang1.sjekk_tittel("look in her eyes"))
    print(sang1.sjekk_artist("tigerstate"))
    print(sang1.sjekk_artist("Fieh"))
