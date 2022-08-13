# 円周の長さと円の面積を求める（その３：円周率としてmath.piを利用）

from math import pi

r = float(input('半径：'))

print('円周の長さは', 2 * pi * r, 'です。')
print('面積は', pi * r * r, 'です。')