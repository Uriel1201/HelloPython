import sys
# import stdio 

n = int(sys.argv[1])
r = int(sys.argv[2])

if n > 0:
  sum = 0.0

  for i in range(n):
    term = 1.0 / pow(i + 1, r)
    sum = term + sum

  print(sum)
  # stdio.writeln(sum)

else:
  print('n must to be positive')
  # stdio.writeln('n must to be positive')
