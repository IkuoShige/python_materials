# ファイルに２行分の文字列を書き込む（writelinesメソッド）

f = open('hello.txt', 'w')      # オープン（テキスト＋書込みモード）

print('Hello!\nHow are you?', file=f)   # 末尾に改行文字が自動的に出力される

f.close()                       # クローズ
