from spillobjekt import Spillobjekt
from sau import Sau

class Menneske(Spillobjekt):
    def __init__(self) -> None:
        super().__init__()
        self.fart: int
        self.poeng: int
        self.baererSau: bool
    
    def beveg(self):
        pass

    def reduser_fart(self, endring: int):
        pass

    def ok_poeng(self, poeng_okning: int):
        pass

    def baer_sau(self, sau: Sau):
        pass

    def sjekk_kollisjon(self):
        pass
