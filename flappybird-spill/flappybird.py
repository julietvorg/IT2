import pygame
import random
from meny import show_menu
from bird import Bird
from pipe import Pipe
from scoreboard import Scoreboard

# Definerer farger
LIGHT_BLUE = (0, 191, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Definerer farger for hvert nivå
LEVEL_COLORS = [(0, 0, 0), (0, 255, 0), (0, 0, 255)]  # Svart, grønn, blå

# Oppsett for skjermen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Variabler for røravstand og mellomrom
PIPE_GAP = 250
PIPE_SPACING = 200
LAST_PIPE_X = SCREEN_WIDTH

# Initialiserer Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Forrige poengsum
previous_score = 0

level = 1

# Viser menyen og henter forrige poengsum
previous_score = show_menu(screen, previous_score)

# Lager spilleren, rørene og poengtavlen
bird = Bird(SCREEN_WIDTH, SCREEN_HEIGHT)
pipes = pygame.sprite.Group()
scoreboard = Scoreboard()

# Spillhovedløkke
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Oppdaterer spilleren, rørene og poengtavlen
    bird.update()
    pipes.update()
    scoreboard.update()

    # Genererer nye rør
    if len(pipes) < 5:
        pipe_gap_top = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50)
        pipe_height_bottom = SCREEN_HEIGHT - pipe_gap_top - PIPE_GAP
        pipe_top = Pipe(LAST_PIPE_X + PIPE_SPACING, 0, pipe_gap_top, LEVEL_COLORS[level - 1])
        pipe_bottom = Pipe(LAST_PIPE_X + PIPE_SPACING, SCREEN_HEIGHT, pipe_height_bottom, LEVEL_COLORS[level - 1], True)
        pipes.add(pipe_top)
        pipes.add(pipe_bottom)
        LAST_PIPE_X = pipe_top.rect.right

    # Sjekker for kollisjoner mellom spilleren og rørene
    if pygame.sprite.spritecollide(bird, pipes, False):
        # Returnerer til menyen når spilleren dør
        previous_score = show_menu(screen, scoreboard.score)
        # Resetter spillet
        bird.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        pipes.empty()
        scoreboard.score = 0

    # Fjerner rør som har forlatt skjermen
    for pipe in pipes:
        if pipe.rect.right < 0:
            pipe.kill()

    # Sjekker om spilleren passerer gjennom rørene for å øke poengtellingen
    for pipe in pipes:
        if pipe.rect.right == bird.rect.left and pipe != scoreboard.last_scored_pipe:
            scoreboard.score += 1
            scoreboard.last_scored_pipe = pipe
            # Sjekker om spilleren har nådd poengsummen for neste nivå
            if scoreboard.score == 10 and level < 3:  # Endre 10 til ønsket poengsum for å gå til neste nivå
                level += 1
            # Oppdaterer fargen til rørene basert på det nye nivået
            for p in pipes:
                p.update_color(LEVEL_COLORS[level - 1])
            break  # Avslutter løkken etter å ha funnet én passasje

    # Tegner alt på skjermen
    screen.fill(LIGHT_BLUE)
    pipes.draw(screen)
    screen.blit(bird.image, bird.rect)
    screen.blit(scoreboard.rendered_score, scoreboard.rect)
    pygame.display.flip()
    # Viser nåværende nivå i høyre hjørne
    level_text = "Nivå: " + str(level)
    level_font = pygame.font.Font(None, 24)
    level_rendered = level_font.render(level_text, True, BLACK)
    screen.blit(level_rendered, (SCREEN_WIDTH - 100, 10))
    pygame.display.flip()

    # Setter FPS
    clock.tick(30)

pygame.quit()
