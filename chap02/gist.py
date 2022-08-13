# 第２章 まとめ

print('ABC', 'XYZ')
print('ABC', 'XYZ', end='')  # 最後で改行しない
print('ABC', 'XYZ', sep='')  # 区切りを入れない
print()                      # 改行
print('ABC\n\nXYZ', sep='')  # 途中で２回改行
print()                      # 改行

s = input('文字列：')
print('あなたは' , s , 'と入力しました。')
print('あなたは' + s + 'と入力しました。')
print('あなたは{}と入力しました。'.format(s))
print()

no = int(input('正の整数値：'))
print('最下位桁：', str(no % 10), sep='')
print('２進：' + bin(no))  # ２進文字列に変換
print('８進：' + oct(no))  # ８進文字列に変換
print('10進：' + str(no))  # 10進文字列に変換
print('16進：' + hex(no))  # 16進文字列に変換
print()

PI = 3.14159    # 円周率を表す定数
print('長方形と円の面積を求めます。')
width  = float(input('長方形の横幅：'))
height = float(input('長方形の高さ：'))
radius = float(input('円の直径：'))

print('長方形：{}'.format(width * height))
print('円　　：{}'.format(PI * radius * radius))
