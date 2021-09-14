import pygame
import math
import random
import turtle

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
RED = (245, 50, 17)
pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Crossy road")
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
        self.rect.y = 300
        self.rect.topleft = self.rect.x, self.rect.y
        self.width = width
        self.height = height
        self.speed = 0
        self.score = 0 # ordinary attribute
        self.lives = 5

    def increase_score(self, val):
        self.score += val
        
    def player_move(self, val):
        self.rect.x += val


## -- Define the class invaders which is a sprite
class Road(pygame.sprite.Sprite):
    # Define the constructor for invaders
    def __init__(self, color, width, height, x, y):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Set the position of the sprite
        self.width = width
        self.height = height
        
    def road_move(self, val):
        self.rect.y = self.rect.y + val
        if self.rect.y >= size[1]:
            self.rect.y = 0
        

class Cars(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 600)
        self.width = width
        self.height = height
        self.l = [-1, 1]
        self.randomw = (random.choice(self.l))

    def car_move(self, val):
        self.rect.y = self.rect.y + val
        if self.rect.y >= size[1]:
            self.rect.y = 0
        if self.rect.x >= size[0] or self.rect.x <= 0:
            self.rect.x = random.randrange(0, 640)
        
    def update(self):
        self.rect.x = self.rect.x - 1*self.randomw


all_sprites_group = pygame.sprite.Group()
road_group = pygame.sprite.Group()
car_group = pygame.sprite.Group()

# create player 
player = Player(RED, 30, 30)
all_sprites_group.add(player)

#create cars
for c in range (20):
    car = Cars(BLUE, 30, 30)      
    car_group.add(car)
    all_sprites_group.add(car)


#create roads
y = 100
for r in range (10):
    road = Road(YELLOW, 640, 20, 0, y)      
    road_group.add(road)
    all_sprites_group.add(road)
    y += random.randrange(75, 125)


clock = pygame.time.Clock()

while not done and player.lives > 0:
#-user input and controls

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_LEFT: # - if the left key pressed                
                player.player_move(-40) # speed set to -3
            if key == pygame.K_RIGHT: # - if the right key pressed
                player.player_move(40) # speed set to 3
            if key == pygame.K_UP:
                player.increase_score(1)
                for r in road_group:
                    r.road_move(40)
                for c in car_group:
                    c.car_move(40)
            if key == pygame.K_DOWN:
                for r in road_group:
                    r.road_move(-40)
                for c in car_group:
                    c.car_move(-40)
        

    # check for collisions 
    collide_group = pygame.sprite.spritecollide(player, car_group, True)
    
    # -- Game logic goes in here
    all_sprites_group.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)
    # -- Drawing code goes here
    all_sprites_group.draw(screen)
    
    #invader_hit_group_2 = pygame.sprite.spritecollide(barrier, bullet_group, True)
    print_text(20, 20, screen, "Lives: %d" % player.lives)
    print_text(20, 50, screen, "Score: %d" % player.score)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)


#End While - End of game loop
pygame.quit()
