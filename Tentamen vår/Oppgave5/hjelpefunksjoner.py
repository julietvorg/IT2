import random

def finn_unik_pos(bredde, hoyde, baller, hindere, spiller1, spiller2):
    
    unik = False
    while not unik:
        unik = True
        x = random.randint(0, bredde)
        y = random.randint(0, hoyde)
        for ball in baller:
            if ball.rect.collidepoint(x, y):
                unik = False
        for hinder in hindere:
            if hinder.rect.collidepoint(x, y):
                unik = False
        if spiller1.rect.collidepoint(x, y):
            unik = False
        if spiller2.rect.collidepoint(x, y):
            unik = False
    return x, y