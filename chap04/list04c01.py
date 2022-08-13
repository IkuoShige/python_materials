# 正の整数値を0まで１秒ごとにカウントダウン

import time

print('カウントダウンします。')
n = int(input('正の整数値：'))

while n >= 0:
    print(n, end=' ')
    n -= 1           # nから1を引く
    time.sleep(1)    # 1秒お休み
print()
