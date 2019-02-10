import pygame
import Bird
import Pipe
import Treat
import neat
import numpy as np

def game(genomes, config, score):
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    size = width, height = 400, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Birdy")
    dead_count = 0
    pipes = []
    birds = []
    genome_info=[]
    score_info = []
    timer = 0
    done = False
    game_score = 0
    eaten_treats= 0


    for genome in genomes:
        birds.append(Bird.bird(screen=screen,genome=genome,config=config))


    ##Neural Net
    pipes.append(Pipe.pipe())
    pipes[0].top =  height / 4
    pipes[0].bottom = height / 2


    treat = Treat.treat()
    treats=[]


    while not done:
        timer += 1

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render("Score: "+str(game_score), False, (255, 255, 255))
        screen.blit(textsurface, (0, 0))
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render("Treats: "+str(eaten_treats), False, (255, 255, 255))
        screen.blit(textsurface, (0, 550))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if timer % 150 == 0:
            pipes.append(Pipe.pipe())
            if np.random.randint(1,10)>5:
                treats.append(Treat.treat())

        for treat in treats:
            treat.show()
            treat.update()



        for pipe in pipes:
            pipe.show()
            pipe.update()
            if pipe.offscreen() and len(pipes) > 10:
                pipes.remove(pipe)





        for index, bird in enumerate(birds):

            score = bird.score
            bird.update()
            bird.show()
            bird.think(pipes)
            bird.decide()
            bird.see_treat(treats)

            for treat in treats:
                eaten = bird.eat(treat)
                if treat.x < 0 or eaten:
                    treats.remove(treat)
                if eaten:
                    eaten_treats +=1
            bird.distance = game_score
            if bird.hits(pipes) == True:
                bird.dead = True
                if bird.dead == True:
                    genome_info.append(bird.genome)
                    score_info.append(score)
                    birds.remove(bird)
                dead_count +=1


            if dead_count == len(genomes):
                return genome_info, score_info



        clock.tick(1000)

        pygame.display.update()
        screen.fill((0, 0, 0))
        game_score +=1

    pygame.quit()

