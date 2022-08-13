# 文字列に含まれる文字の出現回数を辞書に格納（その３：辞書内包表記【改良版】）

txt = input('文字列：')

count = {ch: txt.count(ch) for ch in set(txt)}

print('分布＝', count)
