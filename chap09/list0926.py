# キーワード引数の強制

def puts(*, n, s):
    """n個のsを連続して表示"""
    for _ in range(n):
        print(s, end='')

puts(n = 3, s = '*')
print()
puts(s = '+', n = 7)
print()
puts(3, '*')    # エラー
