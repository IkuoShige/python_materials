# 第７章 まとめ

import random

MAX = 10
print('0～{}の乱数を生成します。'.format(MAX))
number = int(input('生成する個数：'))

# 要素数がnumberで全要素がNoneのリストを生成
v = [None] * number

# 全要素に0～MAXの乱数を代入
for i in range(number):
    v[i] = random.randint(0, MAX)

# リストとして表示
print(v)

# '*'による縦向き棒グラフとして表示
for i in range(MAX, 0, -1):
    for j in range(0, number):
        if v[j] >= i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print('-' * number)
for i in range(number):
    print(i % 10, end='')
