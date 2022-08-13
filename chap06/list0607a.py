# 文字列txt内に文字列ptnは含まれているか（別解：not in演算子）

txt = input('文字列txt：')
ptn = input('文字列ptn：')

if ptn not in txt:
    print('ptnはtxtに含まれていません。')
else:
    print('ptnはtxtに含まれています。')
