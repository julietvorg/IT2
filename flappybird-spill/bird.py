import pygame

class Bird(pygame.sprite.Sprite):
    """
    En klasse som representerer fuglen i spillet.

    Parametere:
        screen_width (int): Bredden på skjermen.
        screen_height (int): Høyden på skjermen.
    """
    def __init__(self, screen_width, screen_height):
        """
        Initialiserer en ny instans av Bird.

        Parametere:
            screen_width (int): Bredden på skjermen.
            screen_height (int): Høyden på skjermen.
        """
        super().__init__()
        self.image = pygame.Surface((50, 50)) # Lager et overflateobjekt med størrelse 50x50 piksler
        self.image.fill((255, 255, 0)) # Fyller overflateobjektet med gul farge
        self.rect = self.image.get_rect() # Henter rektangelet som omslutter bildet
        self.rect.center = (screen_width // 4, screen_height // 2) # Plasserer fuglen i startposisjonen
        self.velocity = 0 # Fart til fuglen
        self.gravity = 0.5 # Gravitasjonens påvirkning på fuglen
        self.jump_strength = -10 # Styrken til hoppet

    def update(self):
        """
        Oppdaterer posisjonen til fuglen basert på tastetrykk og gravitasjon.
        """
        keys = pygame.key.get_pressed() # Sjekker hvilke taster som er trykket
        if keys[pygame.K_UP]: # Hvis opp-tasten er trykket
            self.velocity = self.jump_strength # Setter fuglens vertikale fart til hoppstyrken

        self.velocity += self.gravity # Legger til gravitasjonens effekt på fuglens fart
        self.rect.y += self.velocity # Oppdaterer fuglens vertikale posisjon basert på farten
