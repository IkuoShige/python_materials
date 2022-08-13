# 敬称を付けて挨拶する関数（デフォルト値をもつ仮引数）

def hello(name, honorific = 'さん'):
    """敬称を付けて挨拶する"""
    print('こんにちは、{}{}。'.format(name, honorific))

hello('田中')
hello('関根', '君')
hello('西田', '先生')
