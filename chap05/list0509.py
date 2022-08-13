# 整数値を左右にシフトした値を２進数で表示

x = int(input('整数：'))
n = int(input('シフトするビット数：'))

print('x      = {:b}'.format(x))
print('x << n = {:b}'.format(x << n))
print('x >> n = {:b}'.format(x >> n))
