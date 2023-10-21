'''
Writing a program that reads in a sequence of integers and
prints both the integer that appears in a longest consecutive 
run and  the length of that run.
'''

import sys 
import re 

sys.stdin = open(sys.stdin.fileno(), 'r', newline = None)
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
  return int(s, 10)

#---------------------------------------------
_max = 0
rep = 0
x = 0
best = x

while not isEmpty(): 
  y = readInt() 
  if x == y:
    rep = rep + 1
  else:
    x = y
    rep = 1
  if _max < rep:
    _max = rep
    best = y

print('Longest Run: ', end = '')
print(_max, end = ' ')
print('consecutive', end = ' ')
print(best, end = '')
print('s.')
