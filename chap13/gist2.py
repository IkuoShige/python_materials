# 第13章 まとめ（その２）
# List 13-7で作ったバイナリファイルの任意の位置の文字を読み書き

with open('binfile.bin', 'br+') as f:
    while True:
        pos = int(input('位置：'))
        f.seek(pos)
        c = f.read(1)
        print(c[0])

        retry = input('値の変更[Y/N]：')
        if retry in {'Y', 'y'}:
            value = int(input('0～255の値：'))
            if 0 <= value <= 255:
                f.seek(pos)
                f.write(bytes([value]))
            else:
                print('不正な値です。')

        retry = input('もう一度[Y/N]：')
        if retry in {'N', 'n'}:
            break
