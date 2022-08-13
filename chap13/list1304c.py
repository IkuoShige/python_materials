# ファイルからすべての行の文字列を読み込んで表示（走査の対象はファイルオブジェクト）

f = open('hello.txt')       # オープン（テキスト＋読込みモード）

for line in f:
    print(line, end='')

f.close()                   # クローズ
