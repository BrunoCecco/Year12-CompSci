import pygame
import math
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
ORANGE = (245, 154, 17)
pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")
done = False


class Player(pygame.sprite.Sprite):
    # Define the constructor for invaders
    def __init__(self, color, width, height):
        
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = size[1]-height
        self.speed = 0
     #End Procedure
    
    def player_set_speed(self, val):
        self.speed = val
        
    def update(self):
        self.rect.x = self.rect.x + self.speed

    bullet_count = 50

## -- Define the class invaders which is a sprite
class Invader(pygame.sprite.Sprite):
    # Define the constructor for invaders
    def __init__(self, color, width, height, speed):
        
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(-50, 0)
     #End Procedure

        self.speed = speed
        
    def update(self):
        self.rect.y = self.rect.y + self.speed


class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, speed, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.speed = 2

    def update(self):
        self.rect.y = self.rect.y - self.speed
 

all_sprites_group = pygame.sprite.Group()
invader_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
#bullet = Bullet(ORANGE, 2, 5, 5)
#bullet_group.add(bullet)
#all_sprites_group.add(bullet)
player = Player(YELLOW, 20, 20)
#bullet = Bullet(ORANGE, 2, 10, 10)

all_sprites_group.add(player)

# Create the snowflakes
number_of_invaders = 10 # we are creating 50 snowflakes
for x in range (number_of_invaders):
    invaders = Invader(BLUE, 20, 20, 1) # snowflakes are white with size 10 by 10
    invader_group.add(invaders) # adds the new snowflake to the group of snowflakes
    all_sprites_group.add(invaders) # adds it to the group of all Sprites
#Next x

clock = pygame.time.Clock()

while not done:
#-user input and controls            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: # - a key is down
            if event.key == pygame.K_LEFT: # - if the left key pressed
                player.player_set_speed(-3) # speed set to -3
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
                player.player_set_speed(3) # speed set to 3
        elif event.type == pygame.KEYUP: # - a key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0) # speed set to 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bullet = Bullet(ORANGE, 2, 5, 5)
                bullet_group.add(bullet)
                all_sprites_group.add(bullet)
                bullet_hit_group = pygame.sprite.spritecollide(bullet, invader_group, True)
        # -- Game logic goes in here
    all_sprites_group.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)
    # -- Drawing code goes here
    all_sprites_group.draw(screen)

# -- flip display to reveal new position of objects
    pygame.display.flip()
 # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()

