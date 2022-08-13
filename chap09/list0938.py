# global文あり

n = 1

def func():
    global n
    n = 2    # nは広域変数
    print('n =', n)

print('n =', n)
func()
print('n =', n)
