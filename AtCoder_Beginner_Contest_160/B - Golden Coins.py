X = int(input())
happy = 0
happy += X // 500 * 1000
happy += (X % 500) // 5 * 5
print(happy)