# updateメソッドによる辞書の結合（重複なし）

rgb = {'red': '赤', 'green': '緑', 'blue': '青'}
cmy = {'cyan': '水色', 'magenta': '赤紫', 'yellow': '黄'}

# 辞書rgbに辞書cmyを結合
rgb.update(cmy)
print(rgb)
