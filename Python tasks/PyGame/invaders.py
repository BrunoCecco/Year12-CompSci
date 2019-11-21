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
        if self.bullet_count > 0:
            self.bullet_count -= 1


## -- Define the class invaders which is a sprite
class Invader(pygame.sprite.Sprite):
    # Define the constructor for invaders
    def __init__(self, width, height, speed, filename):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        #self.image = pygame.Surface([width,height])
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(-100, 0)
        # Set the position of the sprite
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
        self.width = width
        self.height = height
        self.speed = 1

    def update(self):
        self.rect.y = self.rect.y - self.speed
        if self.rect.y < 0:
            bullet_group.remove(self)

class Barrier(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.speed = 0


def new_invader_group(invader, num_invaders, sprite_group, invader_group, invader_image):
    for x in range (num_invaders):
        invader = Invader(20, 20, 1, invader_image)      
        invader_group.add(invader)
        sprite_group.add(invader)
    #Next x

    
all_sprites_group = pygame.sprite.Group()
invader_group = pygame.sprite.Group()
#invader_group_2 = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
barrier_group = pygame.sprite.Group()


# create barriers
num_barriers = 7
x = 0
for b in range(num_barriers):
    barrier = Barrier(BLUE, 40, 40, x, 300)
    barrier_group.add(barrier)
    all_sprites_group.add(barrier)
    x += 100

# create player 
player = Player(YELLOW, 10, 10)
all_sprites_group.add(player)

# Create the invaders
invader = Invader(20, 20, 1, 'invader_img.png') 
new_invader_group(invader, 10, all_sprites_group, invader_group, 'invader_img.png')

clock = pygame.time.Clock()
last_keydown = 0

while not done and player.lives > 0:
#-user input and controls            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN: # - a key is down
            curr_time = pygame.time.get_ticks()
            if event.key == pygame.K_LEFT: # - if the left key pressed                
                player.player_set_speed(-3) # speed set to -3
            if event.key == pygame.K_RIGHT: # - if the right key pressed
                player.player_set_speed(3) # speed set to 3
            if event.key == pygame.K_UP and player.bullet_count > 0:
                    bullet = Bullet(RED, 5, 5)
                    all_sprites_group.add(bullet)
                    bullet_group.add(bullet)
                    player.decrease_bullets()
                    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.player_set_speed(0) # speed set to 0

    # collisions between player and invaders
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
    for p in player_hit_group:
        player.lives -= 1
        
    if len(bullet_group) > 0:
        # collisions between barriers and bullets
        barrier_hit_group = pygame.sprite.groupcollide(barrier_group, bullet_group, False, True)
        
    for b in bullet_group:
        # collisions between invaders and bullets
        invader_hit_group = pygame.sprite.spritecollide(b, invader_group, True)
        if len(invader_group) == 0:
            new_invader_group(invader, 10, all_sprites_group, invader_group, 'invader_img_2.png')
        #decrease score if there's a collision
        for b in invader_hit_group:
            player.increase_score(5)

    # -- Game logic goes in here
    all_sprites_group.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)
    # -- Drawing code goes here
    all_sprites_group.draw(screen)
    
    #invader_hit_group_2 = pygame.sprite.spritecollide(barrier, bullet_group, True)
    print_text(20, 20, screen, "Lives: %d" % player.lives)
    print_text(20, 50, screen, "Score: %d" % player.score)
    print_text(20, 80, screen, "Bullets: %d" % player.bullet_count)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)


#End While - End of game loop
pygame.quit()
