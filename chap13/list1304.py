# ファイルからすべての行の文字列を読み込んで表示

f = open('hello.txt')       # オープン（テキスト＋読込みモード）

while True:
    line = f.readline()
    if not line:            # 読み込めなかった（末尾に達した）
        break
    print(line, end='')

f.close()                   # クローズ
