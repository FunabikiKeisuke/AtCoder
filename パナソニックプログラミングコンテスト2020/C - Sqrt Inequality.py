a, b, c = map(int, input().split())
left = 4 * a * b
right = c - (a + b)
if (right < 0):
  print('No')
  exit()
right = right ** 2
if (left < right):
  print('Yes')
else:
  print('No')
