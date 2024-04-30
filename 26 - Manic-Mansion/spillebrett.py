import pygame
from spillobjekt import Spillobjekt

class Spillebrett:
    def __init__(self, bredde, hoyde) -> None:
        self.hoyde: int = hoyde
        self.bredde:int = bredde
        self.objekter: list[Spillobjekt] = []

        # Alle "ting" i Pygame må ha en surface og en rect
        self.surface = pygame,Surface((self.bredde, self.hoyde))
        self.rect = self.surface.get_rect()

        # Plasserer spillebrettet i (x, y)
        self.rect.topleft = (0, 0)
        

    def legg_til_objekt(self, nytt_objekt: Spillobjekt):
        self.objekter.append(nytt_objekt)  #append = legger til

    def fjern_objekt(self, objekt: Spillobjekt):
        self.objekter.remove(objekt)

    def tegn(self, vindu: pygame.Surface):
        vindu.blit()
