# %%
# !! {"metadata":{
# !!   "id": "RwkM6q57LNu6"
# !! }}
"""
# Random Walkers

## The Weak Law of Large Numbers
The weak law of large numbers states that the average of the results obtained from a large number of independent and identical random samples converges in probability to the constant mu, where mu also represents the theoretical mean from each sample.

## Monte Carlo Simulation
Estimating an unknown quantity by generating random samples and aggregating the results is an example of a Monte Carlo Simulation.
"""

# %%
# !! {"metadata":{
# !!   "id": "MQCu5wwNLOSL",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706900623736,
# !!     "user_tz": 360,
# !!     "elapsed": 287,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# !! {"metadata":{
# !!   "id": "31nIdPi2MaLu"
# !! }}
"""
Taking two integer r and trials. In each of trials independent experiments, simulate a random walk until the random walker is at Manhattan distance r from the starting point and generate a sample for the variable Steps.
"""

# %%
# !! {"metadata":{
# !!   "id": "HWB8dISL6XUj",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706900627817,
# !!     "user_tz": 360,
# !!     "elapsed": 279,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
def main():
    r = int(input("Manhattan Distance from the starting point: "))
    trials= int(input("Number of Simulations: "))
    if r < 0:
        raise ValueError('r must represent a measure')
    else:
        sum = 0
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
            sum += steps
            dot = 1.0 * sum / (t + 1)
            x.append(dot)
        print(f'Average Number of Steps: {1.0 * sum / trials}')
        X = np.array(x, dtype = float)
        index = np.arange(len(X))
        plt.figure(figsize = (9, 7))
        sns.set(style= 'darkgrid')
        plt.title(f'Behaviour of the cocient #Steps/n')
        plt.xlabel(f'trials')
        plt.ylabel(f'Average')
        sns.lineplot(x = index, y = X, color = '#088F8F', marker = 'o')
        plt.tight_layout()
        plt.show()

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 349
# !!   },
# !!   "id": "t1d9cq7T_Q56",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706900673012,
# !!     "user_tz": 360,
# !!     "elapsed": 7753,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "d2f6656a-4bae-436c-f2e6-a4b48ab16c18"
# !! }}
if __name__ == '__main__':
    main()

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyOQ9CbFtrZ34YMb7inUKkZm"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}
