import pygame

class Ball:
    # class var
    RADIUS = 15

    def __init__(self, x, y, vx, vy, screen, ballColor,bgColor):
        # instance var
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = ballColor
        self.bgColor = bgColor
        self.screen = screen

    def show(self, color):
        pygame.draw.circle(self.screen,color,(self.x,self.y),self.RADIUS)

    def update(self):
        self.show(self.bgColor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.color)
        pass