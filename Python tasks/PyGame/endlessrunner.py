import pygame, sys
import random
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 440))
pygame.display.set_caption('Race')

FPS = 3
fpsClock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (205,201,201)
GREEN = (0,255,127)
RED = (255,0,0)
MAIN_X = 300
MAIN_Y = 300
ROW_COUNT = 0

LIST1 = []
LIST2 = []
LIST3 = []
LIST4 = []

score = 0

ROW_TURN = 1
arial = pygame.font.SysFont('arial', 20, bold=False,italic=False)
def game_over(sco):
        font_obj = pygame.font.Font('freesansbold.ttf', 32)
        text_surf_obj_go = arial.render('GAME OVER', True, BLACK)
        text_surf_obj_sco = font_obj.render('SCORE: ' + str(sco), True, BLACK)
        text_rec_obj_go = text_surf_obj_go.get_rect()
        text_rec_obj_sco = text_surf_obj_sco.get_rect()
        text_rec_obj_go.center = (200,150)
        text_rec_obj_sco.center = (200,190)
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(text_surf_obj_go, text_rec_obj_go)
        DISPLAYSURF.blit(text_surf_obj_sco, text_rec_obj_sco)
        pygame.display.update()

def score_tracker(sco):
        font_obj = pygame.font.Font('freesansbold.ttf',20)
        text_surf_obj = font_obj.render(('SCORE: ' + str(sco)), True, GREY)
        text_rec_obj = text_surf_obj.get_rect()
        text_rec_obj.center = (200,420)
        DISPLAYSURF.blit(text_surf_obj,text_rec_obj)

def play_again():
        font_obj = pygame.font.Font('freesansbold.ttf',20)
        text_surf_obj = font_obj.render('Play Again', True, WHITE, BLACK)
        text_rec_obj = text_surf_obj.get_rect()
        text_rec_obj.center = (200,260)
        DISPLAYSURF.blit(text_surf_obj, text_rec_obj)
        
