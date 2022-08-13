# f文字列による書式化（生成した文字列を表示）

a = int(input('整数a：'))
b = int(input('整数b：'))
c = int(input('整数c：'))
n = int(input('整数n：'))
f1 = float(input('実数f1：'))
f2 = float(input('実数f2：'))
s = input('文字列s：')
print()
print(f'a / b = {a / b}')
print(f'a % b = {a % b}')
print(f'a // b = {a // b}')
print(f'bはaの{a / b:%}')        # 百分率
print()
print(f'     a    b    c')       # 正　負  
print(f'[+]{a:+5}{b:+5}{c:+5}')  # '+' '-'
print(f'[-]{a:-5}{b:-5}{c:-5}')  # 　　'-'
print(f'[ ]{a: 5}{b: 5}{c: 5}')  # ' ' '-'
print()
print(f'{c:<12}')       # 左寄せ
print(f'{c:>12}')       # 右寄せ
print(f'{c:^12}')       # 中央揃え
print(f'{c:=12}')       # 符号の後ろに余白文字
print()
print(f'n = {n:4}')     # 少なくとも４桁
print(f'n = {n:6}')     # 少なくとも６桁
print(f'n = {n:8}')     # 少なくとも８桁
print(f'n = {n:,}')     # ３桁ごとに,
print()
print(f'n = ({n:b})2')  # ２進数
print(f'n = ({n:o})8')  # ８進数
print(f'n = ({n})10')   # 10進数
print(f'n = ({n:x})16') # 16進数（小文字）
print(f'n = ({n:X})16') # 16進数（大文字）
print()
print(f'f1 = {f1:e}')   # 指数形式
print(f'f1 = {f1:f}')   # 固定小数点形式
print(f'f1 = {f1:g}')   # 形式を自動判別
print()
print(f'f1 = {f1:.7f}')    # 精度は7
print(f'f1 = {f1:12f}')    # 全体で12
print(f'f1 = {f1:12.7f}')  # 全体で12＋精度は7
print()
print(f'f2 = {f2:.0f}')    # 小数部がなければ省略
print(f'f2 = {f2:#.0f}')   # 小数部がなくても小数点
print()
print(f'{s:*<12}')      # 左寄せ
print(f'{s:*>12}')      # 右寄せ
print(f'{s:*^12}')      # 中央揃え
print()

for i in range(65, 91):   # 65～90の文字
    print(f'{i:c}', end='') 
print()
