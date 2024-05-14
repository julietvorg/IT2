import pygame

# Bird-klassen styrer oppførselen til fuglen i spillet. 
# Den lar spillere hoppe ved å trykke på tastaturet og 
# kontrollerer fuglens bevegelse med gravitasjonen, som trekker den nedover.


# En sprite er et grafisk objekt eller en bildebeholder som representerer en spillfigur, et spillobjekt eller en annen visuell komponent i et spill.
class Bird(pygame.sprite.Sprite): 
# brukes til å organisere og håndtere grafiske elementer på skjermen. 
# betyr det at Bird-klassen er en type sprite, og den vil arve funksjonalitet fra pygame.sprite.Sprite, slik at jeg kan opprette og administrere fugle-objekter som sprite-objekter i spillet ditt.
    """
    En klasse som representerer fuglen i spillet.

    Parametere:
        screen_width (int): Bredden på skjermen.
        screen_height (int): Høyden på skjermen.
    """
    def __init__(self, screen_width, screen_height): # kalles når vi lager en ny fugl i spillet. Den trenger to tall: bredden og høyden på skjermen, slik at den kan plassere fuglen riktig.
        """
        Initialiserer en ny instans av Bird.

        Parametere:
            screen_width (int): Bredden på skjermen.
            screen_height (int): Høyden på skjermen.
        """
        super().__init__() ## Kalles for å starte opp den overordnede klassen (pygame.sprite.Sprite i dette tilfellet) # at alle attributter og metoder som tilhører pygame.sprite.Sprite blir tilgjengelige for vår Bird-klasse. Så, "starte opp" betyr å gjøre klar og gjøre den overordnede klassens funksjonalitet tilgjengelig for vår egen klasse.
        self.image = pygame.Surface((50, 50)) # Lager et overflateobjekt med størrelse 50x50 piksler
        self.image.fill((255, 255, 0)) # Fyller overflateobjektet med gul farge
        self.rect = self.image.get_rect() ## Henter rektangelet som omslutter bildet, brukes til kollisjon og posisjonering
        self.rect.center = (screen_width // 4, screen_height // 2) # Plasserer fuglen i startposisjonen (midt på venstre side av skjermen vertikalt)
        self.velocity = 0 # Fart til fuglen
        self.gravity = 0.5 # Gravitasjonens påvirkning på fuglen (jo høyere tall, jo sterkere gravitasjon)
        self.jump_strength = -10 # Styrken til hoppet (negativ verdi fordi vi vil at fuglen skal gå oppover når den hopper)
        # self refererer til selve objektet når du kaller en metode på det. Det lar deg få tilgang til egenskaper og metoder som tilhører det spesifikke objektet.
    def update(self): 
        """
        Oppdaterer posisjonen til fuglen basert på tastetrykk og gravitasjon.
        """
        keys = pygame.key.get_pressed() ## Sjekker hvilke taster som er trykket, henter en liste over alle taster som er trykket
        if keys[pygame.K_UP]: # Hvis opp-tasten er trykket
            self.velocity = self.jump_strength # Setter fuglens vertikale fart til hoppstyrken

        self.velocity += self.gravity # Legger til gravitasjonens effekt på fuglens fart
        self.rect.y += self.velocity # Oppdaterer fuglens vertikale posisjon basert på farten
