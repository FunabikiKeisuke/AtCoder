from math import comb


def main():
    """
    長さ L の棒の分割後の各棒の長さが全て正整数になるためには，整数長さ以外の場所を切ってはいけない．
    切る位置の候補は L-1 個あり，そこから異なる 11 箇所を選ぶ場合の数を求めれば良い．
    これは comb(L-1, 11) で求められる．
    """
    l_input = int(input())
    ans = comb(l_input-1, 11)
    return ans


if __name__ == '__main__':
    print(main())
