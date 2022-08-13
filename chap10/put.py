"""表示モジュールput
   関数：
       puts -- n個のsを連続して表示
       put_star -- n個の'*'を連続して表示
"""

def puts(*, n: int, s: str) -> None:
    """n個のsを連続して表示
    仮引数:
        キーワード引数n -- 表示する文字列の個数
        キーワード引数s -- 表示する文字列
    返却値:
        無し
    """
    for _ in range(n):
        print(s, end='')

def put_star(n: int) -> None:
    """n個の'*'を連続して表示
    仮引数:
        引数n -- 表示する個数
    返却値:
        無し
    """
    puts(n=n, s='*')
