# ファイルからすべての行の文字列を読み込んで表示（readメソッド）

f = open('hello.txt')       # オープン（テキスト＋読込みモード）

lines = f.read()
print(lines, end='')

f.close()                   # クローズ
