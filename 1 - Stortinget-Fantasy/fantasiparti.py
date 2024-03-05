from politiker import Politiker

class Fantasiparti:
    def __init__ (self, navn: str, eier: str) -> None:
        self.navn: str = navn
        self.eier: str = eier
        self.poeng: int = 0
        self.saldo: int = 100_000
        self.partileder: Politiker = None
        self.politikere: list[Politiker] = []

    def __str__(self):
        return f"{self.navn} - {self.eier} ({self.poeng} poeng, {self.saldo} kr)"

    def kjøp_politiker(self, politiker: Politiker):
        if self.saldo >= politiker.verdi and politiker not in self.politikere:
            self.saldo -= politiker.verdi
            self.politikere.append(politiker)
        else:
            print("FEIL! Avvist, manglende saldo")

    def selg_politiker(self, politiker: Politiker):
        if politiker in self.politikere:
            self.politikere.remove(politiker)
            self.saldo += politiker.verdi
        else:
            print("FEIL! Politikeren er ikke med i partiet")


    def vis_parti(self):
        print(f"-- {self.navn} --")
        print(f"Poeng: {self.poeng}")
        print(f"Saldo: {self.saldo}")
        print("Medlemmer")
        for politiker in self.politikere:
            print(politiker)
        print()



if __name__ == "__main__":
    print("Tester Fantasiparti-klassen")
    testparti_1 = Fantasiparti("Apolitisk Testparti", "Test Testesen")
    testparti_2 = Fantasiparti("Politisk Testparti", "Stolt Jensenberg")
    print(testparti_1)
    print(testparti_2)

