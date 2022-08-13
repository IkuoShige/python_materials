# for文による整数値のカウントアップ（ソート後のaからbまで）

a = int(input('整数a：'))
b = int(input('整数b：'))

a, b = sorted([a, b])       # 昇順にソート

for counter in range(a, b + 1):
    print(counter, end=' ')
print()
