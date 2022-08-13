# ユーザ定義関数putsと組込み関数maxのドキュメントを表示

def puts(n, s):
    """n個のsを連続して表示"""
    for _ in range(n):
        print(s, end='')

help(puts)
help(max)
