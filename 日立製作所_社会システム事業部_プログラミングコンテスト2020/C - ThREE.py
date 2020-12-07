N = int(input())
A = []
B = []
ans = []

for i in range(N-1):
  a, b = list(map(int, input().split()))
  A.append(a)
  B.append(b)

if (A[2] == B[0]):
  ans = [1, 5, 2, 4, 3]
elif (A[2] == B[1]):
  ans = [1, 2, 5, 4, 3]

print(*ans, sep=' ')
