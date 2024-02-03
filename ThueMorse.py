#----------------------------------------------------------
"""
# Thue-Morse Sequence
The Thue-Morse Sequence is an infinite sequence of 0s and 1s 
that is constructed by starting with 0 and successively appending 
the bitwise negation of the existing sequence.
"""
#----------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pch
from matplotlib.collections import PatchCollection


#----------------------------------------------------------
"""
For visualizing this sequence, create an n-by-n pattern 
printing black for 0 and white for 1.
"""

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


#----------------------------------------------------------
if __name__ == '__main__':
    main()
