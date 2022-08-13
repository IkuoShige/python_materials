# ファイルからすべての行の文字列を読み込んで表示（readlinesメソッド）

f = open('hello.txt')       # オープン（テキスト＋読込みモード）

lines = f.readlines()
for line in lines:
    print(line, end='')

f.close()                   # クローズ
