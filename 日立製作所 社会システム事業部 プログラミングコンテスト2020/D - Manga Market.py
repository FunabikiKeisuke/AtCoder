N, T = map(float, input().split())
T += 0.5
A = []
B = []
for k in range(int(N)):
  a, b = list(map(int, input().split()))
  A.append(a)
  B.append(b)

ans = 0
t = 1
shoped = []
f_inf = float('inf')

while (t < T and ans < N):
  shoping = []
  for i in range(int(N)):
    shoping.insert(i, A[i] * t + B[i])
  for j in range(len(shoped)):
    shoping.insert(shoped[j], f_inf)
  time = min(shoping)
  shoped.append(shoping.index(time))
  t += time
  if (t < T):
    ans += 1

print(ans)