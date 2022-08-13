# 文字列内の全文字を逆順に走査して表示（reserved関数を利用）

s = input('文字列：')

for ch in reversed(s):
    print(ch, end='')
print()
