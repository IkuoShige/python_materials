"""乗算表を表示（内部関数：引数を削除）"""

upper = int(input('1から何まで：'))

def multiplication_table(n: int) -> bool:

    """1～nまでの乗算表を表示"""
    if    1 <= n <=  3: w = 2
    elif  4 <= n <=  9: w = 3
    elif 10 <= n <= 31: w = 4
    else              : return False

    def put_bar() -> None:
        """n * w個の'-'を連続表示して改行"""
        print('-' * n * w)

    f = '{{:{}d}}'.format(w)
    put_bar()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f.format(i * j), end='')
        print()
    put_bar()
    return True

multiplication_table(upper)
