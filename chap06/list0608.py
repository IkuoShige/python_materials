# 文字列内の全文字をenumerate関数で走査して表示

s = input('文字列：')

for i, ch in enumerate(s):
    print('s[{}] = {}'.format(i, ch))
