# スポーツクラブの会員クラス（第１版：エラー）

class Member:
    """スポーツクラブの会員クラス（第１版）"""
    pass

# 会員クラスのテスト

yamada = Member()
yamada.no = 15
yamada.name = '山田太郎'
yamada.weight = 72.7

sekine = Member()
sekine.no = 38
sekine.name = '関根信彦'
sekine.weigth = 65.3    # スペルミス

print('{}: {} {}kg'.format(yamada.no, yamada.name, yamada.weight))
print('{}: {} {}kg'.format(sekine.no, sekine.name, sekine.weight))
