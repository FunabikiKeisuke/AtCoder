K, N = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
length = []
for i in range(len(A) - 1):
  length.append(A[i + 1] - A[i])
length.append(K - A[-1] + A[0])
print(sum(length) - max(length))
