# 読み込んだ整数値以下の全約数を列挙

n = int(input('整数値：'))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')
print()
