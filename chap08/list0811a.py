# 辞書のすべてのキー、すべての値、すべての要素をタプルとして取り出す

rgb = {'red': '赤', 'green': '緑', 'blue': '青'}

print('キー：', tuple(rgb.keys()))      # キーのビューをタプルに変換
print('値　：', tuple(rgb.values()))    # 値のビューをタプルに変換
print('要素：', tuple(rgb.items()))     # (キー, 値)のビューをタプルに変換
