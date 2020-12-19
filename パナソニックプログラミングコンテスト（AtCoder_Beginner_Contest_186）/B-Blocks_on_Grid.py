h_input, w_input = map(int, input().split())
array = []
for i in range(h_input):
    array.append(list(map(int, input().split())))

array = sum(array, [])
m = min(array)

ans = 0
for i in array:
    ans += i - m

print(ans)
