#import stdio
import sys
import numpy as np

m = input("Number of files?") 
n = input("Number of Columns?") 
k = input("How Many Mines?") 
t = m * n

shuffle = np.zeros(t, dtype = bool) 
shuffle[:k] = True

np.random.shuffle(shuffle)

mines = np.zeros([m + 2, n + 2], dtype = bool) 
for h in range(1, m + 1):
  for i in range(1, n + 1):
    mines[h, i] = shuffle[n * (h - 1) + i - 1]

count = np.zeros([m + 2, n + 2], dtype = int) 

for i in range(1, m + 1):
  for j in range(1, n + 1):
    count[i, j] = np.sum(mines[i - 1:i + 2, j - 1:j + 2])
      
for i in range(1, m + 1):
  for j in range(1, n + 1):
    if mines[i, j]: 
      print('*', end = '  ') 
      # stdio.write()
    else:
      print(count[i, j], end = '  ')
      # stdio.write() 
  print()
  # stdio.writeln()
