# 文字列のインターンと同一性を判定

import sys

s1 = input('文字列s1：')
s2 = input('文字列s2：')

str1 = sys.intern(s1)
str2 = sys.intern(s2)

print('str1 is     str2 =', str(str1 is str2))
print('str1 is not str2 =', str(str1 is not str2))
