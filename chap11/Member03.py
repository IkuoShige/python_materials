# スポーツクラブの会員クラス（第３版）

class Member:
    """スポーツクラブの会員クラス（第３版）"""

    def __init__(self, no: int, name: str, weight: float) -> None:
        """コンストラクタ"""
        self.__no = no
        self.__name = name
        self.__weight = weight

    def lose_weight(self, loss: float) -> None:
        """lossキロ減量"""
        self.__weight -= loss

    def print(self) -> None:
        """データ表示"""
        print('{}: {} {}kg'.format(self.__no, self.__name, self.__weight))

# 会員クラスのテスト

yamada = Member(15, '山田太郎', 72.7)
sekine = Member(37, '関根信彦', 65.3)

yamada.lose_weight(3.5)     # 山田君が3.5kg減量
sekine.lose_weight(5.3)     # 関根君が5.3kg減量

yamada.print()
sekine.print()
