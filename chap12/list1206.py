# raise文による例外の送出

def func(sw: int) -> None:
    if sw == 0:
        raise ValueError
    elif sw == 1:
        raise ZeroDivisionError

sw = int(input('sw：'))

try:
    func(sw)

except BaseException as e:
    print('例外捕捉！')
    print(type(e))
