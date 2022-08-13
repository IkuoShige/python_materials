# 辞書化されたキーワード引数の情報を表示する

def print_kwargs(s, **kwargs):
    """辞書化されたキーワード引数を受け取るkwargsの情報を表示"""
    print(s)
    print('type(kwargs) =', type(kwargs))
    print('len(kwargs)  =', len(kwargs))
    print('kwqrgs       =', kwargs)

print_kwargs('１番', spring='春', summer='夏')
print()
print_kwargs('２番', spring='春')
