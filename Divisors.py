# %%
# !! {"metadata":{
# !!   "id": "rGnRPEkCH4Y2"
# !! }}
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# !! {"metadata":{
# !!   "id": "Q54xz9mNIFf8"
# !! }}
def gcd(a, b):
    if b < 0:
        b = -b
    if a < 0:
        a = -a
    if b > a:
        s = b
        b = a
        a = s
    if b == 0:
        return a
    else:
        while b > 0:
            t = a
            a = b
            b = t % a
        return a

# %%
# !! {"metadata":{
# !!   "id": "AD78AI1ZNp_z",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706740399060,
# !!     "user_tz": 360,
# !!     "elapsed": 406,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return np.abs(a) // gcd(a,b) * np.abs(b)

# %%
# !! {"metadata":{
# !!   "id": "tU45RoVXPmJv"
# !! }}
def areRelativelyPrime(a, b):
    g = gcd(a,b)
    return g == 1

# %%
# !! {"metadata":{
# !!   "id": "lpdUYImCQMER"
# !! }}
def dynamicPhi(n):
    if n < 0:
        raise ValueError('n must be positive')
    phi = np.zeros(n + 1, dtype = int)
    for i in range(n + 1):
        phi[i] = i
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi

# %%
# !! {"metadata":{
# !!   "id": "ZQFYYpq5ZLnK",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706740405384,
# !!     "user_tz": 360,
# !!     "elapsed": 370,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
def main():
    x = int(input("First Integer: "))
    y = int(input("Second Integer: "))
    print(f'gcd({x}, {y}): {gcd(x, y)}\n', end = '')
    print(f'lcm({x}, {y}): {lcm(x, y)}\n', end = '')
    print(f'areRelativelyPrime? : {areRelativelyPrime(x, y)}\n', end = '')
    z = np.maximum(x, y)
    totients = dynamicPhi(z)
    print(f'totient({x}): {totients[x]}\n', end = '')
    print(f'totient({y}): {totients[y]}\n', end = '')

    plt.figure(figsize = (9, 7))
    sns.set(style = 'darkgrid')
    index = np.arange(len(totients))
    plt.xlabel(f'n')
    plt.ylabel(f'phi(n)')
    plt.title(f"Euler's totient to {z}")
    sns.scatterplot(x =index, y = totients, color = '#088F8F')
    plt.tight_layout()
    plt.show()

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 398
# !!   },
# !!   "id": "gvt_mSVUcVrM",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706740489760,
# !!     "user_tz": 360,
# !!     "elapsed": 31200,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "8c13338e-c980-478d-b728-2e3f97b1fb27"
# !! }}
if __name__ == '__main__':
    main()

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyOkOr+hsvLwgsyUKfWWDSwZ"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}
