# 文字列内の全文字をenumerate関数で走査（1からカウント）

s = input('文字列：')

for i, ch in enumerate(s, 1):
    print('{}番目の文字：{}'.format(i, ch))
