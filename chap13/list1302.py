# ファイルから２行分の文字列を読み込んで表示

f = open('hello.txt')       # オープン（テキスト＋読込みモード）

line1 = f.readline()        # １行分読み込む
line2 = f.readline()        # １行分読み込む

print(line1, end='')
print(line2, end='')

f.close()                   # クローズ
