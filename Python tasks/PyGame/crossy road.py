#crossy road
import pygame
import time
import random

black = (0, 0, 0)
white = (255, 255, 255)
blue = (50, 50, 255)

pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Crossy Road")
done = False
clock = pygame.time.Clock()
player_width = 20
x_player = (size[0]/2)
y_player = size[1] - player_width

class Cars(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([size[0], size[1]])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-100, 0)
        self.rect.y = random.randrange(0, 400)
        self.width = width
        self.length = height
        self.change_x = 5
        self.change_y = 5
        
        def update(self):
            self.rect.x += self.change_x
            self.rect.y += self.change_y
    #End Procedure
        
#End Class

cars_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

number_of_cars = 20
for x in range(number_of_cars):
    car = Cars(white, 10, 10)
    cars_group.add(car)
    all_sprites_group.add(car)
    
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)
    all_sprites_group.update()
    all_sprites_group.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

