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
    if line = '':
      return True
    _contenedor += line
 
  return False s 

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
