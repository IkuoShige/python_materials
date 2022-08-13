# 小さいほうの値と大きいほうの値を求めて表示（その４：条件演算子）

a = int(input('整数a：'))
b = int(input('整数b：'))

min2, max2 = (a, b) if a < b else (b, a)

print('小さいほうの値は', min2, 'です。')
print('大きいほうの値は', max2, 'です。')
