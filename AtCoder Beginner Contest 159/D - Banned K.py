import copy
import collections
import numpy as np

N = int(input())
A = list(map(int, input().split()))
c = 0

for j in range(N):
  B = copy.copy(A)
  B[j] = 0
  c = collections.Counter(B)
  c = np.array(list(c.values()))
  print(int(np.sum((c * (c - 1) / 2))))

# for j in range(N):
#   B = copy.copy(A)
#   B[j] = 0
#   cnt = 0
#   for i in range(N):
#     c = B.count(i+1)
#     if c <= 1:
#       cnt += 0
#     else:
#       cnt += int((c * (c - 1) / 2))
#   print(cnt)

def main():
  from collections import defaultdict
  from collections import Counter

  n = int(input())
  a = list(map(int, input().split()))

  d = Counter(a)
  e = defaultdict(int)

  func = lambda x: x * (x - 1) // 2 if x >= 2 else 0
  v = list(d.values())
  base = sum(list(map(func, v)))

  for k, v in d.items():
    if v <= 1:
      e[k] = base - 0
    else:
      e[k] = base - (v * (v - 1) // 2 - (v - 1) * (v - 2) // 2)

  p = [str(e[x]) + '\n' for x in a]
  q = ''.join(p)
  print(q)


if __name__ == '__main__':
  main()

