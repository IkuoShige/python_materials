# 読み込んだ文字はアルファベットの何番目か

from string import *

c = input('アルファベット：')

idx = ascii_lowercase.find(c)
if idx != -1:
    print('小文字の{}番目です。'.format(idx + 1))
else:
    idx = ascii_uppercase.find(c)
    if idx != -1:
        print('大文字の{}番目です。'.format(idx + 1))
    else:
        print('違う文字です。')
