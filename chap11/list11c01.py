# 名前修飾を確認

class C():
    __abc = 5

# 変更後の名前でアクセス可能
print(C._C__abc)

# 本来の名前ではアクセス不能
print(C.__abc)
