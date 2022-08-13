# 第12章 まとめ（その１）

class RangeException(Exception):
    """範囲外の例外"""
    pass

class ParameterRangeException(RangeException):
    """仮引数範囲外の例外"""
    pass

class ResultException(RangeException):
    """返却値範囲外の例外"""
    pass

def is_valid(value: int) -> bool:
    """valueは0～9か？"""
    return 0 <= value <= 9

def add(a: int, b: int) -> int:
    """aとbの和を返却

    事前条件：aとbは0～9であること
              満たされない場合はParameterRangeExceptionを送出

    事後条件：返却する和は0～9であること
              満たされない場合はResultRangeExceptionを送出

    """
    if not is_valid(a):
        raise ParameterRangeException
    if not is_valid(b):
        raise ParameterRangeException

    result = a + b

    if not is_valid(result):
        raise ResultException
    return result

a = int(input('整数a：'))
b = int(input('整数b：'))

try:
    print('それらの和は{}です。'.format(add(a, b)))
except RangeException:
    print('範囲外です。')
except:
    print('何らかの例外が発生しました')
finally:
    print('お疲れさまでした。')
