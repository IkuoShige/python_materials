# 第13章 まとめ（その１：自身のファイルの内容を行番号付きで表示）

with open('gist1.py', 'r', encoding='utf8') as f:
    for i, line in enumerate(f, 1):
        print(f'{i:04} {line}', end='')
