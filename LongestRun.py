max = 0
rep = 1
x = readInt()
best = x

while not isEmpty(): 
  y = readInt() 
  if x == y:
    rep = rep + 1
  else:
    x = y
    rep = 1
  if max < rep:
    max = rep
    best = y

print('Longest Run: ', end = '')
print(max, end = '')
print('consecutive', end = '')
print(best, end = '')
print('s.')
