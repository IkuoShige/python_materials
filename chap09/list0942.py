"""関数の型と識別番号を表示"""

def min2(a, b):
    """aとbの最小値を求めて返却する関数"""
    return a if a < b else b

func = min2

print('type(min2), id(min2) = ', type(min2), id(min2))
print('type(func), id(func) = ', type(func), id(func))
