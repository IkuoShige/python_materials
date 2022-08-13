# 辞書に格納されている人物の情報を表示

def put_person(name=None, visa=None, age=None):
    """キーワード引数に受け取った人物の情報を表示"""
    if name != None: print('名前 =', name, end='  ')
    if visa != None: print('国籍 =', visa, end='  ')
    if age  != None: print('年齢 =', age,  end='  ')
    print()  # 改行

put_person(name='中田', visa='日本', age=27)
put_person(name='趙', visa='中国')
