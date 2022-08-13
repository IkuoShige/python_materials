# 人数と点数を読み込んで最低点・最高点を表示（その２：組込み関数を利用）

print('注："End"で入力終了。')

number = 0
tensu = []                  # 空リスト

while True:
    s = input('{}番の点数：'.format(number + 1))
    if s == 'End':
        break
    tensu.append(int(s))    # 末尾に追加
    number += 1

minimum = min(tensu)
maximum = max(tensu)

for i in range(1, number):
    if tensu[i] < minimum: minimum = tensu[i]
    if tensu[i] > maximum: maximum = tensu[i]

print('最低点は{}点です。'.format(minimum))
print('最高点は{}点です。'.format(maximum))
