# スポーツクラブの会員クラス（第４版）

class Member:
    """スポーツクラブの会員クラス（第４版）"""

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

    @property
    def weight(self) -> float:
        """体重を取得（ゲッタ）"""
        return self.__weight

    @weight.setter
    def weight(self, weight: float) -> None:
        """体重を設定（セッタ）"""
        self.__weight = weight if weight > 0.0 else 0.0

# 会員クラスのテスト

yamada = Member(15, '山田太郎', 72.7)

yamada.weight = 67.3                        # 山田君の体重を設定
print('yamada.weight =', yamada.weight)     # 山田君の体重を取得
