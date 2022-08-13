# 文字列内の全文字を逆順に走査して表示

s = input('文字列：')

for ch in s[::-1]:
    print(ch, end='')
print()
