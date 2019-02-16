import sys, pygame, neat
import numpy as np


class bird:
    height = 600
    width = 400
    gravity = 1
    lift = -60
    yStart = 250





    def __init__(self,screen,genome,config):
        self.x = 100
        self.y = self.yStart
        self.velocity = 0
        self.screen = screen
        self.genome = genome
        self.neural_network = neat.nn.FeedForwardNetwork.create(genome, config)
        self.dead = False
        self.distance = 0
        self.distance_obst = 0
        self.input = [0, 0, 0, 0, 0, 0, 0, 0, 0] #self.input
        self.score = 0
        self.distance_treat_x=0
        self.distance_treat_y = 0
        self.food = 0
        self.rnd_color1 = np.random.randint(0, 100)
        self.rnd_color2 = np.random.randint(0, 100)
        self.rnd_color3 = np.random.randint(0, 100)
        self.power = 100

    def show(self):
        if self.dead == False:
            pygame.draw.circle(self.screen,(255-self.rnd_color1 ,255-self.rnd_color2 ,255-self.rnd_color3 ),[self.x, self.y],max(int(15*self.power/100),3))
            #self.screen.blit(pygame.image.load('assets/redbird-downflap.png'),(self.x, self.y))
        else:
            pygame.draw.circle(self.screen, (0, 0, 0), [-100, -100], 15)
    def update(self):
        self.velocity += self.gravity
        self.y += int(self.velocity*0.1)
        if (self.y > int(self.height)):
            self.y = int(self.height)
            self.velocity = 0
        if (self.y < 0):
            self.y = 0
            self.velocity = 0
        self.score += self.distance/1000


    def up(self):
        self.velocity += self.lift
        self.score -= 1
        self.power -= 3


    def hits(self,pipes):
        for pipe in pipes:
            if self.y < pipe.top or self.y > pipe.height - pipe.bottom or self.y >= self.height or self.y <= 0:
                if self.x > pipe.x and self.x < pipe.x + pipe.w or self.y >= self.height:
                    return True


    def think(self,pipes):
        min_dist = 1000000
        closest_pipe = pipes[0]
        pipeClose = lambda piipe:  piipe.x - self.x
        for pipe in pipes:

            if pipeClose(pipe) <= min_dist and pipeClose(pipe) > 0:
                min_dist = pipeClose(pipe)
                closest_pipe = pipe
                self.distance_obst = min_dist




        self.input[0] = self.velocity/20
        self.input[1] = closest_pipe.x/self.width
        self.input[2] = (self.y-closest_pipe.top)/self.height
        self.input[3] = (closest_pipe.bottom-self.y)/self.height
        self.input[4] = closest_pipe.mid_distance/self.width
        self.input[5] = self.distance_obst/100
        self.input[6] = self.distance_treat_y / 100
        self.input[7] = self.distance_treat_x / 100
        self.input[8] = self.power/100

    def decide(self):
        output = self.neural_network.activate(self.input)
        if output[0] > 0.5:
            self.up()


    def eat(self,treat):
        range = 20
        if self.x <= treat.x+range and self.x > treat.x-range and self.y <= treat.y +range and self.y > treat.y-range :
            self.score=+10
            self.food +=1
            self.power += 10


            return True
    def see_treat(self,treats):
        min_dist_y = 1000000
        for treat in treats:
            treatClosey = lambda treeat: treat.y - self.y
            if treatClosey(treat) <= min_dist_y:
                min_dist_y = treatClosey(treat)

                self.distance_treat_y = min_dist_y

        treatClosex = lambda treeat:  treat.x - self.x
        min_dist_x =10000
        for treat in treats:

            if treatClosex(treat) <= min_dist_x and treatClosex(treat) > 0:

                min_dist_x = treatClosex(treat)
                self.distance_treat_x = min_dist_x






