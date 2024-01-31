import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#--------------------------------------------------
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


#--------------------------------------------------
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return np.abs(a) // gcd(a,b) * np.abs(b)


#--------------------------------------------------
def areRelativelyPrime(a, b):
    g = gcd(a,b)
    return g == 1


#--------------------------------------------------
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


#--------------------------------------------------
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


#--------------------------------------------------
if __name__ == '__main__':
    main()
