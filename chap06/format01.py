# formatメソッドの引数の順序の指定

a, b, c = 1, 2, 3
print('a = {}, b = {}, c = {}'.format(a, b, c))
print('b = {1}, c = {2}, a = {0}'.format(a, b, c))
print('b = {kb}, c = {kc}, a = {ka}'.format(ka=a, kb=b, kc=c))
