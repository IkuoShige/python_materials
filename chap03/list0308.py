# 読み込んだ整数値の符号を表示（ゼロはパス）

n = int(input('整数値：'))

if n > 0:
    print('その値は正です。')
elif n == 0:
    pass
else:
    print('その値は負です。')