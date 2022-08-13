# 二つの整数値を昇順にソート（その２）

a = int(input('整数a：'))
b = int(input('整数b：'))

if a > b:
    a, b = b, a

print('a≦bとなるようにソートしました。')
print('変数aの値は', a, 'です。')
print('変数bの値は', b, 'です。')
