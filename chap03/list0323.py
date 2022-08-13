# 読み込んだ整数値の符号を表示（条件演算子）

n = int(input('整数値：'))

print('その値は' + ('正' if n > 0 else '０' if n == 0 else '負') + 'です。')
