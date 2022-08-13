# formatメソッドの余白と揃えの指定

print('{:<12}'.format(77))     # 左寄せ
print('{:>12}'.format(77))     # 右寄せ
print('{:^12}'.format(77))     # 中央揃え
print('{:=12}'.format(-77))    # 符号 余白文字 数値
print('{:*<12}'.format(77))    # これ以降、余白文字は'*'
print('{:*>12}'.format(77))
print('{:*^12}'.format(77))
print('{:*=12}'.format(-77))
