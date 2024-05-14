import pygame # Importerer pygame-biblioteket
import random # Importerer random for tilfeldig tallgenerering
from meny import show_menu ## Importerer show_menu-funksjonen fra meny
# show_menu-funksjonen viser hovedmenyen i spillet
from bird import Bird # Importerer Bird-klassen fra bird
from pipe import Pipe # Importerer Pipe-klassen fra pipe
from scoreboard import Scoreboard # Importerer Scoreboard-klassen fra scoreboard

# Spillet inneholder funksjoner for å vise en meny, styre spillerbevegelse, generere rør, 
# håndtere kollisjoner, og oppdatere og vise poengtavlen.
# Spilleren styrer en fugl gjennom hindringer av rør. 
# Målet er å unngå kollisjoner med rørene samtidig som man prøver å passere gjennom dem 
# for å øke poengsummen og nå neste nivå.

# Definerer farger
LIGHT_BLUE = (0, 191, 255)  # Definerer en lys blå farge
BLACK = (0, 0, 0) # Definerer en svart farge
YELLOW = (255, 255, 0) # Definerer en gul farge

# Definerer farger for hvert nivå
LEVEL_COLORS = [(0, 0, 0), (0, 255, 0), (0, 0, 255)] # Lager en liste med farger for hvert nivå: Svart, grønn, blå

# Oppsett for skjermen
SCREEN_WIDTH = 400 # Setter bredden på spillvinduet til 400 piksler
SCREEN_HEIGHT = 600 # Setter høyden på spillvinduet til 600 piksler

# Variabler for røravstand og mellomrom
PIPE_GAP = 250 # Setter avstanden mellom rørene til 250 piksler
PIPE_SPACING = 200 # Setter mellomrommet mellom rørene til 200 piksler
LAST_PIPE_X = SCREEN_WIDTH # Setter x-posisjonen til det siste røret til bredden på skjermen

# Initialiserer Pygame
pygame.init() ## Starter Pygame-biblioteket
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Oppretter spillvinduet med gitt bredde og høyde
pygame.display.set_caption("Flappy Bird") # Setter tittel på spillvinduet til "Flappy Bird"
clock = pygame.time.Clock() # Oppretter en klokke for å kontrollere oppdateringshastigheten

# Forrige poengsum
previous_score = 0 # Setter forrige poengsum til 0

level = 1 # Setter startnivået til 1

# Viser menyen og henter forrige poengsum
previous_score = show_menu(screen, previous_score)  ## Viser menyen og lagrer forrige poengsum

