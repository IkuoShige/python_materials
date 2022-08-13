# 引数の和を表示しながら求める（実引数のアンパック）

def print_sum(a, *no):
    """引数の和を返却（式も表示）"""
    sum = a
    print(a, end='')
    n = len(no)
    if n > 0:
        print(' + ', end='')
        for i in range(n - 1):
            sum += no[i]
            print(no[i], '+ ', end='')
        sum += no[n - 1]
        print(no[n - 1], end='')
    print(' =', sum)
    return sum

lst1 = [1, 3, 5, 7]
print_sum(*lst1)
