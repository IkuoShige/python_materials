# ファイルに２行分の文字列を追加する

f = open('hello.txt', 'a')  # オープン（テキスト＋追記モード）

f.write('Fine, thanks.\n')
f.write('And you?\n')

f.close()                   # クローズ
