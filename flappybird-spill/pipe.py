import pygame

# Pipe-klassen håndterer opprettelsen av rør i spillet. 
# Disse rørene kan være vanlige eller omvendte, og de beveger seg kontinuerlig mot venstre. 
# Klassen angir farger for rørene, 
# og den har funksjoner for å oppdatere både rørets posisjon og farge.

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, height, color, inverted=False):
        # hvis det ikke er en verdi for "inverted" når man oppretter et nytt Pipe-objekt, vil den være satt til False som standard.
        # da vil røret bli plassert med den øvre delen av røret øverst og den nedre delen nederst.
        super().__init__() # Initialiserer forelderklasse pygame.sprite.Sprite
        self.image = pygame.Surface((50, height)) # Oppretter en overflate for røret med angitt bredde og høyde
        self.image.fill(color) # Fyller rørets overflate med angitt farge
        self.rect = self.image.get_rect() # Henter rektangelet som omslutter røret
        self.rect.x = x # Setter rørets x-posisjon
        self.color = color # Lagrer fargen til røret
        self.update_color(color) # Setter fargen, oppdaterer fargen til røret
        if inverted: # Hvis røret er omvendt
            self.image = pygame.transform.flip(self.image, False, True) # Snur røret opp ned
            # False and True gjør bilde speilvendt langs den vertikale aksen, men ikke langs den horisontale aksen
            self.rect.bottomleft = (x, y) # Setter rørets posisjon til nederst til venstre
        else:
            self.rect.topleft = (x, y) # Setter rørets posisjon til øverst til venstre

    def update(self):
        self.rect.x -= 5  # Flytter røret mot venstre med en konstant hastighet

    def update_color(self, color):  
        self.color = color  # Oppdaterer rørets farge
        self.image.fill(self.color) # Fyller rørets overflate med den nye fargen
