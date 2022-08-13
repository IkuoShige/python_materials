# 左下直角の二等辺三角形と長方形を表示（その２：キーワード引数）

# n個のsを連続して表示
def puts(n, s):
    for i in range(n):
        print(s, end='')

print('左下直角二等辺三角形')
n = int(input('短辺：'))

for i in range(1, n + 1):
    puts(n = i, s = '*')
    print()

print('長方形')
h = int(input('高さ：'))
w = int(input('横幅：'))

for i in range(1, h + 1):
    puts(s = '+', n = w)
    print()
