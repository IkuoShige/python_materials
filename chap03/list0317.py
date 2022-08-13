# 読み込んだ月の季節を表示（その２：冬の判定を複数行で表記）

month = int(input('季節を求めます。\n何月ですか：'))

if month >= 3 and month <= 5:
    print('それは春です。')
elif month >= 6 and month <= 8:
    print('それは夏です。')
elif month >= 9 and month <= 11:
    print('それは秋です。')
elif (month == 1 or     #  1月は冬
      month == 2 or     #  2月も冬
      month == 12       # 12月も冬
     ):
    print('それは冬です。')
else:
    print('\aそんな月はありませんよ。')
