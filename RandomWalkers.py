import sys
import random
# import stdio

r      = int(sys.argv[1])
trials = int(sys.args[2])

if r >= 0:
  sum = 0
  
  for t in range(trials):
    i = 0
    j = 0
    manhattan = 0 
    steps = 0
    
    while manhattan < r:
      p = random.random()
      
      if   p < 0.25: i = i + 1
      elif p < 0.5:  i = i - 1
      elif p < 0.75: j = j + 1
      else:          j = j - 1
      
      ai = abs(i)
      aj = abs(j)
      manhattan = ai + aj
      steps = steps + 1

    sum = sum + steps
    
  average = sum / trial
  print ('Average Number of Steps: ', end = '')
  print (average)
  # stdio.writeln()

else:
  print('r must to be no negative')
  # stdio.writeln()
