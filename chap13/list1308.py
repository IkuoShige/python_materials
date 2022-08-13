# バイナリファイルから読み込む

with open('binfile.bin', 'br') as f:
    bin = f.read()                      # すべてを読み込む
    for c in bin:
        print(int(c))
