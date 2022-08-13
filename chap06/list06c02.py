# f文字列による文字列の連結

s1 = input('文字列s1：')
s2 = input('文字列s2：')
no = int(input('整数値no：'))

print(f'{s1}{s2}')          # 文字列 + 文字列
print(f'{s1}{no}{s2}')      # 文字列 + 整数 + 文字列
