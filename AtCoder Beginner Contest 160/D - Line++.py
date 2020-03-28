n, x, y = map(int, input().split())
D = [0] * (n - 1)
x -= 1
y -= 1
for i in range(n - 1):
  for j in range(i + 1, n):
    D[min(j - i - 1, abs(x - i) + abs(y - j))] += 1
for d in D: print(d)
