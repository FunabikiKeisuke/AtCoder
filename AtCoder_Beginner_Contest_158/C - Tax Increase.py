import math
a, b = map(int, input().split())
ta = a / 0.08
tb = b / 0.10
if (math.floor(ta * 0.1) == b):
  print(math.ceil(ta))
elif (math.floor(tb * 0.08) == a):
  print(math.ceil(tb))
else:
  print(-1)
