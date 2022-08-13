# 三つの整数値を昇順にソート（sroted関数）

a = int(input('整数a：'))
b = int(input('整数b：'))
c = int(input('整数c：'))

a, b, c = sorted([a, b, c])     # ３値を昇順にソート

print('a≦b≦cとなるようにソートしました。')
print('変数aの値は', a, 'です。')
print('変数bの値は', b, 'です。')
print('変数cの値は', c, 'です。')
