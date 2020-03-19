# var 1
# n, a, b = map(int, input().split())
# tmp = []
# while len(tmp) <= n:
#   for i in range(a):
#     tmp.append('b')
#   for j in range(b):
#     tmp.append('r')
# ans = []
# for k in range(n):
#   ans.append(tmp[k])
# print(ans.count('b'))

# var 2
# n, a ,b = map(int, input().split())
# ans = 0
# length = 0
# while length <= n:
#   length += a + b
#   ans += a
# over = length - n
# if (over == 0):
#   print(ans)
# else:
#   if (over <= b):
#     print(ans)
#   else:
#     over -= b
#     ans -= over
#     print(ans)

n, a, b = map(int, input().split())
q = n // (a+b)
mod = n % (a+b)
ans = q * a
if (mod > a):
  ans += a
else:
  ans += mod
print(ans)


