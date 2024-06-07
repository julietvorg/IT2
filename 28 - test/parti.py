class Parti:
    def __init__(self, id, navn):
        self.id = id
        self.navn = navn
    
    def __repr__(self):
        return f"Parti({self.navn})"

