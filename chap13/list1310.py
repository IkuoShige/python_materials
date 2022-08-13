# ファイルをダンプ（ファイルの中身をコードと文字とで表示）

import string

def is_print(ch: str) -> bool:
    """文字chは印字可能文字であるか？"""
    return (ch == ' ' or ch in string.digits or ch in string.ascii_letters
                      or ch in string.punctuation)

fname = input('ファイル名：')

with open(fname, 'rb') as f:
    count = 0    # アドレス（先頭から何バイト目か）
    while True:
        buf = f.read(16)
        n = len(buf)
        if n == 0:
            break
        print('%08x' % count, end=' ')         # アドレス
        for i in range(n):                     # 文字コード
            print('%02x' % buf[i], end=' ')
        if n < 16:
            print('   ' * (16 - n), end='')
        for i in buf:                          # 文字
            ch = chr(i)
            print('%c' % ch if is_print(ch) else '.', end='')
        print()
        if n < 16:
            break
        count += 16
