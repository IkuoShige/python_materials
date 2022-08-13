# 辞書の全キーをenumerate関数で走査（1からカウント）

rgb = {'red': '赤', 'green': '緑', 'blue': '青'}

for i, key in enumerate(rgb, 1):
    print('{} {}'.format(i, key))
