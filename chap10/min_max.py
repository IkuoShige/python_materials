"""最小値と最大値を求めるモジュール"""

def min_max2(a: 'value', b: 'value') -> 'value':
    """aとbの最小値と最大値を求めて返却"""
    return min(a, b), max(a, b)

def min_max3(a: 'value', b: 'value', c: 'value') -> 'value':
    """aとbとcの最小値と最大値を求めて返却"""
    return min(a, b, c), max(a, b, c)

if __name__ == '__main__':
    x = int(input('整数x：'))
    y = int(input('整数y：'))
    z = int(input('整数z：'))

    print('xとyの最小値は{}で最大値は{}です。'.format(*min_max2(x, y)))
    print('yとzの最小値は{}で最大値は{}です。'.format(*min_max2(y, z)))
    print('xとzの最小値は{}で最大値は{}です。'.format(*min_max2(x, z)))
    print('xとyとzの最小値は{}で最大値は{}です。'.format(*min_max3(x, y, z)))
