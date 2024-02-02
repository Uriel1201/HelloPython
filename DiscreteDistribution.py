#-------------------------------------------------------
"""
# Discrete Distribution Simulation
This script presents a simple algorithm for sampling
from a discrete probability distribution p(x) defined over 
a countably finite set.
In probability theory, this is known as sampling from a 
discrete distribution.
First define the values in the range of a discrete random 
variable named X, and then assigne to this values a 
weight of frequency.
"""
#-------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#-------------------------------------------------------
def main():
    n = int(input("Size of the sample: "))
    if n < 0:
        raise ValueError(f'The sample size must be positive')
    # A range for the discrete variable
    range_d = int(input("A cardinal between 2 and 10: "))
    if range_d < 0:
        raise ValueError(f'The cardinal |range(X)| must be no negative')
    if range_d > 10:
        raise ValueError(f'For practical purposes |range(X)| should not exceed 15')
    else:
        a = np.zeros(range_d, dtype = int)
        for i in range(range_d):
            mln = int(input(f'The length for X = {i + 1}: '))
            if mln < 0:
                raise ValueError(f'The length must represent a measure')
            else:
                a[i]= mln
        s = np.zeros(range_d + 1, dtype = int)
        for i in range(1, range_d + 1):
            s[i] = s[i - 1] + a[i - 1]
        x = []
        for i in range(n):
            p = int(np.random.rand() * s[range_d])
            for j in range(1, range_d + 1):
                if s[j] > p and s[j - 1] <= p:
                    x.append(j)
        X = np.array(x, dtype = int)
        plt.figure(figsize = (9, 7))
        sns.set(style= 'darkgrid')
        plt.title(f'Frequencies From the Sample')
        plt.ylabel(f'Frequency')
        plt.xlabel(f'x in Range(X)')
        sns.countplot(x = X, color = '#088F8F')
        plt.tight_layout()
        plt.show()


#-------------------------------------------------------
if __name__ == '__main__':
    main()
