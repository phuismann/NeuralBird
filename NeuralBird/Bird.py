import sys, pygame, neat


class bird:
    height = 600
    width = 400
    gravity = 1
    lift = -30
    yStart = 250





    def __init__(self,screen,genome,config):
        self.x = 100
        self.y = self.yStart
        self.velocity = 0
        self.screen = screen
        self.genome = genome
        self.neural_network = neat.nn.FeedForwardNetwork.create(genome, config)
        self.dead = False;
        self.distance = 0
        self.distance_obst = 0
        self.input = [0, 0, 0, 0,0,0]#self.input
        self.score = 0

    def show(self):
        if self.dead == False:
            pygame.draw.circle(self.screen,(255,255,255),[self.x, self.y],15)
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
        self.score-= 1 #lot of jumping no good


    def hits(self,pipes):
        for pipe in pipes:
            if self.y < pipe.top or self.y > pipe.height - pipe.bottom or self.y >= self.height or self.y <= 0:
                if self.x > pipe.x and self.x < pipe.x + pipe.w or self.y >= self.height:
                    return True


    def think(self,pipes):
        min_dist = 1000000
        closest_pipe = pipes[0]
        pipeClose = lambda piipe:  piipe.x -self.x
        for pipe in pipes:

            if pipeClose(pipe) <= min_dist and pipeClose(pipe) > 0:
                min_dist = pipeClose(pipe)
                closest_pipe = pipe
                self.distance_obst = min_dist




        self.input[0] = self.velocity/20
        self.input[1] = closest_pipe.x/self.width
        self.input[2] = closest_pipe.top/self.height
        self.input[3] = closest_pipe.bottom/self.height
        self.input[4] = closest_pipe.mid_distance/self.width
        self.input[5] = self.distance_obst/100 #Distance to closest pipe


    def decide(self):
        output = self.neural_network.activate(self.input)
        if output[0] > 0.5:
            self.up()





