"""２値の和を求めるラムダ式（その２）"""

a = int(input('整数a：'))
b = int(input('整数b：'))
print('aとbの和は', (lambda x, y: x + y)(a, b), 'です。')
