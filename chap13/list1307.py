# バイナリファイルに0x00～0xffを書き込む

with open('binfile.bin', 'bw') as f:     # バイナリの書込みモード
    f.write(bytes(range(0, 256)))
