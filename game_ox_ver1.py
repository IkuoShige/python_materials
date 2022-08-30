class othelo_Board:
    def __init__(self, tate, yoko) -> None:
        self.__tate = tate
        self.__yoko = yoko
        self.__list = [['-'] * 3 for i in range(3)]

    def set(self, s):
        for i in range(self.__yoko):
            for j in range(self.__tate):
                self.__list[i][j] = s

    def show(self):
        print(" ")
        for i in range(self.__yoko):
            print(" " + str(i), end="")
        print("")
        for i in range(self.__yoko):
            print(i, end="")
            for j in range(self.__tate):
                print(self.__list[i][j], end=" ")
            print("")

    def turn(self, s):
        print(str(s)+"の番です")
        #b, c = int(input("入力してください"))
        b, c = (int(x) for x in input().split())
        if self.__list[b][c] != '-':
            print("入力されています")
            return 1
        self.__list[b][c] = s
        return 0

    def judge(self, s):
        for j in range(self.__tate):
            for i in range(self.__yoko):
                if self.__list[i][j] != s:
                    break
                if i == self.__yoko-1:
                    return 1
        for i in range(self.__yoko):
            for j in range(self.__tate):
                if self.__list[i][j] != s:
                    break
                if j==self.__tate-1:
                    return 1
        for i in range(self.__yoko):
            if self.__list[i][i] != s:
                break
            if i == self.__yoko-1:
                return 1
        for i in range(self.__yoko):
            if self.__list[i][self.__yoko-1-i] != s:
                break
            if i == self.__yoko-1:
                return 1
        for i in range(self.__yoko):
            for j in range(self.__tate):
                if self.__list[i][j] == '-':
                    return 0
        return 2

    def judge_P(self, s):
        if othelo_Board.turn(self, s)!=0 and othelo_Board.turn(self, s)!=1:
            othelo_Board.show(self)
        else: othelo_Board.show(self)
        if othelo_Board.judge(self, s)!=0:
            return 1

    def judge_V(self, s):
        for i in s:
            if othelo_Board.judge(self, i)==1:
                print("{}の勝ち".format(i))

list_turn = ['o', 'x', '-']
game = othelo_Board(3, 3)
game.set('-')
game.show()

while(True):
    if game.judge_P('o') == 1:
        break
    if game.judge_P('x') == 1:
        break
game.judge_V(list_turn)
