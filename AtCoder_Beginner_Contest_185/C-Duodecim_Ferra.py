from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def main():
    l_input = int(input())
    surplus = l_input - 12
    ans = 0
    if surplus == 0:
        return 1

    return ans


if __name__ == '__main__':
    print(main())