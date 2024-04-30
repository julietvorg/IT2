from spillobjekt import Spillobjekt

class Sau(Spillobjekt):
    def __init__(self) -> None:
        super().__init__()
        self.blir_baaret: bool
    
    def blir_loftet(self):
        pass

    def fjern_sau(self):
        pass