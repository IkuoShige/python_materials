# 辞書から取り出したビューをもとに走査（items()からキーと値を別々に取り出す）

rgb = {'red': '赤', 'green': '緑', 'blue': '青'}

# keys()で取り出したビューをもとに走査
for key in rgb.keys():
    print(key)

# values()で取り出したビューをもとに走査
for value in rgb.values():
    print(value)

# itmes()で取り出したビューをもとに走査
for key, value in rgb.items():
    print(key, value)
