# ファイルから文字列を読み込んで表示（例外処理）

try:
    f = open('hello.txt', 'r')
    try:
        for line in f:
            print(line, end='')
    except OSError:
        pass             # 読込み失敗時の対処
    finally:
        f.close()
except OSError:
    pass                 # オープン失敗時の対処
