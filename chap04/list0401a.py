# 整数値のカウントアップ（counterの最終値を表示）

a = int(input('整数a：'))
b = int(input('整数b：'))

a, b = sorted([a, b])       # 昇順にソート

counter = a
while counter <= b:
    print(counter, end=' ')
    counter = counter + 1   # counterに1を加える
print('\ncounterの値は', counter, 'です。')
