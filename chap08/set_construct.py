# 集合の生成

set01 = {1}                     # {1}
set02 = {1, 2, 3}               # {1, 2, 3}
set03 = {1, 2, 3,}              # {1, 2, 3}
set04 = {'A', 'B', 'C'}         # {'A', 'B', 'C'}

set05 = set()               # set()             空集合
set06 = set('ABC')          # {'A', 'B', 'C'}   文字列の個々の文字から生成
set07 = set([1, 2, 3])      # {1, 2, 3}         リストから生成
set08 = set([1, 2, 3, 2])   # {1, 2, 3}         リストから生成
set09 = set((1, 2, 3))      # {1, 2, 3}         タプルから生成

print('set01 =', set01)
print('set02 =', set02)
print('set03 =', set03)
print('set04 =', set04)
print('set05 =', set05)
print('set06 =', set06)
print('set07 =', set07)
print('set08 =', set08)
print('set09 =', set09)
