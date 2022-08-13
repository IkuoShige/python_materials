# 文字列に含まれる文字の出現回数を辞書に格納（その２：辞書内包表記）

txt = input('文字列：')

count = {ch: txt.count(ch) for ch in txt}

print('分布＝', count)
