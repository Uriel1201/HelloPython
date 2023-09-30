import sys
# import stdio

r = int(sys.argv[1])

if r >= 0:
  i = 0
  j = 0
  print('(' + i + ',' + j + ')')
  # stdio.writeln()
  manhattan = 0
  steps = 0
  while manhattan < r:
    p = random()
    if p < 0.25:   i = i + 1
    elif p < 0.5:  i = i - 1
    elif p < 0.75: j = j + 1
    else:          j = j - 1
    print('(' + i + ',' + j + ')')
    ai = abs(i)
    aj = abs(j)
    manhattan = ai + aj
    steps = steps + 1
  print('Steps: ' + steps)
  # stdio.writeln()
else:
  print('r must to be no negative')
  # stdio.writeln()
