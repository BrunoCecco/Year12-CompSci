import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
ORANGE = (245, 154, 17)
pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Window")
done = False
sun_x = 40
sun_y = 100
clock = pygame.time.Clock()

while not done:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill (BLACK)
# -- Draw here
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (sun_x,sun_y),40,0)

# -- flip display to reveal new position of objects
    pygame.display.flip()
 # - The clock ticks over
    clock.tick(60)
    sun_x += 5
#End While - End of game loop
pygame.quit()

