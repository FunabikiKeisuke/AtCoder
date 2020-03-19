N = int(input())
X = list(map(int, input().split()))

candidates = [sum(X) // N, sum(X) // N + 1]

ans = 0

a = 0
b = 0
for x in X:
    a += (x - candidates[0]) ** 2
    b += (x - candidates[1]) ** 2

if a < b:
    print(a)
else:
    print(b)
