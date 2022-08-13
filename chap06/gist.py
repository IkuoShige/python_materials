# 第６章 まとめ

s1 = input('文字列s1：')
s2 = input('文字列s2：')

idx = s1.find(s2)
if idx == -1:
    print('s1中にs2は含まれません。')
else:
    print(s1)
    # idx個のスペースの後ろにs2を表示
    print(' ' * idx, end='')
    print(s2)

    # s1に含まれるs2をすべて反転
    s1 = s1.replace(s2, s2[::-1])
    print()
    print('照合部分を反転しました。')
    print(s1)

    # s1に含まれるs2[::-1]をすべて削除
    s1 = s1.replace(s2[::-1], '')
    print()
    print('照合部分を削除しました。')
    print(s1)
print()

# formatメソッドの応用例
x = float(input('実数値：'))
w = int(input('表示全桁数：'))
p = int(input('小数部桁数：'))

print('{{:{}.{}f}}'.format(w, p).format(x))
