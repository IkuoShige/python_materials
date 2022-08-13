# ２値の最大値を求める（別解：条件演算子を利用）

def max2(a, b):
    """aとbの最大値を求めて返却"""
    return a if a > b else b 	# 条件演算子if elseを利用

n1 = int(input('整数n1：'))
n2 = int(input('整数n2：'))

print('最大値は', max2(n1, n2), 'です。')
