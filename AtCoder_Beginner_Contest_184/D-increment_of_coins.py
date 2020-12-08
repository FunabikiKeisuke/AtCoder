def main():
    a, b, c = map(int, input().split())
    abc = a+b+c
    ans = (100 - a) * (a / abc) + (100 - b) * (b / abc) + (100 - c) * (c / abc)
    print(ans)

if __name__ == "__main__":
    main()
