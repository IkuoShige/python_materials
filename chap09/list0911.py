# 受け取った時点での仮引数が実引数そのものであることを確認

def func(n):
    """仮引数の値と識別番号を表示"""
    print('n：', n, id(n))
    n = 0
    print('n：', n, id(n))

x = 5
print('x：', x, id(x))
func(x)
print('x：', x, id(x))
