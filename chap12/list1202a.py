# 乗算と除算を行うプログラム（try-finally文）

try:
    a = int(input('整数a：'))
    b = int(input('整数b：'))

    print('a * b は', a * b, 'です。')
    print('a / b は', a / b, 'です。')

finally:
    print('お疲れさまでした。')
