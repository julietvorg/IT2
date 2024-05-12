from pokemon import Pokemon

class Trener:
    def __init__(self, navn: str) -> None:
        self.navn: str = navn
        self.pokemonliste: list[Pokemon] = []

    def legg_til_pokemon(self, pokemon: Pokemon) -> None:
        self.pokemonliste.append(pokemon)

    def fjern_pokemon(self, pokemon: Pokemon) -> None:
        if pokemon in self.pokemonliste:
            self.pokemonliste.remove(pokemon)
            print(f"{pokemon.name_english} ble fjernet fra pokemonlisten til {self.navn}.")
        else:
            print(f"{pokemon.name_english} er ikke i pokemonlisten til {self.navn}.")

    def __str__(self) -> str:
        antall_pokemon = len(self.pokemonliste)
        return f"Trenerens navn: {self.navn}, Antall Pokemon: {antall_pokemon}"
