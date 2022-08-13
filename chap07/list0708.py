# 点数を読み込んで合計点・平均点を表示（その２：エラー）

print('合計点と平均点を求めます。')
number = int(input('学生の人数：'))

tensu = [None] * number

for i, point in enumerate(tensu):
    point = int(input('{}番の点数：'.format(i + 1)))

sum = 0
for i in range(number):
    sum += tensu[i]

print('合計は{}点です。'.format(total))
print('平均は{}点です。'.format(total / number))