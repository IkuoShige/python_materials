# 四つの整数値を昇順にソート（sroted関数）

a = int(input('整数a：'))
b = int(input('整数b：'))
c = int(input('整数c：'))
d = int(input('整数d：'))

a, b, c, d = sorted([a, b, c, d])   # ４値を昇順にソート

print('a≦b≦c≦dとなるようにソートしました。')
print('変数aの値は', a, 'です。')
print('変数bの値は', b, 'です。')
print('変数cの値は', c, 'です。')
print('変数dの値は', d, 'です。')
