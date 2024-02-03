# %%
# !! {"metadata":{
# !!   "id": "cBNq13M_DxmQ"
# !! }}
"""
# Thue-Morse Sequence
The Thue-Morse Sequence is an infinite sequence of 0s and 1s that is constructed by starting with 0 and successively appending the bitwise negation of the existing sequence.
"""

# %%
# !! {"metadata":{
# !!   "id": "igbifJh_Dx9e",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706988851158,
# !!     "user_tz": 360,
# !!     "elapsed": 352,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pch
from matplotlib.collections import PatchCollection

# %%
# !! {"metadata":{
# !!   "id": "cGLpfeACb45V"
# !! }}
"""
For visualizing this sequence, create an n-by-n pattern printing black for 0 and white for 1.
"""

# %%
# !! {"metadata":{
# !!   "id": "OhkWHDY1D0d8",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706988855351,
# !!     "user_tz": 360,
# !!     "elapsed": 287,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
def main():
    n = int(input("n-by-n grid: "))
    if n < 0:
        raise ValueError("n must be no negative")
    a = np.zeros(n, dtype = int)
    patches_list = []
    for i in range(1, n):
        if i % 2 == 0:
            a[i] = a[i // 2]
        else:
            a[i] = 1 - a[i - 1]
    fig, ax = plt.subplots()
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    for i in range(n):
        for j in range(n):
            if a[i] == a[j]:
                color = 'black'
            else:
                color = 'white'
            r = pch.Rectangle((j, i), 1, 1, facecolor = color)
            patches_list.append(r)
    patch_collection = PatchCollection(patches_list, match_original = True)
    ax.add_collection(patch_collection)
    plt.title(f'Thue-Morse Sequence Plot')
    plt.show()

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 299
# !!   },
# !!   "id": "EqWz9HxrD7vZ",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1706988866829,
# !!     "user_tz": 360,
# !!     "elapsed": 7924,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "bfe22847-f22c-4ef8-fed7-8260d34f76d5"
# !! }}
if __name__ == '__main__':
    main()

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyM93/cVKGMRc7nAySuhftID"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}
