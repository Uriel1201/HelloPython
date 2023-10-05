import sys

n = int(sys.argv[1])
sum = 0

for i in range(2, 11):
  dig = n % 10
  sum = sum + dig * i
  n = n // 10

print('The ISBN for your number is:', end = ' ')
print(sys.argv[1], end = '')

r = sum % 11
if r == 0:
  print('0')
elif r == 1:
  print('X')
else: 
  print(11 - r)
