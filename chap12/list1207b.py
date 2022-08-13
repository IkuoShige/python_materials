# ユーザ定義の例外を送出（raiseによる送出を行わない）

class MyException(Exception):
    """マイ例外"""
    pass

def raise_my_exception() -> None:
    raise MyException

def func(sw: int) -> None:
    try:
        if sw == 0:
            raise_my_exception()
    except MyException as e:
        print('マイ例外を捕捉。')
        # マイ例外に対する対処を試みる。
        # 回復不可能と判断。
        print('回復できませんでした。')
        # raiseを実行しない

sw = int(input('sw：'))

try:
    func(sw)
except Exception as e:
    print('例外捕捉！')
    print(type(e))
