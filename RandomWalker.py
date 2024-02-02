#----------------------------------------------------------------------------
"""
#Random Walker
This process is known as a two-dimensional random walk. 
This process is a discrete version of a natural phenomenon 
known as Brownian motion.
"""
#----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#----------------------------------------------------------------------------
"""
Takes an integer r and simulates the motion of a random walk 
until the random walker is at Manhattan distance r 
from the starting point
"""
#----------------------------------------------------------------------------
def main():
    r = int(input("Manhattan Distance from the starting point: "))
    if r < 0:
        raise ValueError("r must represent a measure")
    else:
        x = []
        y = []
        i = 0
        j = 0
        x.append(i)
        y.append(j)
        # print(f'step: ({i}, {j})')
        manhattan = 0
        steps = 0
        while manhattan < r:
            p = np.random.rand()
            if p < 0.25:
                i += 1
            elif p < 0.5:
                i -= 1
            elif p < 0.75:
                j += 1
            else:
                j -= 1
            # print(f'step: ({i}, {j})')
            x.append(i)
            y.append(j)
            ai = np.abs(i)
            aj = np.abs(j)
            manhattan = ai + aj
            steps += 1
        print(f'Final Steps: {steps}')
        X = np.array(x, dtype = int)
        Y = np.array(y, dtype = int)
        plt.figure(figsize = (9, 7))
        sns.set(style= 'darkgrid')
        plt.title(f'Random Walk with p = 1/2')
        plt.xlabel(f'step i')
        plt.ylabel(f'step j')
        sns.scatterplot(x = X, y = Y, color = '#088F8F', marker = 'o')
        plt.tight_layout()
        plt.show()


#----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
