# 乗算と除算を行うプログラム（例外処理：その３）

try:
    a = int(input('整数a：'))
    b = int(input('整数b：'))

    print('a * b は', a * b, 'です。')
    print('a / b は', a / b, 'です。')

except (ValueError, ZeroDivisionError) as e:
    print(type(e))
    print('認識不能orゼロ除算！')

else:
    print('正常終了！')

finally:
    print('お疲れさまでした。')
