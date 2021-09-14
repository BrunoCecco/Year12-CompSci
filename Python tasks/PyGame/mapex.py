import pygame
import math
import random

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 200, 200)


size = (200, 200)
screen = pygame.display.set_mode(size) # create screen 
pygame.display.set_caption("Project game")
screen.fill(BLACK)

block_w = 10
xpos = 0
ypos = 0
# generate 2D array (map)
smap = []
new_row = []

for i in range (0, int(size[1]/block_w)):
    for j in range (0, int(size[0]/block_w)):
        new_row.append(random.randint(0, 1))
    smap.append(new_row)
    new_row = []
print(smap)
    
for y in range(0, int(size[1]/10)):    
    for x in range(0, int(size[0]/10)):
        if smap[x][y] == 1:
            pygame.draw.rect(screen, BLUE, ((x*20,y*20), (block_w,block_w)))
        else:
            pygame.draw.rect(screen, BLACK, ((x*20,y*20), (block_w,block_w)))




pygame.display.flip()
