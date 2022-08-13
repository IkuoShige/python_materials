# 辞書に格納されている人物の情報を表示

def put_person(**person):
    """辞書person内の情報を表示"""
    if 'name' in person: print('名前 =', person['name'], end='  ')
    if 'visa' in person: print('国籍 =', person['visa'], end='  ')
    if 'age'  in person: print('年齢 =', person['age'],  end='  ')
    print()  # 改行

put_person(name='中田', visa='日本', age=27)
put_person(name='趙', visa='中国')
