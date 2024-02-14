# %%
# !! {"metadata":{
# !!   "id": "maNj9PSx5fPz"
# !! }}
"""
# Trinomial Coefficients
Trinomial coefficients arise in combinatorics. The trinomial coefficient, denoted as T(n, k), represents the coefficient of x^(n+k) in the expansion of (1+x+x^2)^n. This script implements a recursive function in a brute-force manner to compute the coefficients by utilizing their corresponding recurrence relation. However, this approach may not be the most efficient way to solve this problem.
"""

# %%
# !! {"metadata":{
# !!   "id": "ZQMY83Y3XK4t",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1707946860623,
# !!     "user_tz": 360,
# !!     "elapsed": 464,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %%
# !! {"metadata":{
# !!   "id": "3IoPMd2s5wtd"
# !! }}
def trinomial(n, k):
    if n == 0 and k == 0:
        return 1
    elif k < -n or k > n:
        return 0
    else:
        return trinomial(n - 1, k - 1) + trinomial(n - 1, k) + trinomial(n - 1, k + 1)

# %%
# !! {"metadata":{
# !!   "id": "8DyB1wx45ZTk",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1707946893770,
# !!     "user_tz": 360,
# !!     "elapsed": 355,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
def main():
    n = int(input(f'integer n: '))
    k = np.arange(-n, n + 1, dtype = int)
    trinomial_v = np.vectorize(trinomial)
    y = trinomial_v(np.full_like(k, n), k)
    plt.figure(figsize = (9, 8))
    sns.set(style = 'darkgrid')
    plt.title(f'trinomial coefficients for n: {n}')
    sns.scatterplot(x = k, y = y, color = '#088F8F')
    plt.tight_layout()
    plt.show()
    print(f'trinomial({n}, {k[n]}): {y[n]}')

# %%
# !! {"metadata":{
# !!   "id": "K93Mnbq45hiy",
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 350
# !!   },
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1707946910302,
# !!     "user_tz": 360,
# !!     "elapsed": 13099,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "b3712d9b-6eb9-4464-bc55-8fa683867bc9"
# !! }}
if __name__ == '__main__':
    main()

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyNNQSsvUAnbp1ClXqTsW18x"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}
