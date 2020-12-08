def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    cnt = 0
    if r1+c1 == r2+c2 or r2-c1 == r2-c2 or abs(r1-r2)+abs(c1-c2) <= 3:
        cnt += 1
    print(cnt)
    
if __name__ == "__main__":
    main()

