import pygame


my_map = [[1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]]
'''

my_map = [[1,1,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1]]        
'''


# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640, 480)
screen = pygame.display.set_mode(size)

# -- Title of window
pygame.display.set_caption("Maps")

# -- Manages how fast the screen refreshes
clock = pygame.time.Clock()

# Set game loop to false so it runs
done = False

## -- Colours

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

## -- Define the class tile which is a sprite
class Tile(pygame.sprite.Sprite):
    # Define the constructor for the tile
    def __init__(self, color, width, height, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #end procedure
#end class

## -- Define the class for the player
class Player(pygame.sprite.Sprite):
    # Define the constructor for the player
    def __init__(self, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create the sprite
        width = 10
        height = 10
        color = RED
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #end procedure

    # Class methods
    def player_update_speed(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.y += y_val
    #end procedure
#end class

class Enemy(pygame.sprite.Sprite):
    # Define the constructor for the player
    def __init__(self, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create the sprite
        width = 10
        height = 10
        color = YELLOW
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #end procedure

    def enemy_update_speed(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.y += y_val



# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()

# Create a list of tiles for the walls
wall_group = pygame.sprite.Group()

# create enemy
enemy = Enemy(150, 100)
all_sprites_group.add(enemy)

# Create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(20):
    for x in range(10):
        if my_map[y][x] == 1:
            my_wall = Tile(BLUE, 20,20, x*20, y*20)
            wall_group.add(my_wall)
            all_sprites_group.add(my_wall)
        #end if
    #next x
#next y

#create enemy
pacman = Player(40, 40)
all_sprites_group.add(pacman)

# Game loop
while not(done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # -- Check for collisions between pacman and wall tiles
    player_hit_list = pygame.sprite.spritecollide(pacman, wall_group, False)
    for p in player_hit_list:
        pacman.player_update_speed(0, 0)
        pacman.rect.x = pacman_old_x
        pacman.rect.y = pacman_old_y
        #Run the update function for all sprites
    pacman_old_x = pacman.rect.x
    pacman_old_y = pacman.rect.y
    #next p
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman.player_update_speed(-2, 0)
    elif keys[pygame.K_RIGHT]:
        pacman.player_update_speed(2, 0)
    elif keys[pygame.K_UP]:
        pacman.player_update_speed(0, -2)
    elif keys[pygame.K_DOWN]:
        pacman.player_update_speed(0, 2)
    #end if

    enemy_hit_list = pygame.sprite.spritecollide(enemy, wall_group, False)
    for e in enemy_hit_list:
        enemy.enemy_update_speed(0, 0)
        enemy.rect.x = enemy_old_x
        enemy.rect.y = enemy_old_y
        #Run the update function for all sprites
    enemy_old_x = enemy.rect.x
    enemy_old_y = enemy.rect.y


    if enemy.rect.x != pacman.rect.x or enemy.rect.y != pacman.rect.y:
        if enemy.rect.x < pacman.rect.x:
            enemy.enemy_update_speed(1, 0)
        elif enemy.rect.x > pacman.rect.x:
            enemy.enemy_update_speed(-1, 0)
        if enemy.rect.y < pacman.rect.y:
            enemy.enemy_update_speed(0, 1)
        elif enemy.rect.y > pacman.rect.y:
            enemy.enemy_update_speed(0, -1)


    player_enemy_collision = pygame.sprite.collide_rect(enemy, pacman)

    if player_enemy_collision:
        all_sprites_group.remove(pacman)

        
    all_sprites_group.update()
    screen.fill(BLACK)
    all_sprites_group.draw(screen)

    # Limit to 60 FPS
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()
#End While
pygame.quit()

