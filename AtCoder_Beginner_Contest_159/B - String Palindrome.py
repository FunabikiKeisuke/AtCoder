S = input()
left = S[:int((len(S) - 1) / 2)]
right = S[int((len(S) + 1) / 2):]

if (S == S[::-1] and left == left[::-1] and right == right[::-1]):
  print('Yes')
else:
  print('No')
