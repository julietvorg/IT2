class Pokemon:
    def __init__(self, pokemon_data: dict) -> None:
        self.id: int = pokemon_data["id"]
        self.name_english: str = pokemon_data["name"]["english"]
        self.name_japanese: str = pokemon_data["name"]["japanese"]
        self.name_chinese: str = pokemon_data["name"]["chinese"]
        self.name_french: str = pokemon_data["name"]["french"]
        self.types: list[str] = pokemon_data["type"]
        self.base_stats: dict = pokemon_data["base"]
 
    def __str__(self):
        return f"Pokemon ID: {self.id}, English Name: {self.name_english}, Japanese Name: {self.name_japanese}, Chinese Name: {self.name_chinese}, French Name: {self.name_french}, Types: {self.types}, Base Stats: {self.base_stats}"
    
    