# 第９章 まとめ

def range_of(*v):
    """最大値と最小値の差を返却"""
    return abs(max(v) - min(v))

print('range_of(1, 5)           = ', range_of(1, 5))
print('range_of(1, -3, 2, 5, 4) = ', range_of(1, -3, 2, 5, 4))