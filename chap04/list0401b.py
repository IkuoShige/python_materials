# 整数値のカウントアップ（１個おきにカウントアップ）

a = int(input('整数a：'))
b = int(input('整数b：'))

a, b = sorted([a, b])       # 昇順にソート

counter = a
while counter <= b:
    print(counter, end=' ')
    counter = counter + 2   # counterに2を加える
print('\ncounterの値は', counter, 'です。')
