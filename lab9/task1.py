#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("lab9/AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab9/Enemy.png")
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
        self.image = pygame.image.load("lab9/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
#INC_SPEED = pygame.USEREVENT + 1
#pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop

# Add parameters of coin
coin_type = 0 # Coin type 0 is regular coin with 1 point, while coin type 1 is a green coin with value 10
coin_value = [1,10]
coin_x = random.randrange(20, SCREEN_WIDTH-20)  # Make coin spawn random on x-axis
coin_y = SCREEN_HEIGHT-60 # Make coin spawn constant on y-axis
coin_surface = pygame.Surface((40,40)) # The size of coin
coin_surface.fill((230, 219, 14)) # The color of coin
coin_rect = coin_surface.get_rect(center=(coin_x, coin_y)) # The Rect object of coin

coin = 0 # The number of coins that we got
coin_state = True # Check for coin appearance of screen()

while True:
    
    #Cycles through all events occuring  
    for event in pygame.event.get():
        SPEED=coin//10+3 # Increasing speed depend on coin
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coins = font_small.render("Coins: " + str(coin), True, BLACK) # Rendering the text that shows us the number of coins that we got
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coins, (285,10)) # Add on the screen the number of coins

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('lab8/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()
    

    
    if not coin_state: # Check if coin is already has taken and change its position to new one
        coin_type = random.randrange(0,2)
        if coin_type:
            coin_surface.fill((80, 255, 0)) # The color of coin
        else:
            coin_surface.fill((230, 219, 14)) # The color of coin
        coin_x = random.randrange(20, SCREEN_WIDTH-20)
        coin_rect = coin_surface.get_rect(center=(coin_x, coin_y))
        coin_state = True

    if P1.rect.colliderect(coin_rect): # Check for collision of player and coin
        coin+=coin_value[coin_type]
        coin_state = False



    DISPLAYSURF.blit(coin_surface, coin_rect)
        
    pygame.display.update()
    FramePerSec.tick(FPS)