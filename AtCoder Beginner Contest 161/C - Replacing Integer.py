N, K = list(map(int, input().split()))
N = N % K
while True:
  last = abs(N - K)
  if (last < N):
    N = last
  else:
    print(N)
    exit()
