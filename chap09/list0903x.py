# 左下直角の二等辺三角形と長方形を表示
# ※エラー：関数定義を末尾に配置

print('左下直角二等辺三角形')
n = int(input('短辺：'))

for i in range(1, n + 1):
    put_star(i)
    print()

print('長方形')
h = int(input('高さ：'))
w = int(input('横幅：'))

for i in range(1, h + 1):
    put_star(w)
    print()

def put_star(n):
    """n個の'*'を連続して表示"""
    for _ in range(n):
        print('*', end='')
