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
padd_width = 60
padd_length = 15
x_padd = 0
y_padd = 20
x_padd_2 = (size[0]-padd_length)
y_padd_2 = 20
clock = pygame.time.Clock()

while not done:

    x_val = x_val + x_direction
    y_val = y_val + y_direction
    
    if x_val <= 0:
        x_val = 150
        y_val = 200
        x_direction = 1
        y_direction = 1
        x_padd = 0
        y_padd = 20
        x_padd_2 = (size[0]-padd_length)
        y_padd_2 = 20
        x_direction = x_direction * -1 #if ball doesn't hit the left paddle
        
    if x_val >= size[0]:
        x_val = 150
        y_val = 200
        x_direction = 1
        y_direction = 1
        x_padd = 0
        y_padd = 20
        x_padd_2 = (size[0]-padd_length)
        y_padd_2 = 20
        x_direction = x_direction * -1 #if ball doesn't hit the right paddle
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y_padd = y_padd - 5
        if y_padd <= 0 - padd_width:
            y_padd = size[1]+padd_width   
    elif keys[pygame.K_DOWN]:
        y_padd = y_padd + 5
        if y_padd >= (size[1]+padd_width):
            y_padd = (0 - padd_width)
    if keys[pygame.K_w]:
        y_padd_2 = y_padd_2 - 5
        if y_padd_2 <= 0 - padd_width:
            y_padd_2 = size[1]+padd_width   
    elif keys[pygame.K_s]:
        y_padd_2 = y_padd_2 + 5
        if y_padd_2 >= (size[1]+padd_width):
            y_padd_2 = (0 - padd_width)
    
    #holds button paddle moves
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    if y_val >= (size[1]- ball_width) or y_val <= 0:
        y_direction = y_direction * -1
    #floor and ceiling
    if (y_val < y_padd + padd_width and y_val > y_padd) and x_val <= ball_width:
        x_direction = x_direction * -1.2
    #endif
    #left hand side paddle
    if (y_val < y_padd_2 + padd_width and y_val > y_padd_2) and x_val >= size[0]-(ball_width+padd_length):
        x_direction = x_direction * -1
    #endif  
    #right hand side paddle

#Next event
            
    screen.fill (BLACK)
    
    pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width))
    pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_length, padd_width))
    pygame.draw.rect(screen, WHITE, (x_padd_2, y_padd_2, padd_length, padd_width))
# -- flip display to reveal new position of objects
    pygame.display.flip()
 # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()

