#import stdio
import sys
import random
import numpy as np 

n = len(sys.argv)
m = int(sys.argv[1])

a = np.zeros(n - 2, dtype = int)
for i in range(n - 2):
  a[i] = int(sys.argv[i + 2])

s = np.zeros(n - 1, dtype = int)
for i in range(1, n - 1):
  s[i] = s[i - 1] + a[i - 1] 

for k in range(m):
  p = int(random.random() * s[n - 2])
  for j in range(1, n - 1):
    if s[j] > p and s[j - 1] <= p:
      print(j, end = ' ')
      # stdio.write()
