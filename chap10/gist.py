"""表示モジュールputの利用例"""

import put

print('左下直角二等辺三角形')
n = int(input('短辺：'))

# 短辺nの左下直角二等辺三角形を'*'で表示
for i in range(1, n + 1):
    put.put_star(i)
    print()

print('長方形')
h = int(input('高さ：'))
w = int(input('横幅：'))

# 高さhで横幅wの長方形を'+'で表示
for _ in range(1, h + 1):
    put.puts(n=w, s='+')
    print()

# モジュールputの文書化文字列を表示
print('\n' + put.__doc__)
