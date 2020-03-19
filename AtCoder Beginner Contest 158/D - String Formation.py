def main():
  S = input()
  Q = int(input())
  for i in range(Q):
    q = input().split()
    if (q[0] == '1'):
      S = S[::-1]
    elif (q[1] == '1'):
      S = q[2] + S
    else:
      S += q[2]
  print(S)

if __name__ == '__main__':
  main()
