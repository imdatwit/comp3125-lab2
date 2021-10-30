# import the pygame module, so you can use it
import pygame
from paddle import Paddle
from ball import Ball
from pygame.locals import *
 
FPS = 60
WINX = 800
WINY = 400
VELOCITY = 4
bgColor = pygame.Color("black")
wallColor = pygame.Color("white")
ballColor = pygame.Color("skyblue")
WALL_BORDER = 20

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("pong")
    #add a solid background as r,g,b:
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((WINX, WINY))
    rect1 = Rect(0,0,WINX,WALL_BORDER) # create first wall, top
    rect2 = Rect(0,0,WALL_BORDER,WINY) # create second wall, left
    rect3 = Rect(0,WINY - WALL_BORDER,WINX,WALL_BORDER) # create third wall, bottom

    # init ball
    ballX = WINX - Ball.RADIUS
    ballY = WINY // 2 
    ballVeloX = -VELOCITY
    ballVeloY = 0
    gameBall = Ball(ballX,ballY,ballVeloX,ballVeloY,screen,ballColor,bgColor)
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
    # main loop
    while running:
        # event handling, gets all event from the event queue
            # Ball
            pygame.draw.rect(screen, wallColor, rect1)
            pygame.draw.rect(screen, wallColor, rect2)
            pygame.draw.rect(screen, wallColor, rect3)
            gameBall.update()
            pygame.display.flip()
            clock.tick(FPS)
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False

    gameBall.show(ballColor)
    screen.fill(bgColor)
    pygame.display.flip()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()