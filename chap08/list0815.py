# 文字列に含まれる文字の出現回数を辞書に格納（その１）

txt = input('文字列：')

count = {}
for ch in txt:
    if ch not in count:
        count[ch] = 1   # 辞書に挿入
    else:
        count[ch] += 1  # 要素の値を更新

print('分布＝', count)
