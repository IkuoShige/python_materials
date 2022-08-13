# ２値の最大値を求める

def max2(a, b):
    """aとbの最大値を求めて返却"""
    if a > b:
        return a
    return b

n1 = int(input('整数n1：'))
n2 = int(input('整数n2：'))

print('最大値は', max2(n1, n2), 'です。')
