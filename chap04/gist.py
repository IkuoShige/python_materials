# 第４章 まとめ

while True:
    n = int(input('0～100の整数値：'))
    if 0 <= n <= 100:
        break
c = n

# c個の'*'を表示
while n > 0:
    print('*', end='')
    n -= 1
print()

# '1234567890'を繰返し表示（全部でc文字）
for i in range(1, c + 1):
    print(i % 10, end='')
print('\n')

# 面積がsで縦横が整数の長方形の辺の長さを列挙
s = int(input('面積：'))
print('面積が{}で縦横が整数の'
      '長方形の辺の長さ'.format(s))
for i in range(1, s + 1):
    if i * i > s: break
    if s % i: continue
    print('{}×{}'.format(i, s // i))
print()

# n個の'*'をw個ごとに改行しながら表示
n = int(input('全部で何個表示：'))
w = int(input('何個ごとに改行：'))
for i in range(1, n + 1):
    print('*', end='')
    if i % w == 0:
        print()
if n % w != 1:
    print()
print()

# 数字長方形
h = int(input('高さ：'))
w = int(input('横幅：'))
for i in range(1, h + 1):
    for j in range(1, w + 1):
        print((i + j - 1) % 10, end='')
    print()
