# ファイルから文字列を読み込んで表示（with文）

with open('hello.txt', 'r') as f:
    for line in f:
        print(line, end='')
