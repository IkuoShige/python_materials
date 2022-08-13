# 書式化演算子%を用いた書式化（値をキーボードから読み込む）

a = int(input('整数a：'))
b = int(input('整数b：'))
n = int(input('整数n：'))
f1 = float(input('実数f1：'))
f2 = float(input('実数f2：'))
s1 = input('文字列s1：')
s2 = input('文字列s2：')

print('nの10進表記＝%d。' % n)
print('nの16進表記＝%o。' % n)
print('%dは8進で%oで16進で%x。' % (n, n, n))

print('nは%5dでf1は%9.5fでf2は%9.5fです。' % (n, f1, f2))

print('"%s"+"%s"は"%s"です。' % (s1, s2, s1 + s2))

print('%dと%dの和は%dです。' % (a, b, a + b))

print('%(no1)d+%(no2)dと%(no2)d+%(no1)dはいずれも%(sum)dです。' %
              {'no1': a, 'no2': b, 'sum': a + b})
