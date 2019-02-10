import sys, pygame
import numpy as np
class pipe:

    size = width, height = 400, 600
    screen = pygame.display.set_mode(size)
    ## direct Pipe Parameters

    #top = 0
    #bottom = 0
    w = 80
    speed = 2

    def __init__(self):
        self.x = self.width  # x position of pipe
        self.top = np.random.randint(100, self.height / 2)
        self.bottom = np.random.randint(100, self.height / 3)
        self.mid_distance = (self.top - self.bottom)*0.5 + self.bottom

    def show(self): #draws two rectangles one top one bot
        pygame.draw.rect(self.screen,(255,255,255), pygame.Rect(self.x, 0, self.w, self.top)) # Top rect
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.x,self.height-self.bottom, self.w, self.bottom)) # Bot rect
    def update(self):
        self.x -= self.speed

    def offscreen(self):
        if self.x < -self.w:
            return True
        else:
            return False