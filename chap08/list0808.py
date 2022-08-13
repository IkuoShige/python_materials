# 辞書の全キーをenumerate関数で走査

rgb = {'red': '赤', 'green': '緑', 'blue': '青'}

for i, key in enumerate(rgb):
    print('{} {}'.format(i, key))
