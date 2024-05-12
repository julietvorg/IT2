import pygame

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.rendered_score = self.font.render(str(self.score), True, (0, 0, 0))  # Black color
        self.rect = self.rendered_score.get_rect()
        self.rect.topleft = (10, 10)
        self.last_scored_pipe = None

    def update(self):
        self.rendered_score = self.font.render(str(self.score), True, (0, 0, 0))  # Black color
