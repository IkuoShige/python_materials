# リストの要素の並びを反転する

def reverse_list(lst):
    """lstの要素の並びを反転"""
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]

x = [22, 57, 11, 32, 91, 68, 77]
print('x =', x)

reverse_list(x)
print('x =', x)
