# 文字列内の全文字をenumerate関数で逆順に走査して表示

s = input('文字列：')

for i, ch in enumerate(reversed(s), 1):
    print('後ろから{}番目の文字：{}'.format(i, ch))
