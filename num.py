import pygame
from sys import exit
pygame.init()

height = 1024
width  = 640
screen = pygame.display.set_mode((height,width))
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
text = test_font.render('8 700 155 55 55', False, (255,255,255))
text = pygame.transform.rotozoom(text,0,3)

text_r = text.get_rect(center = (height/2,width/2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(text,text_r)
    pygame.display.update()

