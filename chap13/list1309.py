# バイナリファイルの任意の位置の文字を読み込む

with open('binfile.bin', 'br') as f:
    while True:
        pos = int(input('位置：'))
        f.seek(pos)
        c = f.read(1)
        print(c[0])

        retry = input('もう一度[Y/N]：')
        if retry in {'N', 'n'}:
            break
