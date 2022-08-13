# 辞書型実引数の**によるアンパックの例

def puts(n, s):
    """n個のsを連続して表示"""
    for _ in range(n):
        print(s, end='')

d1 = {'n': 3, 's': '*'}     # 3個の'*'
d2 = {'s': '+', 'n' :7}     # '+'を7個

puts(**d1)
print()
puts(**d2)
