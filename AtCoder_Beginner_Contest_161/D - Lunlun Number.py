K = int(input())

runrun = [[1]*10]
s = sum(runrun[0][1:])
i = 1
while K > s:
  K -= s
  r = [sum(runrun[-1][max(0,i-1):min(10, i+2)]) for i in range(10)]
  runrun.append(r)
  s = sum(r[1:])
  i += 1

j = 1
while runrun[-1][j] < K:
  K -= runrun[-1][j]
  j += 1

ans = [j]
k = -2
while K and len(runrun) >= -k:
  j = max(0, j-1)
  while runrun[k][j] < K:
    K -= runrun[k][j]
    j += 1
  k -= 1
  ans.append(j)

print("".join(map(str, ans)))
