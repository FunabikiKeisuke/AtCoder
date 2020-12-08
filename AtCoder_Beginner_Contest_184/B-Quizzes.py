def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'o':
            X += 1
        elif X:  # X が 0 の場合は False のためデクリメントしない
            X -= 1

    print(X)

if __name__ == "__main__":
    main()
