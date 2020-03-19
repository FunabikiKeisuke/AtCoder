import numpy as np
a1 = np.array(list(map(int, input().split())))
a2 = np.array(list(map(int, input().split())))
a3 = np.array(list(map(int, input().split())))
a = np.concatenate([a1, a2, a3], axis=0)
n = int(input())
b = 0
for i in range(n):
  b = int(input())
  a = np.where(a == b, 0, a)

a = a.reshape((3, 3))
if (a[0,0] == 0 and a[0,1] == 0 and a[0,2] == 0):
  print('Yes')
  exit()
if (a[1,0] == 0 and a[1,1] == 0 and a[1,2] == 0):
  print('Yes')
  exit()
if (a[2,0] == 0 and a[2,1] == 0 and a[2,2] == 0):
  print('Yes')
  exit()
if (a[0,0] == 0 and a[1,0] == 0 and a[2,0] == 0):
  print('Yes')
  exit()
if (a[0,1] == 0 and a[1,1] == 0 and a[2,1] == 0):
  print('Yes')
  exit()
if (a[0,2] == 0 and a[1,2] == 0 and a[2,2] == 0):
  print('Yes')
  exit()
if (a[0,0] == 0 and a[1,1] == 0 and a[2,2] == 0):
  print('Yes')
  exit()
if (a[0,2] == 0 and a[1,1] == 0 and a[2,0] == 0):
  print('Yes')
  exit()
print('No')
