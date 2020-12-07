H, W = map(int, input().split())
grid = []
for i in range(H):
    array = input()
    tmp = []
    for j in range(W):
        tmp.append(array[j])
    grid.append(tmp)
print(grid[0][0])
change_count = 0
if (grid[0][0] == '#'):
    change_count += 1

