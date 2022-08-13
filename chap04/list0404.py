# 1からnまでの和を求める（nに正の整数値を読み込む）

print('1からnまでの和を求めます。')

while True:
    n = int(input('nの値：'))
    if n > 0:
        break

sum = 0
i = 1
while i <= n:
    sum += i   # sumにiを加える
    i += 1     # iに1を加える
print('1から', n, 'までの和は', sum, 'です。')
