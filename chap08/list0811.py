# 辞書のすべてのキー、すべての値、すべての要素をリストとして取り出す

rgb = {'red': '赤', 'green': '緑', 'blue': '青'}

print('キー：', list(rgb.keys()))      # キーのビューをリストに変換
print('値　：', list(rgb.values()))    # 値のビューをリストに変換
print('要素：', list(rgb.items()))     # (キー, 値)のビューをリストに変換
