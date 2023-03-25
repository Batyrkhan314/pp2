import pygame
pygame.init()
Width, Height = 500,500
x,y = 50,50
screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((255, 255, 255))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and x <= 455:
        x += 20
    if pressed[pygame.K_LEFT] and x >= 45:
        x -= 20
    if pressed[pygame.K_UP] and y >= 45:
        y -= 20
    if pressed[pygame.K_DOWN] and y <= 455:
        y += 20
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    clock.tick(60)
    pygame.display.flip()