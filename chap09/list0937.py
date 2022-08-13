# global文なし

n = 1

def func():
    # 同名の変数を作成
    n = 2    # nは局所変数
    print('n =', n)

print('n =', n)
func()
print('n =', n)
