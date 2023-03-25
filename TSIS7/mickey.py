import pygame
from sys import exit
import datetime


pygame.init()
screen = pygame.display.set_mode((420,420))
pygame.display.set_caption('Mickey clock')

mickey = pygame.image.load('graphics/main-clock.png').convert_alpha()
mr = pygame.image.load('graphics/right-hand.png').convert_alpha()
ml = pygame.image.load('graphics/left-hand.png').convert_alpha()

mickey = pygame.transform.rotozoom(mickey,0,0.5)
mr = pygame.transform.rotozoom(mr,90,0.5)
ml = pygame.transform.rotozoom(ml,90,0.5)

x = datetime.datetime.now()
min = x.minute
sec = x.second
mr = pygame.transform.rotate(mr,-x.minute*360/60)
ml = pygame.transform.rotate(ml,-sec*360/60)


mr_r = mr.get_rect(center = (210,210))
ml_r = ml.get_rect(center = (210,210))

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer,60000)


clock = pygame.time.Clock()

m = 1
s = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    if event.type == timer:
        mr = pygame.transform.rotate(mr,-m*360/60).convert_alpha()
        

        
    mr_r = mr.get_rect(center = (210,210))
    mln = pygame.transform.rotate(ml,-s*360/60).convert_alpha()

    ml_r = mln.get_rect(center = (210,210))
    
    screen.blit(mickey,(0,0))
    screen.blit(mr,mr_r)
    screen.blit(mln,ml_r)
    
    
    m+=1
    s+=1
    pygame.display.update()
    clock.tick(1)

