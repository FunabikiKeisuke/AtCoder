from cython import longlong

def main():
    N: longlong
    A: longlong
    a: longlong
    N = int(input())
    A = []
    a = input()

    i: longlong
    j: longlong
    for i in range(N):
      A.append(int(a[i]))
    for j in range(N):
      for i in range(N-j-1):
        A[i] = abs(A[i] - A[i+1])
    print(A[0])

if __name__ == '__main__':
    main()