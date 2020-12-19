from itertools import combinations
n_input = int(input())
l = list(map(int, input().split()))
ans = 0
for i, j in combinations(l, 2):
    ans += abs(i - j)

print(ans)
