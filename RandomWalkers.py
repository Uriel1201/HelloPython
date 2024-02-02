#----------------------------------------------------
"""
# Random Walkers

## The Weak Law of Large Numbers
The weak law of large numbers states that the average of 
the results obtained from a large number of independent 
and identical random samples converges in probability to 
the constant mu, where mu also represents the theoretical 
mean from each sample.

## Monte Carlo Simulation
Estimating an unknown quantity by generating random samples 
and aggregating the results is an example of a 
Monte Carlo Simulation.
"""
#----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#----------------------------------------------------
"""
Taking two integer r and trials. In each of trials independent 
experiments, simulate a random walk until the random walker is 
at Manhattan distance r from the starting point and generate a 
sample for the variable Steps.
"""
def main():
    r = int(input("Manhattan Distance from the starting point: "))
    trials= int(input("Number of Simulations: "))
    if r < 0:
        raise ValueError('r must represent a measure')
    else:
        total_steps = 0
        x = []
        for t in range(trials):
            i = 0
            j = 0
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
                ai = np.abs(i)
                aj = np.abs(j)
                manhattan = ai + aj
                steps += 1
            total_steps += steps
            dot = 1.0 * total_steps / (t + 1)
            x.append(dot)
        print(f'Average Number of Steps: {1.0 * sum / trials}')
        X = np.array(x, dtype = float)
        index = np.arange(len(X))
        plt.figure(figsize = (9, 7))
        sns.set(style= 'darkgrid')
        plt.title(f'Behaviour of the cocient #Steps/n')
        plt.xlabel(f'Trial Number')
        plt.ylabel(f'Average Number of Steps')
        plt.legend(['Average Steps'])
        sns.lineplot(x = index, y = X, color = '#088F8F', marker = 'o')
        plt.tight_layout()
        plt.show()


#----------------------------------------------------
if __name__ == '__main__':
    main()
