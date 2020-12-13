def main():
    input_n, input_x = map(int, input().split())
    input_s = input()
    for char in input_s:
        if char == 'o':
            input_x += 1
        elif input_x:  # input_x が 0 の場合は False のためデクリメントしない
            input_x -= 1

    print(input_x)


if __name__ == "__main__":
    main()
