# ペットクラスとロボットペットクラス

class Pet:
    """ペットクラス"""

    def __init__(self, name: str, master: str) -> None:
        """コンストラクタ"""
        self._name = name           # 名前
        self._master = master       # 主人の名前

    def introduce(self) -> None:
        """自己紹介"""
        print('僕の名前は{}です！'.format(self._name))
        print('ご主人様は{}です！'.format(self._master))

    def __str__(self) -> str:
        """文字列化"""
        return self._name + ' <<' + self._master + '>>'

    def print(self) -> None:
        """表示（__str__が返却する文字列を表示して改行）"""
        print(self.__str__())

class RobotPet(Pet):
    """ロボットペットクラス"""

    def __init__(self, name: str, master: str, type_no: str) -> None:
        """コンストラクタ"""
        super().__init__(name, master)  # 基底クラスのコンストラクタを呼び出す
        self._type_no = type_no         # 型番

    def introduce(self) -> None:
        """自己紹介"""
        print('◆僕はロボット。名前は{}。'.format(self._name))
        print('◆型番は{}。'.format(self._type_no))
        print('◆僕の主人は{}。'.format(self._master))

    def __str__(self) -> str:
        """文字列化"""
        return(self._name + ' [[' + self._type_no + ']]'
                          + ' <<' + self._master + '>>')

    def work(self, sw: int) -> None:
        """家事を行う"""
        if   sw == 0: print('掃除します。')
        elif sw == 1: print('洗濯します。')
        elif sw == 2: print('炊事します。')

# ペットクラス群のテスト

kurt = Pet('Kurt', 'アイ')
kurt.introduce()
print(kurt)

r2d2 = RobotPet('R2D2', 'ルーク', 'R2')
r2d2.introduce()
print(r2d2)

def self_introduce(obj: object) -> None:
    """objに対して自己紹介をお願いする"""
    obj.introduce()

self_introduce(kurt)
self_introduce(r2d2)

# ペットクラス群のテスト（続き）

# kurtはPet型インスタンス
kurt.print()

# r2d2はRobotPet型インスタンス
r2d2.print()
r2d2.work(1)
