# import stdio
import sys

n = int (sys.argv[1])
w = int (sys.argv[2])

if n >= 0 and w >= 0:
  for i in range(n):
    for j in range(n):
      k = abs(j - i)
      if k > w:
        # stdio.write('0 ')
        print('0 ', end = '')
      else: 
        # stdio.write('* ')
        print('* ', end = '')
    # stdio.writeln()
    print()
else:
  # stdio.writeln('n and w must to be no negative')
  print('n and w must to be no negative')
      
