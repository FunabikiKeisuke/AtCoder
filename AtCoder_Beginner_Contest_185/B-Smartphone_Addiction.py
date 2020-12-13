def main():
    n_input, m_input, t_input = map(int, input().split())
    b_prev = 0
    n_max = n_input
    ans = 'Error'

    for _ in range(m_input):
        a_tmp, b_tmp = map(int, input().split())
        n_input -= (a_tmp - b_prev)
        if n_input <= 0:
            ans = 'No'
            return ans
        n_input += (b_tmp - a_tmp)
        n_input = min(n_input, n_max)
        b_prev = b_tmp

    n_input -= (t_input - b_prev)
    if n_input <= 0:
        ans = 'No'
    else:
        ans = 'Yes'

    return ans


if __name__ == '__main__':
    print(main())
