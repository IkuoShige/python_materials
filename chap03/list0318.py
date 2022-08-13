# 読み込んだ月の季節を表示（その３：値比較演算子を連続適用）

month = int(input('季節を求めます。\n何月ですか：'))

if 3 <= month <= 5:
    print('それは春です。')
elif 6 <= month <= 8:
    print('それは夏です。')
elif 9 <= month <= 11:
    print('それは秋です。')
elif month == 12 or month == 1 or month == 2:
    print('それは冬です。')
else:
    print('そんな月はありませんよ。')
