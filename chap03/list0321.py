# ２値の小さいほうの値を表示（その２：条件演算子）

a = int(input('整数a：'))
b = int(input('整数b：'))

min2 = a if a < b else b

print('小さいほうの値は', min2, 'です。')
