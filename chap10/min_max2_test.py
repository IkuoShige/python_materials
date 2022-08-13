"""min_max2モジュールのmin_max2関数を呼び出す"""

import min_max2

x = float(input('実数x：'))
y = float(input('実数y：'))

mini, maxi = min_max2.min_max2(x, y)
print('最小値は', mini, 'です。')
print('最大値は', maxi, 'です。')
