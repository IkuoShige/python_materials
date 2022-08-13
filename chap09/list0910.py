# 1からnまでの和を求めるプログラム

def sum_1ton(n):
    """1からnまでの整数の和を求める"""
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input('xの値：'))
total = sum_1ton(x)
print('1から', x, 'までの和は', total, 'です。')
