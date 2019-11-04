import pygame
import time
import random

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
coin_width = 10
x_val = 150
y_val = 200
coin_position = [random.randrange(1, size[0]-ball_width),random.randrange(1, size[1])-ball_width]
x_direction = 2.5
y_direction = 2.5
padd_width = 60
padd_length = 15
x_padd = 0
y_padd = 20
x_padd_2 = (size[0]-padd_length)
y_padd_2 = 20
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
line_height = 15
x_pos = (size[0]/2)
y_pos = 20
score_p1 = 0
score_p2 = 0
hit_sound = pygame.mixer.Sound(r'C:\Users\Bruno\Pictures\Saved Pictures\drip.wav')
pad_miss = pygame.mixer.Sound(r'C:\Users\Bruno\Pictures\Saved Pictures\falling.wav')
x = 0
y = 0
coins = 0

def draw_rect(screen, colour, x, y, length, width):
    pygame.draw.rect(screen, colour, (x, y, length, width))

#TBD - coin collision
def coin_collision(coin_position, score):
    coin_position = [random.randrange(1, (size[0]-ball_width)),random.randrange(1, (size[1])-ball_width)]
    score += 1
    return coin_position, score

def _init_():
    #Constructor
    reset()
    x_pos = (size[0]/2)
    y_pos = 20
    
def paddle_hit(paddle): 
    global x_direction, x_val, y_val
    if (y_val < paddle + padd_width + (ball_width-1) and y_val > paddle - (ball_width-1)) and (x_val <= padd_length or x_val >= size[0] - (ball_width + padd_length)):
        x_direction = x_direction
        hit_sound.play()

def paddle_miss():
    global x_val, y_val, x_direction, y_direction, x_padd, y_padd, x_padd_2, y_padd_2, score_p1, score_p2
    if x_val >= size[0] or x_val <= 0:
        if x_val >= size[0]:
            score_p2 += 1
        else:
            score_p1 += 1
        time.sleep(1)
        x_val = (size[0]/2)
        y_val = (size[1]/2)
        x_direction = 2.5
        y_direction = 2.5
        x_padd = 0
        y_padd = 20
        x_padd_2 = (size[0]-padd_length)
        y_padd_2 = 20
        x_direction = x_direction * -1 #if ball doesn't hit the left paddle
            
def print_text(x_pos, y_pos, my_screen, text_string):
    #Draw text onto the screen
    text_map = font.render(str(text_string), True, YELLOW)
    my_screen.blit(text_map, [x_pos, y_pos])
    y_pos += line_height
 
def reset():
    #Reset text to the top of the screen
    x_pos = (size[0]/2)
    y_pos = 20
    line_height = 15

while not done:                                                                     

    x_val = x_val + x_direction
    y_val = y_val + y_direction

    paddle_hit(y_padd)
    paddle_hit(y_padd_2)
    #checks if ball hits right and left hand side paddles
    paddle_miss()
    #checks if paddle has missed the paddles
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y_padd = y_padd - 5
        if y_padd <= 0:
            y_padd = 0   
    elif keys[pygame.K_s]:
        y_padd = y_padd + 5
        if (y_padd + padd_width) >= (size[1]):
            y_padd = (size[1] - padd_width)
    if keys[pygame.K_UP]:
        y_padd_2 = y_padd_2 - 5
        if y_padd_2 <= 0:
            y_padd_2 = 0     
    elif keys[pygame.K_DOWN]:
        y_padd_2 = y_padd_2 + 5
        if (y_padd_2 + padd_width) >= (size[1]):
            y_padd_2 = (size[1] - padd_width)

        
    #holds button paddle moves
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if coin_position[0] >= x_val and coin_position[0] <= x_val + ball_width and coin_position[1] <= y_val + ball_width and coin_position[1] >= y_val:
        if x_direction > 0:
            coin_position, score_p2 = coin_collision(coin_position, score_p2)
        else:
            coin_position, score_p1 = coin_position(coin_position, score_p1)
    #collision with coin
    if y_val >= (size[1]- ball_width) or y_val <= 0:
        y_direction = y_direction * -1
    #floor and ceiling   
    
    screen.fill (BLACK)

    if score_p1 > 2 or score_p2 > 2:
        if score_p2 > score_p1:   #display winning player
            print_text(45, y_pos, screen, "Left side Wins!")
        else:
            print_text(45, y_pos, screen, "Right side Wins!")
    else:
        print_text((x_pos-50), y_pos, screen, score_p2 ) #display score
        print_text((x_pos+10), y_pos, screen, score_p1 ) #display score
    draw_rect(screen, YELLOW, coin_position[0], coin_position[1], coin_width, coin_width)
    draw_rect(screen, WHITE, x_padd_2, y_padd_2, padd_length, padd_width)
    draw_rect(screen, WHITE, x_padd, y_padd, padd_length, padd_width)
    draw_rect(screen, BLUE, x_val, y_val, ball_width, ball_width)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(100)

pygame.quit()
