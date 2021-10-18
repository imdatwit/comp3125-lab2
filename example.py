# import the pygame module, so you can use it
import pygame
from pygame.locals import *
 
WINX = 800
WINY = 400
BLACK = (0,0,0)
WHITE = (255,255,255)
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
    rect1 = Rect(0,0,WINX,WALL_BORDER)
    rect2 = Rect(0,0,WALL_BORDER,WINY)
    rect3 = Rect(0,WINY - WALL_BORDER,WINX,WALL_BORDER)
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, rect1)
        pygame.draw.rect(screen, WHITE, rect2)
        pygame.draw.rect(screen, WHITE, rect3)
        pygame.display.flip()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()