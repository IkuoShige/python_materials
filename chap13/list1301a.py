# ファイルに２行分の文字列を書き込む（writelinesメソッド）

f = open('hello.txt', 'w')      # オープン（テキスト＋書込みモード）

f.writelines(['Hello!\n', 'How are you?\n'])

f.close()                       # クローズ
