# 長方形

print('長方形')
h = int(input('高さ：'))
w = int(input('横幅：'))

for i in range(1, h + 1):
    for _ in range(w):
        print('*', end='')
    print()
