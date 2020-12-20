import numpy as np

h_input, w_input = map(int, input().split())
array = []
for i in range(h_input):
    array.append(list(map(int, input().split())))

array = np.array(array)
ans = np.sum(array - np.min(array))
print(ans)
