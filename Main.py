import neat
import Game
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
SCORE = 0
GENERATION = 0
MAX_FITNESS = 0
BEST_GENOME = 0


def eval_genomes(genomes, config):
     # Play game and get results
     idx, genomes = zip(*genomes) # What does this do?

     genoinf,scoreinf = Game.game(genomes,config,SCORE) #game Returns fitness


     # Calculate fitness and top score
     top_score = 0

     for i, genomes in enumerate(genoinf):

         score = scoreinf[i]
         fitness = score
         genomes.fitness = -1 if fitness == 0 else fitness
         if top_score < score:
             top_score = score

     # print score
     print('The top score was:', top_score)
     fitness_vals.append(fitness)




#Start of actualy program:

fitness_vals = []


config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         'config-feedforward')
pop = neat.Population(config)
pop.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
pop.add_reporter(stats)

winner = pop.run(eval_genomes, 100)

x = np.linspace(0,len(fitness_vals),len(fitness_vals))
sns.lineplot(x=x,y=fitness_vals)
plt.show()

print(stats)


