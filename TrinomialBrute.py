#---------------------------------------------------------------
"""
# Trinomial Coefficients
Trinomial coefficients arise in combinatorics. The trinomial coefficient, 
denoted as T(n, k), represents the coefficient of x^(n+k) in the expansion 
of (1+x+x^2)^n. This script implements a recursive function in a brute-force manner 
to compute the coefficients by utilizing their corresponding recurrence relation. 
However, this approach may not be the most efficient way to solve this problem.
"""
#---------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#---------------------------------------------------------------
def trinomial(n, k):
    if n == 0 and k == 0:
        return 1
    elif k < -n or k > n:
        return 0
    else:
        return trinomial(n - 1, k - 1) + trinomial(n - 1, k) + trinomial(n - 1, k + 1)


#---------------------------------------------------------------
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


#---------------------------------------------------------------
if __name__ == '__main__':
    main()
