#---------------------------------------------------------------------
'''
# Activation Functions 
When working with artificial neural network models, we need a training phase 
to enhance their predictive ability. Input-output pairs are presented to the model, 
and weights are adjusted to minimize the error between the network output 
and the real values. 
There are many techniques to adjust these weights, such as the feedforward 
backpropagation algorithm, which is currently one of the most commonly used. 
This algorithm is an iterative gradient algorithm designed to minimize 
the mean square error between the predictive output and the desired output. 
It requires continuously differentiable nonlinearities, and activation 
functions are mainly used to generate nonlinear variations.
'''
#----------------------------------------------
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#----------------------------------------------
def heaviside(x):
    if np.isnan(x):
        return float('nan')
    elif x < 0.0:
        return 0.0
    elif x == 0.0:
        return 0.5
    else:
        return 1.0
        

#----------------------------------------------
def sigmoid(x):
    if np.isnan(x):
        return float('nan')
    x = -x
    return 1.0 / (1.0 + np.exp(x))


#----------------------------------------------
def tanh(x):
    if np.isnan(x):
        return float('nan')
    elif x >= 20.0:
        return 1.0
    elif x <= -20.0:
        return -1.0
    else:
        y = -x
        ex = np.exp(x)
        ey = np.exp(y)
        return (ex - ey) / (ex + ey)


#----------------------------------------------
def softsign(x):
    if np.isnan(x):
        return float('nan')
    elif x == np.inf:
        return 1.0
    elif x == -np.inf:
        return -1.0
    else:
        return x / (1.0 + np.abs(x))


#----------------------------------------------
def sqnl(x):
    if np.isnan(x):
        return float('nan')
    elif x <= -2.0:
        return -1.0
    elif x > -2.0 and x < 0.0:
        return x + (x * x) / 4.0
    elif x >= 0.0 and x < 2.0:
        return x - (x * x) / 4.0
    else:
        return 1.0


#----------------------------------------------
def main():
    f = float(input("Enter a floating-point number: "))
    print(f'heaviside({f}) : {heaviside(f)}\n', end = '')
    print(f'sigmoid({f}) : {sigmoid(f)}\n', end = '')
    print(f'tanh({f}) : {tanh(f)}\n', end = '')
    print(f'softsign({f}) : {softsign(f)}\n', end = '')
    print(f'sqnl({f}) : {sqnl(f)}\n', end = '')

    x = np.linspace(-25.0, 25.0, 10000, dtype = float)
    heaviside_v = np.vectorize(heaviside)
    sigmoid_v = np.vectorize(sigmoid)
    tanh_v = np.vectorize(tanh)
    softsign_v = np.vectorize(softsign)
    sqnl_v = np.vectorize(sqnl)
    y = [heaviside_v(x), sigmoid_v(x), tanh_v(x), softsign_v(x), sqnl_v(x)]
    names = ['Heaviside', 'Sigmoid', 'Tanh', 'Softsign', 'SQNL']
    plt.figure(figsize = (8, 3 * len(y)))

    sns.set(style = 'darkgrid')

    for i, y_i in enumerate(y, start = 1):
        plt.subplot(5, 1, i)
        plt.title(f'{names[i-1]}')
        sns.lineplot(x = x, y = y_i, color = '#088F8F')

    plt.tight_layout()
    plt.show()


#----------------------------------------------
if __name__ == '__main__':
    main()