# Lager spilleren, rørene og poengtavlen
bird = Bird(SCREEN_WIDTH, SCREEN_HEIGHT)  # Oppretter en fugl-instans
pipes = pygame.sprite.Group() # Oppretter en gruppe for rørene #lar deg legge til, fjerne og manipulere flere sprite-objekter samtidig. Dette gjør det enkelt å oppdatere og tegne flere sprites på skjermen samtidig
scoreboard = Scoreboard() # Oppretter en poengtavle-instans
# Spillhovedløkke
running = True ## Setter en variabel for å styre spillets hovedløkke
while running: # Starter hovedløkken
    for event in pygame.event.get(): # Løkke for å håndtere hendelser
        if event.type == pygame.QUIT: # Hvis brukeren lukker vinduet
            running = False # Avslutter hovedløkken

    # Oppdaterer spilleren, rørene og poengtavlen
    bird.update() # Oppdaterer spillerens posisjon og tilstand
    pipes.update() # Oppdaterer rørene
    scoreboard.update() # Oppdaterer poengtavlen

    # Genererer nye rør
    if len(pipes) < 5: # Hvis antall rør er mindre enn 5
        pipe_gap_top = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50) # Genererer en tilfeldig avstand for topprøret
        pipe_height_bottom = SCREEN_HEIGHT - pipe_gap_top - PIPE_GAP # Beregner høyden på bunnrøret
        pipe_top = Pipe(LAST_PIPE_X + PIPE_SPACING, 0, pipe_gap_top, LEVEL_COLORS[level - 1]) # Oppretter et topprør-objekt
        pipe_bottom = Pipe(LAST_PIPE_X + PIPE_SPACING, SCREEN_HEIGHT, pipe_height_bottom, LEVEL_COLORS[level - 1], True) # Oppretter et bunnrør-objekt
        pipes.add(pipe_top) # Legger til topprøret i rørgruppen
        pipes.add(pipe_bottom) # Legger til bunnrøret i rørgruppen
        LAST_PIPE_X = pipe_top.rect.right # Oppdaterer x-posisjonen til det siste røret

    # Sjekker for kollisjoner mellom spilleren og rørene
    if pygame.sprite.spritecollide(bird, pipes, False): # Hvis det er en kollisjon mellom spilleren og et rør
        # Returnerer til menyen når spilleren dør
        previous_score = show_menu(screen, scoreboard.score) # Viser menyen og lagrer forrige poengsum
        # Resetter spillet
        bird.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2) # Tilbakestiller spilleren til startposisjonen
        pipes.empty() # Tømmer rørgruppen
        scoreboard.score = 0  # Nullstiller poengtavlen

    # Fjerner rør som har forlatt skjermen
    for pipe in pipes: # For hvert rør i rørgruppen
        if pipe.rect.right < 0: # Hvis røret er utenfor venstre kant av skjermen
            pipe.kill() # Fjerner røret fra rørgruppen

    # Sjekker om spilleren passerer gjennom rørene for å øke poengtellingen
    for pipe in pipes: # For hvert rør i rørgruppen
        if pipe.rect.right == bird.rect.left and pipe != scoreboard.last_scored_pipe: # Hvis spilleren passerer gjennom røret og det ikke er samme rør som sist scoret poeng
            scoreboard.score += 1 # Øker poengtellingen med 1
            scoreboard.last_scored_pipe = pipe # Lagrer røret som sist scoret poeng
            # Sjekker om spilleren har nådd poengsummen for neste nivå
            if scoreboard.score == 10 and level < 3: # Hvis poengsummen er 10 og nivået er mindre enn 3
                level += 1 # Øker nivået med 1
            # Oppdaterer fargen til rørene basert på det nye nivået
            for p in pipes: # For hvert rør i rørgruppen
                p.update_color(LEVEL_COLORS[level - 1]) # Oppdaterer fargen til rørene basert på det nye nivået
            break  # Avslutter løkken etter å ha funnet én passasje

    # Tegner alt på skjermen
    screen.fill(LIGHT_BLUE) # Fyller skjermen med lys blå farge
    pipes.draw(screen) # Tegner rørene på skjermen
    screen.blit(bird.image, bird.rect) # Tegner spilleren på skjermen
    screen.blit(scoreboard.rendered_score, scoreboard.rect) # Tegner poengtavlen på skjermen
    pygame.display.flip() # Oppdaterer skjermen

    # Viser nåværende nivå i høyre hjørne
    level_text = "Nivå: " + str(level) # Lager en tekststreng som viser gjeldende nivå
    level_font = pygame.font.Font(None, 24) # Velger en font for teksten
    level_rendered = level_font.render(level_text, True, BLACK) # Lager teksten som et bilde med svart farge
    screen.blit(level_rendered, (SCREEN_WIDTH - 100, 10)) # Tegner teksten på skjermen i høyre hjørne
    pygame.display.flip() # Oppdaterer skjermen
    # "blit" til å tegne en overflate på en annen overflate eller skjerm.
    # "render" betyr å konvertere tekst eller grafikk til et visuelt format som kan vises på skjermen.

    # Setter FPS
    clock.tick(30) # Begrenser oppdateringshastigheten til 30 FPS

pygame.quit() # Avslutter Pygame-biblioteket når hovedløkken er ferdig

# parameter representerer en verdi som kan gis til en funksjon
# variabel er et navn som er tilordnet en bestemt verdi i et program.