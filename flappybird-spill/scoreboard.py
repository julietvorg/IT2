import pygame

# Scoreboard-klassen i spillet holder styr på spillerens poengsum. 
# Den oppretter et tekstobjekt som viser poengsummen på skjermen og 
# oppdaterer det når poengsummen endres. 
# I tillegg registrerer den hvilket rør som spilleren sist scoret poeng på.

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
    # brukes til å sette opp objektet, 
    # for eksempel ved å tilordne verdier til egenskaper når et nytt objekt lages
        super().__init__() # Arver forelderklasse pygame.sprite.Sprite
        self.score = 0 # Variabel for å holde styr på spillerens poengsum
        self.font = pygame.font.Font(None, 36)  # Oppretter en font for å vise poengsummen
        self.rendered_score = self.font.render(str(self.score), True, (0, 0, 0))  # Lager poengsummen som et tekstobjekt # Black color
        self.rect = self.rendered_score.get_rect() # Henter rektangelet som omslutter tekstobjektet
        self.rect.topleft = (10, 10) # Setter posisjonen til poengsummen øverst til venstre på skjermen
        self.last_scored_pipe = None # Holder styr på den siste røret hvor poeng ble scoret

    def update(self):
        self.rendered_score = self.font.render(str(self.score), True, (0, 0, 0)) ## Oppdaterer poengsummen som et tekstobjekt # Black color
