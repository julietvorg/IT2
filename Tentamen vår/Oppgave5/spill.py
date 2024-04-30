import pygame
from hinder import Hinder
from ball import Ball
from spiller1 import Spiller1
from spiller2 import Spiller2
from hjelpefunksjoner import finn_unik_pos


pygame.init()
BREDDE = 600 
HOYDE = 600  
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
poeng_font = pygame.freetype.SysFont("Arial", 50)
 
# OPPSETT AV SPILL HER:
poeng = 0
spiller1 = Spiller1(BREDDE/2, HOYDE/2)
spiller2 = Spiller1(BREDDE/2, HOYDE/2)
ball = []
hindere = []
for i in range(4):
    x, y = finn_unik_pos(BREDDE, HOYDE, ball, hindere, spiller1, spiller2)
    ball.append(Ball(x, y))


fritid = 0 

while True:
    vindu.fill("black")
    

    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
 
 
    # Input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        spiller1.retning = (0, -1)
    if taster[pygame.K_DOWN]:
        spiller1.retning = (0, 1)
    if taster[pygame.W]:
        spiller2.retning = (0, -1)
    if taster[pygame.S]:
        spiller2.retning = (0, 1)
    
 
    # Oppdater spill:
    spiller1.oppdater_posisjon()
    spiller2.oppdater_posisjon()

    
    for ball in ball:
        if spiller1.rect.colliderect(ball.rect): 
            center_x = ball.rect.centerx 
            center_y = ball.rect.centery 
            hindere.append(Hinder(center_x, center_y)) 
            ball.remove(ball)
            x, y = finn_unik_pos(BREDDE, HOYDE, ball, hindere, spiller1, spiller2)
            ball.append(ball(x, y)) 
            spiller1.fart *= 1.1 
            spiller2.fart *= 1.1
            poeng += 1
            fritid = 120 

    fritid -= 1
    
    if spiller1.rect.left < 0 or spiller1.rect.right > BREDDE or spiller1.rect.top < 0 or spiller1.rect.bottom > HOYDE:
        if spiller2.rect.left < 0 or spiller2.rect.right > BREDDE or spiller2.rect.top < 0 or spiller2.rect.bottom > HOYDE:
            pygame.quit()
        raise SystemExit
    
    
    if fritid < 0:
        for hinder in hindere:
            if spiller1.rect.colliderect(hinder.rect):
                pygame.quit()
                raise SystemExit

    # Tegning:
    spiller1.tegn(vindu)
    spiller2.tegn(vindu)
    for ball in ball:
        ball.tegn(vindu)
    for hinder in hindere:
        hinder.tegn(vindu)

   
    poeng_font.render_to(vindu, (10, 10), f'Poeng: {poeng}', "white")

    pygame.display.flip()
    klokke.tick(60) 