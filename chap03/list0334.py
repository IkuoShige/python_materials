# 二つの整数値を降順にソート

a = int(input('整数a：'))
b = int(input('整数b：'))

a, b = sorted([a, b], reverse=True)  # 降順にソート

print('a≧bとなるようにソートしました。')
print('変数aの値は', a, 'です。')
print('変数bの値は', b, 'です。')
