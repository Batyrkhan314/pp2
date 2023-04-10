import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
clock = pygame.time.Clock()


BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
count = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("racer_inf/AnimatedStreet.png")


DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("racer_inf/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("racer_inf/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('racer_inf/coin.png')
        self.imsc = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.imsc.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(100, SCREEN_HEIGHT-80))
   
     
    def upd(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(100, SCREEN_HEIGHT-80))
        while pygame.sprite.collide_rect(P1, C):
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(100, SCREEN_HEIGHT-80))
        return self.rect.center
    

'''class RCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('racer_inf/rcoin.png')
        self.imsc = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.imsc.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(100, SCREEN_HEIGHT-80))

    def upd(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(100, SCREEN_HEIGHT-80))
        while pygame.sprite.collide_rect(P1, C2):
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(100, SCREEN_HEIGHT-80))
        return self.rect.center'''
        


P1 = Player()
E1 = Enemy()
'''C1 = Coin()
C2 = RCoin()'''
C = Coin()


enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)


INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

coins = pygame.sprite.Group()
coins.add(C)

'''coins1 = pygame.sprite.Group()
coins1.add(C1)

coins2 = pygame.sprite.Group()
coins2.add(C2)'''

while True:
      
    for event in pygame.event.get():
        '''if event.type == INC_SPEED:
              SPEED += 0.5'''     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    if count!=0 and count != cnt and count %2 == 0:
        SPEED += 1

    cnt = count

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coinscore = font_small.render("Coins: " + str(count), True, BLACK)
    DISPLAYSURF.blit(coinscore, (300,10))

    ''' k = random.choice([0,0,0,1])
    if k ==0 :
        DISPLAYSURF.blit(C1.imsc, C1.rect)
    else:
        DISPLAYSURF.blit(C2.imsc, C2.rect)'''

    DISPLAYSURF.blit(C.imsc,C.rect)
    
      
    
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('racer_inf/crash.wav').play()
        time.sleep(1)
                   
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
          
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()    

    '''
    if k==0:
        if pygame.sprite.spritecollideany(P1, coins):
            count += 1
            C1.rect.center = C1.upd()
    else:
        if pygame.sprite.spritecollideany(P1, coins2):
            count += 2
            C2.rect.center = C2.upd()'''
    
    
    if pygame.sprite.spritecollideany(P1,coins):
        count += random.choice([1,1,1,2,3])
        C.rect.center = C.upd()

        
    clock.tick(FPS) 
    pygame.display.update()