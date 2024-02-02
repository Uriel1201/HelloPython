# %%
# !! {"metadata":{
# !!   "id": "LM0_px9PJlIs"
# !! }}
"""
#Random Walker
This process is known as a two-dimensional random walk. This process is a discrete version of a natural phenomenon known as Brownian motion.
"""

# %%
# !! {"metadata":{
# !!   "id": "vCz0L_XYJlll"
# !! }}
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# !! {"metadata":{
# !!   "id": "nYqNjGe0uuf1"
# !! }}
"""
Takes an integer r and simulates the motion of a random walk until the random walker is at Manhattan distance r from the starting point
"""

# %%
# !! {"metadata":{
# !!   "id": "hqU-3tWBJo1Z"
# !! }}
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

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 331
# !!   },
# !!   "id": "StexYYOnSl08",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706836642354,
# !!     "user_tz": 360,
# !!     "elapsed": 5707,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "741aae8d-04d8-4384-bb08-58b62296c0fa"
# !! }}
if __name__ == '__main__':
    main()

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyMyN5GJ8t+1A2LHiRWNlslv"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}
