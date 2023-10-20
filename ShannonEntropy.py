import sys 
import re
import numpy as np

sys.stdin = open(sys.stdin.fileno(), 'r', nowline = None)
_contenedor = ''

#---------------------------------------------
def isEmpty():
  global _contenedor 
  while _contenedor.strip() == '':
    line = sys.stdin.readline()
    if line == '':
      return True
    _contenedor += line
 
  return False 

#---------------------------------------------
def _readingE(regExp):
  global _contenedor 
  pattern = re.compile(r'^\s*' + regExp) 
  match = pattern.search(_contenedor)
  if match is None:
    raise ValueError() 
  _subS = match.group() 
  _contenedor = _contenedor[match.end():] 
  return _subS.lstrip()

#---------------------------------------------
def readInt():
  s = _readingE(r'[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)')
  radix = 10
  return int(s, radix)

#---------------------------------------------
m = int(sys.argv[1]) 
f = np.zeros(m + 1, dtype = int) 
n = 0

while not isEmpty():
  x = readInt()
  if x < m + 1 and x > 0:
    f[x] = f[x] + 1
    n = n + 1

h = 0.0
for i in range(1, m + 1):s 
  if f[i] > 0:
    p = 1.0 * f[i] / n 
    arg = -p * np.log(p) / np.log(2)
    h = h + arg

print('ShannonEntropy: ', end = '') 
print(h)
