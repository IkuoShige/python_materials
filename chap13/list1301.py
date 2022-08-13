# ファイルに２行分の文字列を書き込む

f = open('hello.txt', 'w')      # オープン（テキスト＋書込みモード）

f.write('Hello!\n')
f.write('How are you?\n')

f.close()                       # クローズ
