import pygame

# Definerer farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Oppsett for skjermen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Tekstklassen for menyelementer
class MenuItem(pygame.sprite.Sprite):
    def __init__(self, text, font, position):
        super().__init__()
        self.text = text
        self.font = font
        self.image = self.font.render(self.text, True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

## Funksjon for å vise menyen
def show_menu(screen, previous_score):
    # Initialiserer menyelementer
    menu_font = pygame.font.Font(None, 36)
    title_text = "Flappy Bird"
    previous_score_text = "Forrige poengsum: " + str(previous_score)
    start_item = MenuItem("Start Spill", menu_font, (SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 - 50))
    score_item = MenuItem(previous_score_text, menu_font, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2))
    quit_item = MenuItem("Avslutt", menu_font, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50))
    all_sprites = pygame.sprite.Group(start_item, score_item, quit_item)

    # Spillhovedløkke for menyen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_item.rect.collidepoint(pygame.mouse.get_pos()):
                    return 0 # Starter spillet på nytt, så forrige poengsum blir null
                elif quit_item.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    quit()

        # Oppdaterer teksten for forrige poengsum
        previous_score_text = "Forrige poengsum: " + str(previous_score)
        score_item = MenuItem(previous_score_text, menu_font, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2))
        all_sprites = pygame.sprite.Group(start_item, score_item, quit_item)  # Oppdater gruppen med den nye teksten

        # Oppdaterer og tegner menyen
        screen.fill(WHITE)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

# Testkjøring av menyen
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird - Meny")

    show_menu(screen, 1)
