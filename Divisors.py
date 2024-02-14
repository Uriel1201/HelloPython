# %%
# !! {"metadata":{
# !!   "id": "zgAiNcaZP3cQ"
# !! }}
"""
# **Divisors Methods**
Euler's Totient function plays a crucial role in various areas of mathematics including number theory, cryptography, and algorithms.
For instance the security of RSA encryption relies on the difficulty of factoring large numbers, which is facilitated by the use of this function in generating public and private keys.
"""

# %%
# !! {"metadata":{
# !!   "id": "0G97LBpP5Ktp",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1707851982464,
# !!     "user_tz": 360,
# !!     "elapsed": 1405,
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
# !!   "id": "mgoPBDE3NrMZ"
# !! }}
"""
### gcd(a, b):
The greatest common divisor (gcd) of two integers a and b. By convention, gcd(0,0)=0.
"""

# %%
# !! {"metadata":{
# !!   "id": "Q54xz9mNIFf8",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1707852001892,
# !!     "user_tz": 360,
# !!     "elapsed": 381,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
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
# !!   "id": "Sq3MnNsFQOmB"
# !! }}
"""

### lcm(a, b):
The least common multiple (lcm) of two integers a and b. By convention, if either a or b is 0, then lcm(a,b)=0.
"""

# %%
# !! {"metadata":{
# !!   "id": "AD78AI1ZNp_z",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1707852007723,
# !!     "user_tz": 360,
# !!     "elapsed": 466,
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
# !!   "id": "h8Jz0ij5RLFI"
# !! }}
"""
### areRelativelyPrime(a, b):
Are two integers a and b relatively prime?  
Two integers are relatively prime if they share no common positive factors (divisors) except 1.
"""

# %%
# !! {"metadata":{
# !!   "id": "tU45RoVXPmJv",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1707852013691,
# !!     "user_tz": 360,
# !!     "elapsed": 267,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
def areRelativelyPrime(a, b):
    g = gcd(a,b)
    return g == 1

# %%
# !! {"metadata":{
# !!   "id": "0SggJFGtYCsk"
# !! }}
"""
### dynamicPhi(n):
This method dynamically updates the Euler’s totient function ϕ(i) for each i less than n. This approach is based on the Euler's product representation, where the product is taken over the distinct prime numbers that divide n.
"""

# %%
# !! {"metadata":{
# !!   "id": "lpdUYImCQMER",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1707852019077,
# !!     "user_tz": 360,
# !!     "elapsed": 330,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
def dynamicPhi(n):
    if n < 0:
        raise ValueError('n must be positive')
    phi = np.arange(n + 1, dtype = int)
    for i in range(2, n + 1):
        if phi[i] == i:
            phi[i : n + 1 : i] -= phi[i : n + 1 : i] // i
    return phi

# %%
# !! {"metadata":{
# !!   "id": "xbEsgr9KbzQB"
# !! }}
"""
Finally composing a test client
"""

# %%
# !! {"metadata":{
# !!   "id": "ZQFYYpq5ZLnK",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1707852022375,
# !!     "user_tz": 360,
# !!     "elapsed": 24,
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
# !!     "timestamp": 1707852044964,
# !!     "user_tz": 360,
# !!     "elapsed": 19016,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "8ae06618-a282-4c66-dbf9-75b68fc8fb53"
# !! }}
if __name__ == '__main__':
    main()

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyNFQhLoTrXTjpvq9THw1Q+a"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}
