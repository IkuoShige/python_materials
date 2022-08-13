# 関数名を変数名にしてしまう

a, b, c = 3, 7, 5
max = max(a, b, c)                          # １回目：ＯＫ
print('aとbとcの最大値は', max, 'です。')

max = max(a, b, c)                          # ２回目：エラー