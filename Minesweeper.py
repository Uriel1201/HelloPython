# import stdio 
import sys
import random 
import numpy as np 

m = int(sys.argv[1])
n = int(sys.argv[2])
k = int(sys.argv[3])
t = m * n

shuffle = np.zeros(t, dtype = bool)
for h in range(k):
  shuffle[h] = True

for h in range(t):
  p = h + int(random.random() * (t - h))
  s = shuffle[p]
  shuffle[p] = shuffle[h]
  shuffle[h] = s

mines = np.zeros([m + 2, n + 2], dtype = bool)
for h in range(1, m + 1):
  for i in range(1, n + 1):
    mines[h][i] = shuffle[n * (h - 1) + i - 1]

count = np.zeros([m + 2, n + 2], dtype = int) 
row = 1
while row < m + 1:
  col = 1
  while col < n + 1:
    for i in range(row - 1, row + 2):
      for j in range(col - 1, col + 2):
        if mines[i][j]: count[row][col] = count[row][col] + 1
    col = col + 1
  row = row + 1

for i in range(1, m + 1):
  for j in range(1, n + 1):
    if mines[i][j]: print('*', end = '  ')
      # stdio.write()
    else: print(count[i][j], end = '  ')
      # stdio.write()
  print()
  # stdio.writeln()
