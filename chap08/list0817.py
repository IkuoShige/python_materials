# 二つの文字列を集合化して集合演算を行う

set1 = set(input('文字列s1：'))
set2 = set(input('文字列s2：'))

print('set1：', set1)
print('set2：', set2)
print()
print('set1 == set2：', set1 == set2)
print('set1 != set2：', set1 != set2)
print('set1 <  set2：', set1 <  set2)
print('set1 <= set2：', set1 <= set2)
print('set1 >  set2：', set1 >  set2)
print('set1 >= set2：', set1 >= set2)
print()
print('set1 | set2：', set1 | set2)
print('set1 & set2：', set1 & set2)
print('set1 - set2：', set1 - set2)
print('set1 ^ set2：', set1 ^ set2)