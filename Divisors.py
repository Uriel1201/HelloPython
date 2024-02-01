import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#-----------------------------------------------------------------------
"""
# **Divisors Methods**
"""
#-----------------------------------------------------------------------
"""
### gcd(a, b):
The greatest common divisor (gcd) of two integers a and b. 
By convention, gcd(0,0)=0.
"""
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


#-----------------------------------------------------------------------
"""
### lcm(a, b):
The least common multiple (lcm) of two integers a and b. 
By convention, if either a or b is 0, then lcm(a,b)=0.
"""
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return np.abs(a) // gcd(a,b) * np.abs(b)


#-----------------------------------------------------------------------
"""
### areRelativelyPrime(a, b):
Are two integers a and b relatively prime?  
Two integers are relatively prime if they share no common 
positive factors (divisors) except 1.
"""
def areRelativelyPrime(a, b):
    g = gcd(a,b)
    return g == 1


#-----------------------------------------------------------------------
"""
### dynamicPhi(n):
This method dynamically updates the Euler’s totient function ϕ(i) for each i less than n. 
This approach is based on the Euler's product representation, where the product 
is taken over the distinct prime numbers that divide n.
"""
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


#-----------------------------------------------------------------------
"""
Finally composing a test client
"""
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


#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
