# タプルにまとめられている３値の最大値を求める

def max3(a, b, c):
    """aとbとcの最大値を求めて返却"""
    max = a
    if b > max: max = b
    if c > max: max = c
    return max

tpl1 = (1, 3, 5)
m = max3(*tpl1)
print(tpl1, 'の最大値は', m, 'です。')
