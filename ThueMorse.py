# import stdio
import numpy as np 
import sys

n = int(sys.argv[1])

if n >= 0:
  a = np.zeros(n, dtype = int)
  
  for i in range(1, n):
    if i % 2 == 0: 
      a[i] = a[i // 2]
    else: 
      a[i] = 1 - a[i - 1]
      
  for i in  range(n):
    for j in range(n):
      if a[i] == a[j]: 
        print('+', end = '  ')
        # stdio.write()
      else: 
        print('-', end = '  ')
        # stdio.write()
    print()
    # stdio.writeln()
  
else: 
  print('n must to be no negative')
  # stdio.writeln()
