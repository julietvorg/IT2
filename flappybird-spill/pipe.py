import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, height, color, inverted=False):
        super().__init__()
        self.image = pygame.Surface((50, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.color = color
        self.update_color(color)  # Setter fargen
        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y)
        else:
            self.rect.topleft = (x, y)

    def update(self):
        self.rect.x -= 5

    def update_color(self, color):
        self.color = color
        self.image.fill(self.color)
