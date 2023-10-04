# import stdio
import sys
import random 
import numpy

n = int(sys.argv[1])
trials = int(sys.argv[2])
m = n + 2
s = np.zeros(m, dtype = int)

for i in range(trials):
  birthday = np.zeros(n, dtype = bool)
  count = 0
  
  for j in range(n + 1):
    p = int(random.random() * n)
    count = count + 1
    if birthday[p]: 
      break
    birthday[p] = True
    
  s[count] = s[count] + 1

f = 0.0

for k in range(1, m):
  f = f + 1.0 * s[k] / trials 
  print(k, end = ' ')
  print(s[], end = ' ')
  print(f)
  # stdio.writeln()
  if f >= 0.5:
    break
  
