# 整数値のカウントアップ（ソート後のaからbまで）

a = int(input('整数a：'))
b = int(input('整数b：'))

a, b = sorted([a, b])       # 昇順にソート

counter = a
while counter <= b:
    print(counter, end=' ')
    counter = counter + 1   # counterに1を加える
print()
