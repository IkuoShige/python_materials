# 長方形を表示

print('長方形')
h = int(input('高さ：'))
w = int(input('横幅：'))

for _ in range(h):
    for _ in range(w):
        print('*', end='')
    print()
