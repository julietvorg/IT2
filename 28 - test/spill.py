import pygame
import sys
import json
import os
from spiller import Spiller
from hovedprogram import last_inn_politikere



# Farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)

# Initialiser Pygame
pygame.init()

# Skjermstørrelse
SKJERM_BREDDE = 800
SKJERM_HØYDE = 600
skjerm = pygame.display.set_mode((SKJERM_BREDDE, SKJERM_HØYDE))
pygame.display.set_caption("Stortinget-fantasy")

# Font
font = pygame.font.SysFont(None, 36)

def tegn_tekst(skjerm, tekst, x, y):
    tekstoverflate = font.render(tekst, True, SVART)
    skjerm.blit(tekstoverflate, (x, y))

def vis_alle_politikere(politikere):
    running = True
    while running:
        skjerm.fill(HVIT)
        y = 20
        for politiker in politikere:
            tegn_tekst(skjerm, str(politiker), 20, y)
            y += 40
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False 

def hovedmeny(spiller, politikere):
    running = True
    while running:
        skjerm.fill(HVIT)
        tegn_tekst(skjerm, f"Velkommen, {spiller.navn}!", 20, 20)
        tegn_tekst(skjerm, "1. Se alle politikere", 20, 60)
        tegn_tekst(skjerm, "2. Kjøp en politiker", 20, 100)
        tegn_tekst(skjerm, "3. Selg en politiker", 20, 140)
        tegn_tekst(skjerm, "4. Se portefølje", 20, 180)
        tegn_tekst(skjerm, "5. Avslutt", 20, 220)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    vis_alle_politikere(politikere)
                elif event.key == pygame.K_2:
                    kjøp_politiker(spiller, politikere)
                elif event.key == pygame.K_3:
                    selg_politiker(spiller)
                elif event.key == pygame.K_4:
                    vis_portefølje(spiller)
                elif event.key == pygame.K_5:
                    running = False

def kjøp_politiker(spiller, politikere):
    # Implementer logikk for å kjøpe politiker
    pass

def selg_politiker(spiller):
    # Implementer logikk for å selge politiker
    pass

def vis_portefølje(spiller):
    running = True
    while running:
        skjerm.fill(HVIT)
        tegn_tekst(skjerm, "Din portefølje:", 20, 20)
        y = 60
        for politiker in spiller.portefølje:
            tegn_tekst(skjerm, str(politiker), 20, y)
            y += 40
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_directory, "stortinget.json")
    print("JSON-filbane:", json_file_path)  # Legg til denne linjen
    politikere = last_inn_politikere(json_file_path)
    print("Politikere:", politikere)  # Legg til denne linjen
    if not politikere:
        print("Feil: Kunne ikke laste inn politikere. Avslutter programmet.")
        pygame.quit()
        sys.exit()

    navn = input("Skriv inn navnet ditt: ")
    spiller = Spiller(navn)
    
    hovedmeny(spiller, politikere)

    pygame.quit()
    sys.exit()
