n = int(input())
r = 'a',
# r = ['a']
for _ in range(n - 1):
  r = {s + c for s in r for c in s + chr(ord(max(s)) + 1)}
  #
  # for s in r:
  #   for c in s + chr(ord(max(s)) + 1):
  #     r.append(s + c)
#
print(*sorted(r), sep='\n')
