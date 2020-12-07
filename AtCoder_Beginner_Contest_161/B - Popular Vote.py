N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
line = sum(A) / (4 * M)
count = 0
for i in A:
  if (i >= line):
    count += 1
if (count >= M):
  print("Yes")
else:
  print("No")