while True:
        DISPLAYSURF.fill(BLACK)
        SQ_LENGTH = 100
        BG_X = 0
        BG_Y = 0
        break_it = False
        for i in range(16):
                pygame.draw.rect(DISPLAYSURF, GREY, (BG_X,BG_Y,SQ_LENGTH,SQ_LENGTH),5)
                if BG_X == 300:
                        BG_X = 0
                        BG_Y = BG_Y + SQ_LENGTH
                else:
                        BG_X = BG_X + SQ_LENGTH
        ROW_COUNT = ROW_COUNT + 1
        if ROW_COUNT < 10:
                pygame.draw.rect(DISPLAYSURF,GREEN,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH))
                pygame.draw.rect(DISPLAYSURF,GREY,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH),5)
                for event in pygame.event.get():
                        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                                pygame.quit()
                                sys.exit()
                        elif (event.type == KEYDOWN and event.key == K_RIGHT) and MAIN_X < 300:
                                pygame.draw.rect(DISPLAYSURF,BLACK,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH),5)
                                MAIN_X = MAIN_X + 100
                        elif (event.type == KEYDOWN and event.key == K_LEFT) and MAIN_X > 0:
                                pygame.draw.rect(DISPLAYSURF,BLACK,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH),5)
                                MAIN_X = MAIN_X - 100
                        pygame.draw.rect(DISPLAYSURF,GREEN,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH))
                        pygame.draw.rect(DISPLAYSURF,GREY,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH),5)
        else:
                pygame.draw.rect(DISPLAYSURF,GREEN,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH))
                pygame.draw.rect(DISPLAYSURF,GREY,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH),5)
                for event in pygame.event.get():
                        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                                pygame.quit()
                                sys.exit()
                        elif event.type == KEYDOWN and event.key == K_b:
                                sys.exit()
                        elif (event.type == KEYDOWN and event.key == K_RIGHT) and MAIN_X < 300:
                                pygame.draw.rect(DISPLAYSURF,BLACK,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH),5)
                                MAIN_X = MAIN_X + 100
                        elif (event.type == KEYDOWN and event.key == K_LEFT) and MAIN_X > 0:
                                pygame.draw.rect(DISPLAYSURF,BLACK,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH),5)
                                MAIN_X = MAIN_X - 100
                        samp_rect = pygame.Rect(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH)
 
                        pygame.draw.rect(DISPLAYSURF,GREEN,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH))
                        pygame.draw.rect(DISPLAYSURF,GREY,(MAIN_X,MAIN_Y,SQ_LENGTH,SQ_LENGTH),5)
                        if (MAIN_X == 0) and (1 in LIST4):
                                break_it = True
                                break
                        elif (MAIN_X == 100) and (2 in LIST4):
                                break_it = True
                                break
                        elif (MAIN_X == 200) and (3 in LIST4):
                                break_it = True
                                break
                        elif (MAIN_X == 300) and (4 in LIST4):
                                break_it = True
                                break
                
                if break_it == False:
                        BLOCK_LIST = [1,2,3,4]
                        random.shuffle(BLOCK_LIST)
                        BLOCKS = random.randint(0,2)
                        LIST4 = LIST3
                        LIST3 = LIST2
                        LIST2 = LIST1
                        LIST1 = BLOCK_LIST[0:BLOCKS]

                        
                
                for pos in LIST4:
                        if pos == 1:
                                pygame.draw.rect(DISPLAYSURF,RED,(0,300,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(0,300,SQ_LENGTH,SQ_LENGTH),5)
                                if MAIN_X == 0:
                                        break_it = True
                        elif pos == 2:
                                pygame.draw.rect(DISPLAYSURF,RED,(100,300,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(100,300,SQ_LENGTH,SQ_LENGTH),5)
                                if MAIN_X == 100:
                                        break_it = True
                        elif pos == 3:
                                pygame.draw.rect(DISPLAYSURF,RED,(200,300,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(200,300,SQ_LENGTH,SQ_LENGTH),5)
                                if MAIN_X == 200:
                                        break_it = True
                        elif pos == 4:
                                pygame.draw.rect(DISPLAYSURF,RED,(300,300,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(300,300,SQ_LENGTH,SQ_LENGTH),5)
                                if MAIN_X == 300:
                                        break_it = True
                
                for pos in LIST3:
                        if pos == 1:
                                pygame.draw.rect(DISPLAYSURF,RED,(0,200,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(0,200,SQ_LENGTH,SQ_LENGTH),5)
                        elif pos == 2:
                                pygame.draw.rect(DISPLAYSURF,RED,(100,200,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(100,200,SQ_LENGTH,SQ_LENGTH),5)
                        elif pos == 3:
                                pygame.draw.rect(DISPLAYSURF,RED,(200,200,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(200,200,SQ_LENGTH,SQ_LENGTH),5)
                        elif pos == 4:
                                pygame.draw.rect(DISPLAYSURF,RED,(300,200,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(300,200,SQ_LENGTH,SQ_LENGTH),5)
                for pos in LIST2:
                        if pos == 1:
                                pygame.draw.rect(DISPLAYSURF,RED,(0,100,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(0,100,SQ_LENGTH,SQ_LENGTH),5)
                        elif pos == 2:
                                pygame.draw.rect(DISPLAYSURF,RED,(100,100,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(100,100,SQ_LENGTH,SQ_LENGTH),5)
                        elif pos == 3:
                                pygame.draw.rect(DISPLAYSURF,RED,(200,100,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(200,100,SQ_LENGTH,SQ_LENGTH),5)
                        elif pos == 4:
                                pygame.draw.rect(DISPLAYSURF,RED,(300,100,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(300,100,SQ_LENGTH,SQ_LENGTH),5)
                for pos in LIST1:
                        if pos == 1:
                                pygame.draw.rect(DISPLAYSURF,RED,(0,0,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(0,0,SQ_LENGTH,SQ_LENGTH),5)
                                
                        elif pos == 2:
                                pygame.draw.rect(DISPLAYSURF,RED,(100,0,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(100,0,SQ_LENGTH,SQ_LENGTH),5)
                                
                        elif pos == 3:
                                pygame.draw.rect(DISPLAYSURF,RED,(200,0,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(200,0,SQ_LENGTH,SQ_LENGTH),5)
                                
                        elif pos == 4:
                                pygame.draw.rect(DISPLAYSURF,RED,(300,0,SQ_LENGTH,SQ_LENGTH))
                                pygame.draw.rect(DISPLAYSURF,GREY,(300,0,SQ_LENGTH,SQ_LENGTH),5)
        score = score + 10
        score_tracker(score)
                
        if break_it == True:
                pygame.display.update()
                fpsClock.tick(FPS)
                game_over(score)
                font_obj = pygame.font.Font('freesansbold.ttf',20)
                text_surf_obj = font_obj.render('Play Again', True, WHITE)
                
                text_rec_obj = pygame.Rect(130,260,130,50)
                pygame.draw.rect(DISPLAYSURF,BLACK,text_rec_obj)
                DISPLAYSURF.blit(text_surf_obj, (145,275))
                pygame.display.update()
                fpsClock.tick(FPS)
                while True:
                        for event in pygame.event.get():
                                if event.type == KEYDOWN and event.key == K_ESCAPE:
                                        pygame.quit()
                                        sys.exit()
                                elif event.type == MOUSEBUTTONUP:
                                        x,y = event.pos
                                        if(x >= 130 and x <= 260) and (y >= 260 and y <= 310):
                                                print('PLAY AGAIN')
                                
                        
        pygame.display.update()
        fpsClock.tick(FPS)
        
