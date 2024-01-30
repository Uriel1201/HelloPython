# %%
# !! {"metadata":{
# !!   "id": "YvXjAR-6znRR"
# !! }}
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %%
# !! {"metadata":{
# !!   "id": "52sgmp0A6tE5"
# !! }}
def heaviside(x):
    if np.isnan(x):
        return float('nan')
    elif x < 0.0:
        return 0.0
    elif x == 0.0:
        return 0.5
    else:
        return 1.0

# %%
# !! {"metadata":{
# !!   "id": "XCsgV1dq6-Va"
# !! }}
def sigmoid(x):
    if np.isnan(x):
        return float('nan')
    x = -x
    return 1.0 / (1.0 + np.exp(x))

# %%
# !! {"metadata":{
# !!   "id": "7Wj4y6iI7CSe"
# !! }}
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

# %%
# !! {"metadata":{
# !!   "id": "2RDzagzx7GiV"
# !! }}
def softsign(x):
    if np.isnan(x):
        return float('nan')
    elif x == np.inf:
        return 1.0
    elif x == -np.inf:
        return -1.0
    else:
        return x / (1.0 + np.abs(x))

# %%
# !! {"metadata":{
# !!   "id": "q49dX1np7KZ9"
# !! }}
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

# %%
# !! {"metadata":{
# !!   "id": "S3EePDX17Pei"
# !! }}
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

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 756
# !!   },
# !!   "id": "nuNvKs1IF25N",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706576607759,
# !!     "user_tz": 360,
# !!     "elapsed": 8564,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "27efc138-b725-47a2-9cef-bb42e3a0007e"
# !! }}
if __name__ == '__main__':
    main()

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyPLIYQrLeZjP2On/NraYjLL"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}
