import neat
import Game
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
SCORE = 0
GENERATION = 0
MAX_FITNESS = 0
BEST_GENOME = 0
TOP_SCORE = 0

val_arr = [SCORE,MAX_FITNESS,GENERATION]

def eval_genomes(genomes, config):
     global TOP_SCORE
     global GENERATION
     val_arr = [TOP_SCORE, TOP_SCORE, GENERATION]

     # Play game and get results
     idx, genomes = zip(*genomes) # What does this do?

     genoinf,scoreinf = Game.game(genomes,config,val_arr) #game Returns fitness


     # Calculate fitness and top score
     top_score = 0

     for i, genomes in enumerate(genoinf):

         score = scoreinf[i]
         fitness = score
         genomes.fitness = -1 if fitness == 0 else fitness
         if top_score < score:
             top_score = score
         if TOP_SCORE < score:
             TOP_SCORE = score

     # print score
     print('The top score was:', top_score)
     GENERATION += 1

     fitness_vals.append(TOP_SCORE)
     mean_fit_vals.append(np.mean(scoreinf))




#Start of actualy program:

fitness_vals = []
mean_fit_vals = []

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         'config-feedforward')
pop = neat.Population(config)
pop.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
pop.add_reporter(stats)

winner = pop.run(eval_genomes, 10)




x = np.linspace(0,len(mean_fit_vals),len(mean_fit_vals))
fig2 = sns.lineplot(x=x,y=mean_fit_vals)
plt.xlabel("Generation")
plt.ylabel("Mean Fitness")
plt.show()


print(stats)


