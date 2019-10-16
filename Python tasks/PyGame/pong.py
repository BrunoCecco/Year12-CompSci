import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
ORANGE = (245, 154, 17)
pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
done = False
ball_width = 20
x_val = 150
y_val = 200
x_direction = 1
y_direction = 1

clock = pygame.time.Clock()

while not done:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill (BLACK)
# -- Draw here
    pygame.draw.rect(screen, BLUE, (x_val,y_val, ball_width, ball_width))
# -- flip display to reveal new position of objects
    pygame.display.flip()
 # - The clock ticks over
    clock.tick(60)
    x_val = x_val + x_direction
    y_val = y_val + y_direction
#End While - End of game loop
pygame.quit()

