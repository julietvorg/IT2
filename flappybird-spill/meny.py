import pygame

# Denne koden viser en enkel meny for et spill ved hjelp av Pygame. 
# Den oppretter menyelementer som lar brukeren starte spillet, 
# vise forrige poengsum og avslutte spillet. 
# Brukeren kan klikke på disse elementene med musen for å utføre handlingene. 
# Koden håndterer også oppdatering og visning av menyen på skjermen.

# Definerer farger
LIGHT_BLUE = (0, 191, 255)
BLACK = (0, 0, 0)

# Oppsett for skjermen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Tekstklassen for menyelementer
class MenuItem(pygame.sprite.Sprite): # MenuItem er et element i menyen til et spill, og den arver funksjonaliteten til pygame.sprite.Sprite
    def __init__(self, text, font, position):
        super().__init__() # Arver fra forelderklasse pygame.sprite.Sprite
        self.text = text # Lagrer teksten for menyelementet
        self.font = font # Lagrer fonten som skal brukes til å vise teksten
        self.image = self.font.render(self.text, True, BLACK)  # Lager teksten som et bilde med svart farge
        self.rect = self.image.get_rect() # Henter rektangelet som omslutter teksten (usynlig rektangel rundt teksten)
        self.rect.topleft = position # Setter posisjonen til teksten på skjermen

## Funksjon for å vise menyen
def show_menu(screen, previous_score):
    # Initialiserer menyelementer
    menu_font = pygame.font.Font(None, 36) # Oppretter en font for menyteksten
    title_text = "Flappy Bird" # Titteltekst for menyen
    previous_score_text = "Forrige poengsum: " + str(previous_score) # Tekst for forrige poengsum
    # str() til å konvertere previous_score, som antas å være et tall, til en tekst-streng slik at den kan vises som tekst i menyen
    start_item = MenuItem("Start Spill", menu_font, (SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 - 50)) # Menyvalg for å starte spillet
    score_item = MenuItem(previous_score_text, menu_font, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2)) # Viser forrige poengsum
    quit_item = MenuItem("Avslutt", menu_font, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50)) # Menyvalg for å avslutte
    all_sprites = pygame.sprite.Group(start_item, score_item, quit_item) # Gruppe som inneholder alle menyelementene


    # Spillhovedløkke for menyen
    running = True 
    while running:
        for event in pygame.event.get(): # Løkke for hendelser
            if event.type == pygame.QUIT: # Hvis vinduet lukkes
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN: # Hvis det klikkes med musen
                if start_item.rect.collidepoint(pygame.mouse.get_pos()): # Hvis brukeren klikker på "Start Spill"
                    return 0 # Starter spillet på nytt, så forrige poengsum blir null
                elif quit_item.rect.collidepoint(pygame.mouse.get_pos()): # Hvis brukeren klikker på "Avslutt"
                    pygame.quit()
                    quit()

        # Oppdaterer teksten for forrige poengsum
        previous_score_text = "Forrige poengsum: " + str(previous_score)
        score_item = MenuItem(previous_score_text, menu_font, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2)) 
        all_sprites = pygame.sprite.Group(start_item, score_item, quit_item)  # Oppdater gruppen med den nye teksten

        # Oppdaterer og tegner menyen
        screen.fill(LIGHT_BLUE) # Fyller skjermen med hvit farge
        all_sprites.update() # Oppdaterer alle menyelementene
        all_sprites.draw(screen) # Tegner alle menyelementene på skjermen
        pygame.display.flip() # Oppdaterer skjermen

# Testkjøring av menyen
if __name__ == "__main__": # sjekker om koden blir kjørt som et selvstendig program, hvis den gjør vil koden under kjøre
    pygame.init() # Initialiserer pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Setter opp skjermen
    pygame.display.set_caption("Flappy Bird - Meny") # Setter tittel på vinduet

    show_menu(screen, 1) # Viser menyen med forrige poengsum lik 1
