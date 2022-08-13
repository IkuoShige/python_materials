# スポーツクラブの会員クラス（第２版）

class Member:
    """スポーツクラブの会員クラス（第２版）"""

    def __init__(self, no: int, name: str, weight: float) -> None:
        """コンストラクタ"""
        self.no = no            # 会員番号
        self.name = name        # 氏名
        self.weight = weight    # 体重

    def print(self) -> None:
        """データ表示"""
        print('{}: {} {}kg'.format(self.no, self.name, self.weight))

# 会員クラスのテスト

yamada = Member(15, '山田太郎', 72.7)
sekine = Member(37, '関根信彦', 65.3)

yamada.print()
sekine.print()
