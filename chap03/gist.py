# 第３章 まとめ

a = int(input('整数a：'))
b = int(input('整数b：'))
c = int(input('整数c：'))
d = int(input('整数d：'))

if     a: print('aはゼロではありません。')       # 0でなければ真
if not b: print('bはゼロです。')                 # 0でなければ真の否定

# aとbとcの最初の非ゼロを、１個もなければdをxに代入
x = a or b or c or d
print('x =', x)

if d % c:                                       # dをcで割ったあまりが0でない
    print('cはdの約数ではありません。')
else:
    print('cはdの約数です。')

print('cは' + ('奇数' if c % 2 else '偶数') + 'です。' )

print('点数dの評価：', end='')
if d < 0 or d > 100:    # 0～100以外
    print('不正な値')
elif d >= 60:           # 60～100
    print('合格')
else:                   # 0～59
    print('不合格')
