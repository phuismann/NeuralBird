import pygame
import Bird
import Pipe
import neat
import numpy as np

def game(genomes, config, score):
    pygame.init()
    pygame.font.init()
    done = False
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



    for genome in genomes:
        birds.append(Bird.bird(screen=screen,genome=genome,config=config))


    ##Neural Net
    pipes.append(Pipe.pipe())
    pipes[0].top =  height / 4
    pipes[0].bottom = height / 2

    while not done:
        timer += 1

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(game_score), False, (255, 255, 255))
        screen.blit(textsurface, (0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if timer % 100 == 0:
            pipes.append(Pipe.pipe())

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



        clock.tick(10000)

        pygame.display.update()
        screen.fill((0, 0, 0))
        game_score +=1

    pygame.quit()

