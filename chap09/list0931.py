"""辞書から特定の値をもつキーのリストを生成"""

def keys_of(dic: dict, val: 'value') -> list:
    """辞書dic内の値がvalである要素のキーのリストを返却"""
    return [k for k, v in dic.items() if v == val]

txt = input('文字列：')
count = {ch: txt.count(ch) for ch in txt}
print('分布＝', count)

num = int(input('何個の文字：'))
print('{}個の文字＝{}'.format(num, keys_of(count, num)))
