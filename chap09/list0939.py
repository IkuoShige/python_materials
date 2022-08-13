# nonlocal文なし

def outer():
    n = 1
    def inner():
        # 同名の変数を作成
        n = 2
        print('n =', n)

    print('n =', n)
    inner()
    print('n =', n)

outer()
