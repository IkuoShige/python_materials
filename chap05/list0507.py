# ビット単位の論理積・論理和・排他的論理和・反転を表示

a = int(input('正の整数a：'))
b = int(input('正の整数b：'))
w = int(input('表示桁数：'))

f = '{{:0{}b}}'.format(w)
m = 2 ** w - 1      # w桁すべてが1の２進数に相当

print('a     = ' + f.format(a))
print('b     = ' + f.format(b))
print('a & b = ' + f.format(a & b))
print('a | b = ' + f.format(a | b))
print('a ^ b = ' + f.format(a ^ b))
print('~a    = ' + f.format(~a & m))
print('~b    = ' + f.format(~b & m))
