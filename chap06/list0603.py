# 読み込んだ文字列内の全文字をfor文で走査して表示

s = input('文字列：')

for i in range(len(s)):
    print('s[{}] = {}'.format(i, s[i]))
