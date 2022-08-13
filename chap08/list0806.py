# updateメソッドによる辞書の結合（重複あり）

rgb = {'red': '赤', 'green': '緑', 'blue': '青'}
cry = {'cyan': '水色', 'red': '紅', 'yellow': '黄'}

# 辞書rgbに辞書cryを結合
rgb.update(cry)
print(rgb)
