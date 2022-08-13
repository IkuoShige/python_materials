# 整数値を左右にシフトした値を10進数で表示

x = int(input('整数：'))
n = int(input('シフトするビット数：'))

print('x << n = {:d}'.format(x << n))
print('x >> n = {:d}'.format(x >> n))
