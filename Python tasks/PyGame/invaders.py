import pygame
import math
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
RED = (245, 50, 17)
pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")
done = False
font = pygame.font.Font(None, 30)
            
def print_text(x_pos, y_pos, my_screen, text_string):
    #Draw text onto the screen
    text_map = font.render(str(text_string), True, WHITE)
    my_screen.blit(text_map, [x_pos, y_pos])
    #y_pos += line_height
 
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
        self.rect.topleft = self.rect.x, self.rect.y
        self.width = width
        self.height = height
        self.speed = 0
        self.score = 0 # ordinary attribute
        self.bullet_count = 50
        self.lives = 5

    def increase_score(self, val):
        self.score += val
        
    def player_set_speed(self, val):
        self.speed = val
        
    def update(self):
        self.rect.x = self.rect.x + self.speed
        if self.rect.x >= size[0]:
            self.rect.x = 0
        elif self.rect.x <= 0:
            self.rect.x = 0

    def decrease_bullets(self):
        if self.bullet_count> 0:
            self.bullet_count -= 1


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
        self.rect.y = random.randrange(-100, 0)
        self.rect.topleft = self.rect.x, self.rect.y
        self.width = width
        self.height = height
        self.speed = speed
        
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y >= size[1]:
            self.rect.y = 0
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.rect.topleft = self.rect.x, self.rect.y
        self.width = width
        self.height = height
        self.speed = 1

    def update(self):
        self.rect.y = self.rect.y - self.speed
        if self.rect.y < 0:
            bullet_group.remove(self)


all_sprites_group = pygame.sprite.Group()
invader_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

player = Player(YELLOW, 10, 10)
all_sprites_group.add(player)

# Create the invaders
number_of_invaders = 10
for x in range (number_of_invaders):
    invader = Invader(BLUE, 20, 20, 1) 
    invader_group.add(invader)
    all_sprites_group.add(invader)
#Next x

clock = pygame.time.Clock()
last_keydown = 0

while not done and player.lives > 0:
#-user input and controls            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN: # - a key is down
            curr_time = pygame.time.get_ticks()
            if event.key == pygame.K_LEFT: # - if the left key pressed                
                player.player_set_speed(-3) # speed set to -3
            if event.key == pygame.K_RIGHT: # - if the right key pressed
                player.player_set_speed(3) # speed set to 3

            if curr_time - last_keydown > 100: # limit frequency of shooting
                if event.key == pygame.K_UP:
                    if player.bullet_count > 0:
                        bullet = Bullet(RED, 5, 5)
                        all_sprites_group.add(bullet)
                        bullet_group.add(bullet)
                        player.decrease_bullets()
                        last_keydown = curr_time
                        
        elif event.type == pygame.KEYUP:
            player.player_set_speed(0) # speed set to 0

    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
    for p in player_hit_group:
        player.lives -= 1
        
    for b in bullet_group:         
        invader_hit_group = pygame.sprite.spritecollide(b, invader_group, True)
        for b in invader_hit_group:
            player.increase_score(5)

    if player.lives == 4:
        print_text(250, 150, screen, "Game Over")
    # -- Game logic goes in here
    all_sprites_group.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)
    # -- Drawing code goes here
    all_sprites_group.draw(screen)

    print_text(20, 20, screen, "Lives: %d" % player.lives)
    print_text(20, 50, screen, "Score: %d" % player.score)
    print_text(20, 80, screen, "Bullets: %d" % player.bullet_count)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)


#End While - End of game loop
pygame.quit()
