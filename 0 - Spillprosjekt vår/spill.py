import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 700 

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#define game variables
ground_scroll = 0
scroll_speed = 4


#load images
bg = pygame.image.load('img:bg.png')
bg = pygame.transform.scale(bg, (screen_width, screen_height))
ground_img = pygame.image.load('img:ground.png')


run = True
while run: 

    clock.tick(fps)

    #draw background
    screen.blit(bg, (0,-150))

    #draw and scroll the ground
    screen.blit(ground_img, (-60, 450)) 
    ground_scroll -= scroll_speed


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()