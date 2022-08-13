# リストの全要素を２倍にする（関数）

def double(n):
    return 2 * n

x = [1, 2, 3, 4]
y = map(double, x)

print(list(y))
